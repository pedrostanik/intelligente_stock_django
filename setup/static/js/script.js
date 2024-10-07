function toggleChat() {
    var chatBox = document.getElementById('chatBox');
    if (chatBox.style.display === 'none' || chatBox.style.display === '') {
        chatBox.style.display = 'flex';  // Mostra o chat
    } else {
        chatBox.style.display = 'none';  // Esconde o chat
    }
}

async function sendMessage() {
    var chatBody = document.getElementById('chatBody');
    var chatInput = document.getElementById('chatInput');
    console.log("chatInput: " + chatInput)
    var message = chatInput.value.trim();
    console.log("message: " + message)


    if (message !== '') {

        messageFormatada = "[Usuário]: " + message
        var messageElement = document.createElement('div');
        messageElement.textContent = messageFormatada;
        messageElement.classList.add('chat-message');
        chatBody.appendChild(messageElement);

        chatInput.value = ''; // Limpa o campo de input
        chatBody.scrollTop = chatBody.scrollHeight; // Rola para o final

        smartAnswer = await connectMessage(message)
        console.log("smartAnswer: " + smartAnswer)

        if (smartAnswer != '') {
            smartAnswer = "[Sistema]: " + smartAnswer;
            var SmartMessageElement = document.createElement('div');
            SmartMessageElement.textContent = smartAnswer;
            SmartMessageElement.classList.add('chat-message');
            chatBody.appendChild(SmartMessageElement);
            chatBody.scrollTop = chatBody.scrollHeight; // Rola para o final
        }
    }
}

async function connectMessage(message) {
    // Monta a URL com a mensagem codificada
    const url = `/respond_message/${encodeURIComponent(message)}`;

    try {
        const response = await fetch(url);  // Espera a resposta do fetch
        if (!response.ok) {
            throw new Error('Erro na requisição');
        }

        const data = await response.text();  // Recebe a resposta como texto
        console.log("data: " + data)
        return data;  // Retorna os dados
    } catch (error) {
        console.error('Erro:', error);
        throw error;  // Propaga o erro se necessário
    }
}

