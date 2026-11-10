/**
 * CodeQuest Duolingo-style Interleaved Stepper & Quiz Engine
 * Mengatur alur langkah materi -> soal secara selang-seling, efek suara Web Audio API,
 * navigasi maju-mundur, validasi jawaban di tempat, dan progres localStorage.
 */

(function () {
    let currentStepIndex = 0;
    let selectedChoice = null;
    let isCurrentStepChecked = false;
    let isCurrentStepPassed = false;

    // Pelacak akurasi percobaan pertama
    const quizMistakes = {}; // { stepIndex: boolean }
    let totalQuizzes = 0;

    // DOM Elements
    const stepCard = document.getElementById('step-card');
    const completionCard = document.getElementById('completion-card');
    const progressFill = document.getElementById('duo-progress-fill');
    const stepCounter = document.getElementById('duo-step-counter');
    const btnPrev = document.getElementById('btn-prev-step');
    const btnAction = document.getElementById('btn-action');
    const actionDock = document.getElementById('action-dock');
    const dockFeedback = document.getElementById('dock-feedback');
    const feedbackIcon = document.getElementById('feedback-icon');
    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackExplanation = document.getElementById('feedback-explanation');
    const completionAccuracy = document.getElementById('completion-accuracy');

    // =========================================================================
    // Web Audio API Sound Synthesizer (Zero External Audio Files)
    // =========================================================================
    let audioCtx = null;

    function getAudioContext() {
        if (!audioCtx) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (AudioContextClass) {
                audioCtx = new AudioContextClass();
            }
        }
        if (audioCtx && audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        return audioCtx;
    }

    function playSoundSuccess() {
        try {
            const ctx = getAudioContext();
            if (!ctx) return;

            const now = ctx.currentTime;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.type = 'triangle';
            // Duolingo-like bright 2-tone chime
            osc.frequency.setValueAtTime(587.33, now); // D5
            osc.frequency.setValueAtTime(880.00, now + 0.1); // A5

            gain.gain.setValueAtTime(0.18, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);

            osc.connect(gain);
            gain.connect(ctx.destination);

            osc.start(now);
            osc.stop(now + 0.45);
        } catch (e) {
            console.warn("Audio playback not supported", e);
        }
    }

    function playSoundError() {
        try {
            const ctx = getAudioContext();
            if (!ctx) return;

            const now = ctx.currentTime;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.type = 'sawtooth';
            // Gentle low-pitch buzz
            osc.frequency.setValueAtTime(190, now);
            osc.frequency.linearRampToValueAtTime(140, now + 0.25);

            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);

            osc.connect(gain);
            gain.connect(ctx.destination);

            osc.start(now);
            osc.stop(now + 0.3);
        } catch (e) {
            console.warn("Audio playback not supported", e);
        }
    }

    // =========================================================================
    // Inisialisasi Stepper
    // =========================================================================
    function initStepper() {
        if (!LESSON_STEPS || LESSON_STEPS.length === 0) {
            stepCard.innerHTML = "<p>Tidak ada langkah pelajaran yang dimuat.</p>";
            return;
        }

        totalQuizzes = LESSON_STEPS.filter(s => s.type === 'quiz').length;
        currentStepIndex = 0;
        renderCurrentStep();
    }

    // =========================================================================
    // Render Step Aktif (Materi / Kuis)
    // =========================================================================
    function renderCurrentStep() {
        const totalSteps = LESSON_STEPS.length;
        const step = LESSON_STEPS[currentStepIndex];

        // 1. Update Progress Bar & Counter
        const progressPercent = Math.round((currentStepIndex / totalSteps) * 100);
        progressFill.style.width = `${progressPercent}%`;
        stepCounter.textContent = `Langkah ${currentStepIndex + 1} dari ${totalSteps}`;

        // 2. Tombol Navigasi Mundur (Disabled jika di langkah pertama)
        btnPrev.disabled = (currentStepIndex === 0);

        // 3. Reset State & Feedback Dock
        selectedChoice = null;
        isCurrentStepChecked = false;
        isCurrentStepPassed = false;
        hideFeedback();

        // 4. Render Kartu berdasarkan Tipe
        if (step.type === 'material') {
            renderMaterialStep(step);
        } else if (step.type === 'quiz') {
            renderQuizStep(step);
        }
    }

    function renderMaterialStep(step) {
        let contentHtml = '';

        (step.content_blocks || []).forEach(block => {
            if (block.type === 'paragraph') {
                contentHtml += `<p class="step-text">${block.text}</p>`;
            } else if (block.type === 'code') {
                contentHtml += `
                    <div class="code-container">
                        <div class="code-header">
                            <span class="code-lang">Python</span>
                            <span class="code-dot"></span>
                        </div>
                        <pre><code>${escapeHtml(block.code)}</code></pre>
                    </div>
                `;
            } else if (block.type === 'callout') {
                const listItems = (block.items || []).map(it => `<li>${it}</li>`).join('');
                contentHtml += `
                    <div class="callout-box">
                        <h4 class="callout-title">💡 ${escapeHtml(block.title)}</h4>
                        <ul class="callout-list">${listItems}</ul>
                    </div>
                `;
            }
        });

        stepCard.innerHTML = `
            <div class="step-badge">📖 ${escapeHtml(step.badge || 'Materi')}</div>
            <h2 class="step-title">${escapeHtml(step.title)}</h2>
            <div class="step-material-body">
                ${contentHtml}
            </div>
        `;

        // Untuk materi: Tombol langsung aktif untuk lanjut
        btnAction.disabled = false;
        btnAction.className = 'btn-primary btn-block';
        btnAction.innerHTML = 'Lanjutkan &rarr;';
        isCurrentStepPassed = true;
    }

    function renderQuizStep(step) {
        let choicesHtml = (step.choices || []).map(c => `
            <div class="choice-item" data-choice-id="${c.id}" onclick="onSelectChoice('${c.id}')">
                <span class="choice-key">${c.id}</span>
                <span class="choice-text">${escapeHtml(c.text)}</span>
            </div>
        `).join('');

        stepCard.innerHTML = `
            <div class="step-badge badge-quiz">⚡ ${escapeHtml(step.badge || 'Latihan')}</div>
            <div class="quiz-question-box">
                <h3 class="quiz-question-heading">${formatQuestionText(step.question)}</h3>
            </div>
            <div class="choices-list" id="choices-wrapper">
                ${choicesHtml}
            </div>
        `;

        // Untuk kuis: Tombol "Periksa Jawaban" dan dinonaktifkan sampai ada pilihan
        btnAction.disabled = true;
        btnAction.className = 'btn-primary btn-block';
        btnAction.textContent = 'Periksa Jawaban';
    }

    // =========================================================================
    // Interaksi Pilihan Jawaban (Quiz Interaction)
    // =========================================================================
    window.onSelectChoice = function (choiceId) {
        selectedChoice = choiceId;

        // Visual update pada pilihan
        const allChoices = document.querySelectorAll('.choice-item');
        allChoices.forEach(item => {
            if (item.getAttribute('data-choice-id') === choiceId) {
                item.classList.add('selected');
            } else {
                item.classList.remove('selected');
            }
        });

        // Aktifkan tombol aksi
        btnAction.disabled = false;

        // Jika sebelumnya sudah dicek dan salah, pengguna bisa klik pilihan yang benar
        if (isCurrentStepChecked && !isCurrentStepPassed) {
            btnAction.textContent = 'Periksa Jawaban';
        }
    };

    function handleActionClick() {
        const step = LESSON_STEPS[currentStepIndex];

        // Jika slide materi atau kuis sudah berhasil dijawab benar -> Maju ke langkah berikutnya
        if (step.type === 'material' || (step.type === 'quiz' && isCurrentStepPassed)) {
            advanceNextStep();
            return;
        }

        // Jika kuis dan belum diperiksa (atau mengulang periksa setelah salah)
        if (step.type === 'quiz') {
            checkCurrentAnswer();
        }
    }

    function checkCurrentAnswer() {
        const step = LESSON_STEPS[currentStepIndex];
        if (!selectedChoice) return;

        isCurrentStepChecked = true;
        const isCorrect = (selectedChoice === step.answer);
        const allChoices = document.querySelectorAll('.choice-item');

        if (isCorrect) {
            // Jawaban BENAR
            isCurrentStepPassed = true;
            playSoundSuccess();

            allChoices.forEach(item => {
                const cId = item.getAttribute('data-choice-id');
                if (cId === step.answer) {
                    item.className = 'choice-item correct';
                } else {
                    item.className = 'choice-item locked';
                }
            });

            showFeedback(true, 'Luar biasa, jawabanmu benar!', step.explanation);
            btnAction.textContent = 'Lanjutkan &rarr;';
            btnAction.disabled = false;
        } else {
            // Jawaban SALAH
            isCurrentStepPassed = false;
            quizMistakes[currentStepIndex] = true;
            playSoundError();

            allChoices.forEach(item => {
                const cId = item.getAttribute('data-choice-id');
                if (cId === selectedChoice) {
                    item.className = 'choice-item wrong';
                } else {
                    item.className = 'choice-item';
                }
            });

            showFeedback(
                false,
                'Belum tepat. Coba lagi!',
                `${step.explanation} (Pilih opsi yang benar untuk melanjutkan).`
            );
            btnAction.textContent = 'Coba Pilih Jawaban Lain';
            btnAction.disabled = true; // Dinonaktifkan sampai pengguna memilih opsi lain
        }
    }

    function advanceNextStep() {
        currentStepIndex++;
        if (currentStepIndex < LESSON_STEPS.length) {
            renderCurrentStep();
        } else {
            finishLesson();
        }
    }

    function handlePrevStep() {
        if (currentStepIndex > 0) {
            currentStepIndex--;
            renderCurrentStep();
        }
    }

    // =========================================================================
    // Layar Selesai & Penghitungan Skor
    // =========================================================================
    function finishLesson() {
        progressFill.style.width = '100%';
        stepCard.classList.add('hidden');
        actionDock.classList.add('hidden');
        completionCard.classList.remove('hidden');

        playSoundSuccess();

        // Hitung akurasi first-try
        let firstTryCount = 0;
        LESSON_STEPS.forEach((s, idx) => {
            if (s.type === 'quiz' && !quizMistakes[idx]) {
                firstTryCount++;
            }
        });

        completionAccuracy.textContent = `${firstTryCount} / ${totalQuizzes} Benar Sekali Coba`;

        // Simpan progres ke browser localStorage
        saveCompletionData();
    }

    function saveCompletionData() {
        try {
            const completed = JSON.parse(localStorage.getItem('cq_completed_lessons') || '[]');
            const isNew = !completed.includes(LESSON_ID);

            if (isNew) {
                completed.push(LESSON_ID);
                localStorage.setItem('cq_completed_lessons', JSON.stringify(completed));

                const currentXp = parseInt(localStorage.getItem('cq_total_xp') || '0', 10);
                const updatedXp = currentXp + (LESSON_XP || 50);
                localStorage.setItem('cq_total_xp', updatedXp.toString());
            }

            if (typeof updateGlobalStats === 'function') {
                updateGlobalStats();
            }
        } catch (e) {
            console.error("Gagal menyimpan ke localStorage:", e);
        }
    }

    window.restartLesson = function () {
        completionCard.classList.add('hidden');
        stepCard.classList.remove('hidden');
        actionDock.classList.remove('hidden');
        Object.keys(quizMistakes).forEach(k => delete quizMistakes[k]);
        currentStepIndex = 0;
        renderCurrentStep();
    };

    // =========================================================================
    // Feedback Banner Helpers
    // =========================================================================
    function showFeedback(isCorrect, title, desc) {
        dockFeedback.classList.remove('hidden', 'correct', 'wrong');
        dockFeedback.classList.add(isCorrect ? 'correct' : 'wrong');
        feedbackIcon.textContent = isCorrect ? '✓' : '✗';
        feedbackTitle.textContent = title;
        feedbackExplanation.textContent = desc;
    }

    function hideFeedback() {
        dockFeedback.classList.add('hidden');
        dockFeedback.classList.remove('correct', 'wrong');
    }

    function formatQuestionText(text) {
        if (!text) return '';
        // Ubah `kode` menjadi <code>kode</code>
        let formatted = escapeHtml(text);
        formatted = formatted.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');
        return formatted.replace(/\n/g, '<br>');
    }

    function escapeHtml(str) {
        if (!str) return '';
        return str
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    // =========================================================================
    // Event Listeners
    // =========================================================================
    btnAction.addEventListener('click', handleActionClick);
    btnPrev.addEventListener('click', handlePrevStep);

    document.addEventListener('DOMContentLoaded', initStepper);
})();
