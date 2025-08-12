import sqlite3

DB_NAME = "alertas.db"

def inicializar_db():
    """Cria a tabela de alertas no banco de dados se ela não existir."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alertas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        keyword TEXT NOT NULL,
        channel TEXT NOT NULL
    );
    """)
    conexao.commit()
    conexao.close()

def adicionar_alerta(user_id: int, keyword: str, channel: str):
    """Adiciona um novo alerta no banco de dados."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alertas (user_id, keyword, channel) VALUES (?, ?, ?)",
                   (user_id, keyword.lower(), channel))
    conexao.commit()
    conexao.close()
    print(f"Alerta adicionado: User({user_id}), Keyword('{keyword}'), Channel('{channel}')")

def obter_todos_alertas():
    """Retorna uma lista de todos os alertas salvos."""
    conexao = sqlite3.connect(DB_NAME)
    # Usamos Row para acessar os resultados como um dicionário, o que é mais legível
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT user_id, keyword, channel FROM alertas")
    alertas = cursor.fetchall()
    conexao.close()
    return alertas

inicializar_db()