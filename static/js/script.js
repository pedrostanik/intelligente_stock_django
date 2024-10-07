function toggleChat() {
    var chatBox = document.getElementById('chatBox');
    if (chatBox.style.display === 'none' || chatBox.style.display === '') {
        chatBox.style.display = 'flex';  // Mostra o chat
    } else {
        chatBox.style.display = 'none';  // Esconde o chat
    }
}

function sendMessage() {
    var chatBody = document.getElementById('chatBody');
    var chatInput = document.getElementById('chatInput');
    var message = chatInput.value.trim();

    if (message !== '') {
        var messageElement = document.createElement('div');
        messageElement.textContent = message;
        messageElement.classList.add('chat-message');
        chatBody.appendChild(messageElement);

        chatInput.value = ''; // Limpa o campo de input
        chatBody.scrollTop = chatBody.scrollHeight; // Rola para o final
    }
}
