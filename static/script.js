document.addEventListener('DOMContentLoaded', () => {
    loadProgress();
});

// Run Code Function
async function runCode(lessonId) {
    const code = document.getElementById('codeEditor').value;
    const outputArea = document.getElementById('outputHelpers');
    const btn = document.getElementById('runBtn');

    btn.innerText = "Running...";

    const response = await fetch('/run_code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code, lesson_id: lessonId })
    });

    const data = await response.json();

    outputArea.innerText = data.output;
    btn.innerText = "▶ Run Code";

    if (data.passed) {
        outputArea.style.color = "#22c55e"; // Green text
        saveProgress(lessonId);
        document.getElementById('successModal').style.display = 'flex';
    } else {
        outputArea.style.color = "#ef4444"; // Red text
    }
}

// Save Progress to Browser LocalStorage
function saveProgress(completedLevelId) {
    let progress = parseInt(localStorage.getItem('geoPythonLevel')) || 1;
    
    // Only increase if we just beat the highest unlocked level
    if (completedLevelId === progress) {
        localStorage.setItem('geoPythonLevel', progress + 1);
        localStorage.setItem('geoPythonXP', (progress * 150)); // Add XP
    }
}

// Update Dashboard UI based on saved progress
function loadProgress() {
    const currentLevel = parseInt(localStorage.getItem('geoPythonLevel')) || 1;
    const currentXP = localStorage.getItem('geoPythonXP') || 0;

    // Update Header
    const levelDisplay = document.getElementById('userLevel');
    const xpDisplay = document.getElementById('userXP');
    if(levelDisplay) levelDisplay.innerText = currentLevel > 3 ? "Analyst" : "Novice";
    if(xpDisplay) xpDisplay.innerText = currentXP;

    // Unlock Levels
    for (let i = 1; i <= 3; i++) {
        const lockStatus = document.getElementById(`status-${i}`);
        const card = document.getElementById(`lesson-card-${i}`);
        
        if (i <= currentLevel) {
            if(lockStatus) {
                lockStatus.innerText = "🔓 Open";
                lockStatus.className = "status unlocked";
            }
            if(card) card.classList.remove('locked');
        }
    }
}