const itemsBought = {}

// Função para criar o event listener de cada produto
document.querySelectorAll(".product-item").forEach(productItem => {
    const incrementButton = productItem.querySelector("button[id^='incrementButton']");
    const decrementButton = productItem.querySelector("button[id^='decrementButton']");
    const qttyProduct = productItem.querySelector("input[id^='qttyProduct']");
    const productId = productItem.getAttribute('data-id');
    const warningStorage = productItem.querySelector("p[id^='warningStorage']");

    incrementButton.addEventListener('click', () => {
        let value = parseInt(qttyProduct.value);

        // available = String(checkStock(value, productId));  
        checkStock(value, productId).then(available => {
            console.log("available: ", available);
            if (available) {
                value += 1; // Incrementa o valor
                qttyProduct.value = value;
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
        let value = parseInt(qttyProduct.value);
        if (value > 0) { // Previne valor negativo
            value -= 1;
        }
        qttyProduct.value = value;
        warningStorage.textContent = "";
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const botaoCart = document.querySelector('.botao_cart');

    botaoCart.addEventListener('click', function() {
        // Lógica para finalizar a compra, por exemplo, redirecionar para o checkout
        console.log("Botão 'Finalizar Compra' clicado!");

        // Redirecionar para a página de checkout
        // window.location.href = "{% url 'checkout' %}"; // Substitua 'checkout' pelo nome da sua URL
        callCartAjax();
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome desejado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function callCartAjax() {
    fetch('cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Adicione o token CSRF para segurança
        },
        body: JSON.stringify(itemsBought)
    })
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        throw new Error('Network response was not ok.')
    })
    .then(html => {
        document.getElementById('cart-container').innerHTML = html;
    })
    .catch(error => {
        console.error('Houve um problema com a requisição fetch:', error);
    });
}

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


