document.addEventListener('DOMContentLoaded', () => {
    const detailsForm = document.getElementById('details-form');
    const questionForm = document.getElementById('question-form');
    const chatWindow = document.getElementById('chat-window');
    
    // Store user details to send with follow-up questions
    let userDetails = {};

    // --- Event Listener for Initial Details Form ---
    detailsForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // 1. Collect data from the form
        userDetails = {
            name: document.getElementById('name').value,
            hobby: document.getElementById('hobby').value,
            occupation: document.getElementById('occupation').value,
            future_goal: document.getElementById('future_goal').value,
            positive_moment: document.getElementById('positive_moment').value,
            negative_moment: document.getElementById('negative_moment').value,
        };

        // 2. Display user's provided info in the chat
        const userSummary = `
            Name: ${userDetails.name}<br>
            Hobby: ${userDetails.hobby}<br>
            Occupation: ${userDetails.occupation}<br>
            Goal: ${userDetails.future_goal}
        `;
        addMessage(userSummary, 'user-message');
        
        // 3. Hide details form, show question form
        detailsForm.classList.add('hidden');
        showTypingIndicator();

        // 4. Send data to backend for prediction
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userDetails),
            });
            const data = await response.json();
            
            removeTypingIndicator();
            addMessage(data.answer, 'bot-message');
            questionForm.classList.remove('hidden');
            document.getElementById('question-input').focus();

        } catch (error) {
            removeTypingIndicator();
            addMessage("Sorry, the connection to the spirit world is weak. Please try again.", 'bot-message');
            console.error('Error:', error);
        }
    });

    // --- Event Listener for Follow-up Questions ---
    questionForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const questionInput = document.getElementById('question-input');
        const question = questionInput.value.trim();

        if (!question) return;

        // 1. Display user's question
        addMessage(question, 'user-message');
        questionInput.value = '';
        showTypingIndicator();

        // 2. Send question and original details to backend
        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: question,
                    details: userDetails // Send context
                }),
            });
            const data = await response.json();

            removeTypingIndicator();
            addMessage(data.answer, 'bot-message');

        } catch (error) {
            removeTypingIndicator();
            addMessage("My apologies, I sense a disturbance in the ether. I cannot answer right now.", 'bot-message');
            console.error('Error:', error);
        }
    });

    // --- Helper Functions ---
    function addMessage(text, className) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', className);
        
        const p = document.createElement('p');
        p.innerHTML = text; // Use innerHTML to render line breaks
        messageDiv.appendChild(p);

        chatWindow.appendChild(messageDiv);
        // Scroll to the latest message
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('bot-message', 'typing-indicator');
        typingDiv.innerHTML = '<span></span><span></span><span></span>';
        chatWindow.appendChild(typingDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function removeTypingIndicator() {
        const indicator = document.querySelector('.typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }
});