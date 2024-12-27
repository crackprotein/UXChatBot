const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

function clearChatLog() {
    chatLog.innerHTML = '';
}

function appendMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    chatLog.appendChild(messageDiv);
    chatLog.scrollTop = chatLog.scrollHeight; 
}

sendButton.addEventListener('click', () => {
    const message = userInput.value;
    if (message.trim() !== '') {
        clearChatLog();  
        appendMessage('user', message);
        userInput.value = '';

        fetch('http://127.0.0.1:5000/chat', { 
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('bot', data.response);
        })
        .catch(error => {
          appendMessage('bot', 'Error fetching response.');
          console.error('Error:', error);
        });
    }
});


userInput.addEventListener('keydown', (event) => {
    if(event.key === 'Enter'){
        event.preventDefault();
        sendButton.click();
    }
});
