import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import config
import database

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia uma mensagem de boas-vindas quando o comando /start é emitido."""
    user_name = update.message.from_user.first_name
    await update.message.reply_text(
        f"Olá, {user_name}! Eu sou seu bot monitor de promoções.\n\n"
        "Use o comando /monitorar <palavra_chave> <link_do_canal> para criar um alerta.\n\n"
        "Exemplo: `/monitorar whey https://t.me/xetdaspromocoes`"
    )

async def monitorar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Salva um novo alerta solicitado pelo usuário."""
    try:
        partes = update.message.text.split()
        if len(partes) != 3:
            await update.message.reply_text(
                "❌ Formato incorreto!\n"
                "Use: /monitorar <palavra_chave> <link_do_canal>"
            )
            return

        keyword = partes[1]
        channel_link = partes[2]
        user_id = update.message.from_user.id

        database.adicionar_alerta(user_id, keyword, channel_link)

        await update.message.reply_text(
            f"✅ Alerta criado! Vou te notificar quando a palavra '**{keyword}**' aparecer em '{channel_link}'."
        )

    except Exception as e:
        print(f"Erro no comando /monitorar: {e}")
        await update.message.reply_text("Ocorreu um erro ao processar seu pedido. Tente novamente.")


def main():
    """Função principal que inicia o bot."""
    print("Iniciando o bot...")
    
    application = Application.builder().token(config.BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("monitorar", monitorar))

    print("Bot iniciado e aguardando comandos...")
    application.run_polling()


if __name__ == "__main__":
    main()