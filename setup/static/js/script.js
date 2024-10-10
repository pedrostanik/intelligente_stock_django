const itemsBought = {}


// Função para criar o event listener de cada produto
document.querySelectorAll(".product-item").forEach(productItem => {
    const incrementButton = productItem.querySelector("button[id^='incrementButton']");
    const decrementButton = productItem.querySelector("button[id^='decrementButton']");
    const qttyProduct = productItem.querySelector("span[id^='qttyProduct']");
    const productId = productItem.getAttribute('data-id');
    const warningStorage = productItem.querySelector("p[id^='warningStorage']");

    incrementButton.addEventListener('click', () => {
        let value = parseInt(qttyProduct.textContent);

        // available = String(checkStock(value, productId));  
        checkStock(value, productId).then(available => {
            console.log("available: ", available);
            if (available) {
                value += 1; // Incrementa o valor
                qttyProduct.textContent = value;
                warningStorage.textContent = ""
                itemsBought[productId] = value
                console.log(itemsBought)
            } else {
                warningStorage.textContent = "There is only " + value + " products in storage!"
            }
        }).catch(error => {
            console.error("Erro ao checar o estoque:", error);
        });



    });

    decrementButton.addEventListener('click', () => {
        let value = parseInt(qttyProduct.textContent);
        if (value > 0) { // Previne valor negativo
            value -= 1;
        }
        qttyProduct.textContent = value;
        warningStorage.textContent = "";
    });
});

async function checkStock(currentQtty, productId) {
    const url = `/check_storage/${currentQtty}/${productId}`;

    try {
        const response = await fetch(url);  // Espera a resposta do fetch
        if (!response.ok) {
            throw new Error('Erro na requisição');
        }

        const data = await response.json();  // Recebe a resposta como texto

        console.log('data: ' + JSON.stringify(data, null, 2))
        return data.disponivel;  // Retorna os dados
    } catch (error) {
        console.error('Erro:', error);
        throw error;  // Propaga o erro se necessário
    }
}


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


