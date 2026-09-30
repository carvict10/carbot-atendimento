# DEMO 01 — Bot de Atendimento

Bot de demonstração para portfólio de criação de bots/chatbots.

## Funcionalidades

- Menu com botões
- Apresentação de serviços
- FAQ
- Área de contato
- Falar com atendente
- Botão de voltar ao menu
- Resposta para mensagens não reconhecidas

## 1. Criar o bot no Telegram

No Telegram, abra o **@BotFather**, crie um bot com `/newbot` e copie o token fornecido.

Nunca publique esse token no GitHub ou envie para clientes.

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 3. Configurar

Forma rápida:

- abra `bot.py`
- defina `BOT_TOKEN` com o token do BotFather
- altere `ADMIN_USERNAME` para seu usuário do Telegram

Ou use variáveis de ambiente:

```text
BOT_TOKEN=seu_token
ADMIN_USERNAME=seu_usuario
```

## 4. Executar

```bash
python bot.py
```

## Observação

Esta é uma DEMO de portfólio. Antes de vender uma versão para um cliente, confirme os requisitos, as integrações necessárias e as regras da plataforma escolhida.
