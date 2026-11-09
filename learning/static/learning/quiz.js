/**
 * CodeQuest Interactive Quiz Engine (JavaScript)
 * Menangani state kuis, validasi instan, dan penyimpanan progres ke localStorage.
 */

(function () {
    let currentIndex = 0;
    let selectedChoice = null;
    let correctCount = 0;
    let isChecked = false;

    // DOM Elements
    const contentArea = document.getElementById('quiz-content-area');
    const counterElem = document.getElementById('quiz-question-counter');
    const progressBar = document.getElementById('quiz-progress-bar');
    const btnCheck = document.getElementById('btn-check-answer');
    const btnNext = document.getElementById('btn-next-question');
    const feedbackBanner = document.getElementById('feedback-banner');
    const feedbackIcon = document.getElementById('feedback-icon');
    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackDesc = document.getElementById('feedback-desc');
    const quizCard = document.querySelector('.quiz-card');
    const resultCard = document.getElementById('quiz-result-card');
    const resultScoreText = document.getElementById('result-score-text');

    function initQuiz() {
        if (!QUIZ_QUESTIONS || QUIZ_QUESTIONS.length === 0) {
            contentArea.innerHTML = "<p>Tidak ada soal untuk modul ini.</p>";
            return;
        }
        currentIndex = 0;
        correctCount = 0;
        renderQuestion();
    }

    function renderQuestion() {
        selectedChoice = null;
        isChecked = false;

        const currentQ = QUIZ_QUESTIONS[currentIndex];
        const totalQ = QUIZ_QUESTIONS.length;

        // Update progress bar & counter
        counterElem.textContent = `Soal ${currentIndex + 1} dari ${totalQ}`;
        const progressPercent = Math.round((currentIndex / totalQ) * 100);
        progressBar.style.width = `${progressPercent}%`;

        // Reset buttons and feedback banner
        btnCheck.disabled = true;
        btnCheck.classList.remove('hidden');
        btnNext.classList.add('hidden');
        feedbackBanner.classList.add('hidden');
        feedbackBanner.className = 'feedback-banner hidden';

        // Render question text & choices
        let choicesHtml = currentQ.choices.map(c => `
            <div class="choice-item" data-choice-id="${c.id}" onclick="selectChoice('${c.id}')">
                <span class="choice-key">${c.id}</span>
                <span class="choice-text">${escapeHtml(c.text)}</span>
            </div>
        `).join('');

        contentArea.innerHTML = `
            <div class="quiz-question-text">${escapeHtml(currentQ.question)}</div>
            <div class="choices-list" id="choices-container">
                ${choicesHtml}
            </div>
        `;
    }

    window.selectChoice = function (choiceId) {
        if (isChecked) return; // Tidak bisa ganti jawaban setelah diperiksa
        selectedChoice = choiceId;

        // Highlight selected card
        const allChoices = document.querySelectorAll('.choice-item');
        allChoices.forEach(item => {
            if (item.getAttribute('data-choice-id') === choiceId) {
                item.classList.add('selected');
            } else {
                item.classList.remove('selected');
            }
        });

        // Enable check button
        btnCheck.disabled = false;
    };

    function checkAnswer() {
        if (!selectedChoice || isChecked) return;
        isChecked = true;

        const currentQ = QUIZ_QUESTIONS[currentIndex];
        const isCorrect = (selectedChoice === currentQ.answer);

        if (isCorrect) {
            correctCount++;
        }

        // Lock choices & highlight right/wrong
        const allChoices = document.querySelectorAll('.choice-item');
        allChoices.forEach(item => {
            item.classList.add('locked');
            const choiceId = item.getAttribute('data-choice-id');
            if (choiceId === currentQ.answer) {
                item.classList.add('correct');
            } else if (choiceId === selectedChoice && !isCorrect) {
                item.classList.add('wrong');
            }
        });

        // Show feedback banner
        feedbackBanner.classList.remove('hidden');
        if (isCorrect) {
            feedbackBanner.classList.add('correct');
            feedbackIcon.textContent = '✓';
            feedbackTitle.textContent = 'Hebat! Jawabanmu benar.';
        } else {
            feedbackBanner.classList.add('wrong');
            feedbackIcon.textContent = '✗';
            feedbackTitle.textContent = 'Kurang tepat. Coba perhatikan pembahasannya:';
        }
        feedbackDesc.textContent = currentQ.explanation;

        // Toggle buttons
        btnCheck.classList.add('hidden');
        btnNext.classList.remove('hidden');
    }

    function nextQuestion() {
        currentIndex++;
        if (currentIndex < QUIZ_QUESTIONS.length) {
            renderQuestion();
        } else {
            showQuizResult();
        }
    }

    function showQuizResult() {
        const totalQ = QUIZ_QUESTIONS.length;
        progressBar.style.width = '100%';

        quizCard.classList.add('hidden');
        resultCard.classList.remove('hidden');

        resultScoreText.textContent = `Skor: ${correctCount} / ${totalQ} Benar`;

        // Save progress to localStorage
        saveProgress(correctCount, totalQ);
    }

    function saveProgress(score, total) {
        try {
            // Catat daftar modul selesai
            const completed = JSON.parse(localStorage.getItem('cq_completed_lessons') || '[]');
            const isNewCompletion = !completed.includes(LESSON_ID);

            if (isNewCompletion) {
                completed.push(LESSON_ID);
                localStorage.setItem('cq_completed_lessons', JSON.stringify(completed));

                // Tambahkan XP jika baru pertama kali selesai
                const currentXp = parseInt(localStorage.getItem('cq_total_xp') || '0', 10);
                const updatedXp = currentXp + (LESSON_XP || 50);
                localStorage.setItem('cq_total_xp', updatedXp.toString());
            }

            // Panggil fungsi update navbar global jika ada
            if (typeof updateGlobalStats === 'function') {
                updateGlobalStats();
            }
        } catch (e) {
            console.error("Gagal menyimpan ke localStorage:", e);
        }
    }

    window.restartQuiz = function () {
        resultCard.classList.add('hidden');
        quizCard.classList.remove('hidden');
        initQuiz();
    };

    function escapeHtml(str) {
        if (!str) return '';
        return str
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    // Event Listeners
    btnCheck.addEventListener('click', checkAnswer);
    btnNext.addEventListener('click', nextQuestion);

    // Jalankan inisialisasi saat DOM siap
    document.addEventListener('DOMContentLoaded', initQuiz);
})();
