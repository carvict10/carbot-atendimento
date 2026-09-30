import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# =========================
# CONFIGURAÇÃO
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN", "COLOQUE_SEU_TOKEN_AQUI")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "seu_usuario")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 Serviços", callback_data="services")],
        [InlineKeyboardButton("❓ Perguntas frequentes", callback_data="faq")],
        [InlineKeyboardButton("💬 Falar com atendente", callback_data="support")],
        [InlineKeyboardButton("📞 Contato", callback_data="contact")],
        [InlineKeyboardButton("ℹ️ Sobre", callback_data="about")],
    ])


def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="menu")]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "cliente"

    text = (
        f"👋 Olá, {name}!\n\n"
        "🤖 *Bem-vindo ao nosso atendimento!*\n"
        "Estou aqui para apresentar nossos serviços e ajudar você "
        "a encontrar a solução certa para o seu projeto.\n\n"
        "Escolha uma opção abaixo:"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "menu":
        text = (
            "🤖 *Menu principal*\n\n"
            "Escolha uma opção:"
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

    elif data == "services":
        text = (
            "📋 *Nossos serviços*\n\n"
            "• 🤖 Criação de bots e chatbots\n"
            "• ⚙️ Automações de tarefas\n"
            "• 🔗 Integração com APIs\n"
            "• 💾 Banco de dados\n"
            "• 🧠 Integração com IA\n"
            "• 🎫 Sistemas de atendimento e tickets\n"
            "• 🛠️ Correção e melhoria de projetos existentes\n\n"
            "Cada projeto pode ser personalizado de acordo com "
            "as necessidades do cliente."
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=back_button(),
        )

    elif data == "faq":
        text = (
            "❓ *Perguntas frequentes*\n\n"
            "*Quanto custa?*\n"
            "O valor depende das funcionalidades. Projetos simples "
            "podem começar a partir de R$100.\n\n"
            "*Quanto tempo demora?*\n"
            "O prazo é definido de acordo com o tamanho do projeto.\n\n"
            "*Posso pedir uma função personalizada?*\n"
            "Sim! As funcionalidades são definidas antes do desenvolvimento.\n\n"
            "*Vocês trabalham com APIs?*\n"
            "Sim, quando a API possui acesso e documentação adequados."
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=back_button(),
        )

    elif data == "support":
        text = (
            "💬 *Falar com atendente*\n\n"
            "Para solicitar um orçamento, envie:\n\n"
            "1. Plataforma desejada\n"
            "2. O que o bot deve fazer\n"
            "3. Funcionalidades principais\n"
            "4. APIs ou sistemas que precisam ser integrados\n"
            "5. Se já possui algum código\n\n"
            f"👤 Atendente: @{ADMIN_USERNAME}\n\n"
            "⚠️ Não envie senhas, tokens ou outras informações "
            "confidenciais nesta conversa."
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=back_button(),
        )

    elif data == "contact":
        text = (
            "📞 *Contato*\n\n"
            f"👤 Telegram: @{ADMIN_USERNAME}\n"
            "🌐 Serviço: criação de bots, chatbots e automações\n"
            "💻 Desenvolvimento: Python, APIs e bancos de dados\n\n"
            "Entre em contato para explicar sua ideia."
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=back_button(),
        )

    elif data == "about":
        text = (
            "ℹ️ *Sobre o projeto*\n\n"
            "Este bot é uma demonstração de um sistema de "
            "atendimento automatizado.\n\n"
            "Ele pode ser personalizado com novas funções, "
            "integrações, banco de dados, IA e painéis administrativos."
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=back_button(),
        )


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Não entendi sua mensagem.\n\n"
        "Use /start para abrir o menu principal."
    )


def run():
    if BOT_TOKEN == "COLOQUE_SEU_TOKEN_AQUI":
        raise RuntimeError(
            "Configure a variável BOT_TOKEN antes de iniciar o bot."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))
    app.add_handler(
        # Mensagens de texto que não sejam comandos.
        # O filtro é aplicado diretamente no handler.
        __import__("telegram.ext", fromlist=["MessageHandler"]).MessageHandler(
            __import__("telegram.ext", fromlist=["filters"]).filters.TEXT
            & ~__import__("telegram.ext", fromlist=["filters"]).filters.COMMAND,
            unknown_message,
        )
    )

    logger.info("Bot iniciado.")
    app.run_polling()


if __name__ == "__main__":
    run()
