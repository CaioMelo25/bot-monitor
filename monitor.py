import asyncio
from telethon import TelegramClient, events

import config
import database

async def new_message_handler(event, bot_client):
    """Este é o coração do monitor. Ele é acionado para CADA nova mensagem."""
    try:
        mensagem_texto = event.message.message.lower()
        chat = await event.get_chat()
        channel_username = getattr(chat, 'username', None)

        if not channel_username:
            return

        todos_alertas = database.obter_todos_alertas()

        for alerta in todos_alertas:
            if channel_username.lower() in alerta['channel'].lower():
                if alerta['keyword'].lower() in mensagem_texto:
                    
                    print(f"✅ ALERTA! Palavra '{alerta['keyword']}' encontrada no canal '@{channel_username}' para o usuário {alerta['user_id']}")
                    
                    mensagem_notificacao = (
                        f"🔔 **Alerta de Palavra-chave!**\n\n"
                        f"A palavra **'{alerta['keyword']}'** foi encontrada no canal `@{channel_username}`.\n\n"
                        f"🔗 [Clique aqui para ver a mensagem original](https://t.me/{channel_username}/{event.message.id})"
                    )

                    await bot_client.send_message(
                        alerta['user_id'],
                        mensagem_notificacao,
                        parse_mode='md'
                    )

    except Exception as e:
        print(f"❌ Erro no handler: {e}")

async def main():
    """Função principal que gerencia os clientes e o loop de eventos."""
    
    bot_client = TelegramClient(
        'bot_session',
        config.API_ID,
        config.API_HASH
    )

    user_client = TelegramClient(
        'user_session',
        config.API_ID,
        config.API_HASH
    )


    async with bot_client, user_client:
        print("✅ Clientes conectados. Monitor iniciado. Aguardando mensagens...")

        user_client.add_event_handler(lambda event: new_message_handler(event, bot_client), events.NewMessage())
        
        await user_client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())