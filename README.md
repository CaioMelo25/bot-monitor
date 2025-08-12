# Monitor de Palavras-Chave para Telegram

Este é um bot para o Telegram desenvolvido em Python, projetado para monitorar canais públicos em busca de palavras-chave específicas. Quando uma palavra-chave cadastrada é encontrada em uma mensagem de um canal monitorado, o bot envia uma notificação instantânea para o usuário no chat privado.

Este projeto foi desenvolvido como um estudo prático de programação assíncrona, APIs e gerenciamento de banco de dados.

## Principais Funcionalidades

* Monitoramento de múltiplos canais e múltiplas palavras-chave.
* Notificações em tempo real com link direto para a mensagem original.
* Arquitetura de dois processos: um para interação com o usuário e outro para o monitoramento.
* Armazenamento persistente de alertas usando SQLite.
* Configuração segura com separação de chaves e credenciais.

## Tecnologias Utilizadas

* **Python 3.13**
* **python-telegram-bot**: Para a interface com o usuário (recebimento de comandos).
* **Telethon**: Para o monitoramento dos canais, utilizando o protocolo MTProto para leitura de mensagens em tempo real.
* **SQLite3**: Para o banco de dados local que armazena os alertas.
* **asyncio**: Para gerenciar as operações assíncronas do monitor.

## Como Usar

Os seguintes comandos estão disponíveis no chat com o bot:

* `/start` - Inicia a conversa e exibe a mensagem de boas-vindas.
* `/monitorar <palavra_chave> <link_do_canal>` - Cadastra um novo alerta para ser monitorado.
    * *Exemplo: `/monitorar whey https://t.me/canaldealertas`*

## Configuração do Ambiente Local

Para executar este projeto localmente:

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    ```
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Crie o arquivo `config.py` na raiz do projeto e adicione suas chaves da API do Telegram (`BOT_TOKEN`, `API_ID`, `API_HASH`).
5.  Execute os dois processos principais em terminais separados:
    ```bash
    # No terminal 1
    python bot.py
    
    # No terminal 2
    python monitor.py
    ```
