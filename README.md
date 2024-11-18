[ENGLISH]
# 🐾 PetShop Online with Django and Chatbot 💻🛒🤖

## This project is an e-commerce system for a pet shop developed with Django, offering a unique and personalized experience for pet owners. With the integration of an intelligent chatbot, users can ask questions, receive product recommendations, and take better care of their animals.

## 🎯 Main Features
- **Pet Product Catalog**: Full management of products, including food, toys, accessories, medications, and more.
- **Shopping Cart and Checkout**: Add items to the cart, complete purchases, and track order status.
- **Custom Pet Chatbot**: A virtual assistant that:
  - Recommends products based on the pet's type and needs.
  - Answers questions about pet care.
  - Suggests promotions and special offers.
- **User System**: Registration, login, and purchase history for each customer.
- **Admin Panel**: Tools to manage products, orders, and customers.

## 🛠️ Technologies Used
- **Language**: Python
- **Backend Framework**: Django
- **Database**: SQLite (for development) or PostgreSQL (recommended for production)
- **Chatbot**: AI-based solution integrated for personalized customer service.

## 🚀 How to Run the Project
### Prerequisites
- Python
- Git
- Virtualenv (optional, but recommended)

### Setup Instructions
Clone the repository:
```bash
git clone https://github.com/pedrostanik/intelligente_stock_django.git
cd petshop
```

Create virtual environmental:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Intall dependencies:
```bash
pip install -r requirements.txt
```

Apply migrations:
```bash
python manage.py migrate
```

Start server:
```bash
python manage.py runserver
```


## 🤖 Chatbot Setup
Set up the chatbot to respond to the e-commerce needs:

Personalize responses based on pet type (dogs, cats, etc.).
Add useful information like care and nutrition tips.
Configure API keys and external services (like OpenAI or Dialogflow) in the settings.py file.

bash
python manage.py test
📂 Estrutura do Projeto
plaintext

.
├── petshop/
│   ├── settings.py      # Django project settings
│   ├── urls.py          # Project routes
│   ├── wsgi.py          # WSGI configuration for deployment
├── chatbot/             # Chatbot application
├── products/            # Product management application
├── cart/                # Shopping cart application
├── customers/           # Customer registration and management application
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── manage.py            # Django management command
├── requirements.txt     # Project dependencies

## 🐕 Future Improvements
Integration with payment gateways like Stripe or PayPal.
Implementation of a subscription system for pet food and other consumables.
Functionality to upload pet information (age, weight, allergies) for more accurate recommendations.
Support for seasonal promotions, such as "Black Friday for Pets."

## 🙌 Contributions
Contributions are welcome! Feel free to open issues and pull requests for improvements.



[PORTUGUÊS]
# 🐾 PetShop Online com Django e Chatbot 💻🛒🤖

## Este projeto é um sistema de e-commerce para petshop desenvolvido com Django, que oferece uma experiência única e personalizada para donos de pets. Com a integração de um chatbot inteligente, os usuários podem tirar dúvidas, receber recomendações de produtos e cuidar melhor de seus animais.

## 🎯 Recursos Principais
Catálogo de Produtos para Pets: Gerenciamento completo de produtos, incluindo rações, brinquedos, acessórios, medicamentos e mais.
Carrinho de Compras e Checkout: Adicione itens ao carrinho, finalize compras e acompanhe o status do pedido.
Chatbot Personalizado para Pets: Um assistente virtual que:
Recomenda produtos com base no tipo de pet e suas necessidades.
Responde perguntas sobre cuidados com os pets.
Sugere promoções e ofertas especiais.
Sistema de Usuários: Cadastro, login e histórico de compras para cada cliente.
Painel Administrativo: Ferramentas para gerenciar produtos, pedidos e clientes.

## 🛠️ Tecnologias Utilizadas
Linguagem: Python
Framework Backend: Django
Banco de Dados: SQLite (para desenvolvimento) ou PostgreSQL (recomendado para produção)
Chatbot: Solução baseada em inteligência artificial integrada para personalização de atendimento.

## 🚀 Como Executar o Projeto
Pré-requisitos
Python
Git
Virtualenv (opcional, mas recomendado)

Passos para Configuração
Clone o repositório:
Copiar código
```bash
git clone https://github.com/pedrostanik/intelligente_stock_django.git
cd petshop
```

Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Aplique as migrações do banco de dados:
```bash
python manage.py migrate
```

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```



## 🤖 Configuração do Chatbot
Configure o chatbot para responder às necessidades do e-commerce:
Personalize respostas baseadas no tipo de pet (cachorros, gatos, etc.).
Adicione informações úteis, como dicas de cuidados e nutrição.
Configure chaves de API e serviços externos (como OpenAI ou Dialogflow) no arquivo settings.py.



bash
Copiar código
python manage.py test
📂 Estrutura do Projeto
plaintext
Copiar código
.
├── petshop/
│   ├── settings.py      # Configurações do projeto Django
│   ├── urls.py          # Rotas do projeto
│   ├── wsgi.py          # Configuração WSGI para deployment
├── chatbot/             # Aplicação do chatbot
├── products/            # Aplicação para gerenciamento de produtos
├── cart/                # Aplicação para carrinho de compras
├── customers/           # Aplicação para cadastro e gerenciamento de clientes
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos (CSS, JS, imagens)
├── manage.py            # Comando de gerenciamento do Django
├── requirements.txt     # Dependências do projeto

## 🐕 Futuras Melhorias
Integração com gateways de pagamento, como Stripe ou PayPal.
Implementação de um sistema de assinaturas para rações e outros consumíveis.
Funcionalidade de upload de informações do pet (idade, peso, alergias) para sugestões mais precisas.
Suporte a promoções sazonais, como "Black Friday para Pets".

## 🙌 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias.
