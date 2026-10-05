import psycopg

DB_CONFIG = {
    "dbname": "cinema",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"
}

filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
cadeiras = range(1, 21)

# Geramos a lista de assentos uma única vez
dados_assentos = []
for fila in filas:
    for cadeira in cadeiras:
        dados_assentos.append([fila, cadeira, False])

# Lista com as salas que queremos criar e popular
salas = ["assentos_sala1", "assentos_sala2", "assentos_sala3"]

try:
    # Abrimos uma única conexão para toda a operação
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            
            for nome_tabela in salas:
                # 1. Cria a tabela se não existir
                cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS {nome_tabela} (
                        id SERIAL PRIMARY KEY,
                        fila CHAR(1) NOT NULL,
                        numero_cadeira INT NOT NULL,
                        ocupado BOOLEAN DEFAULT FALSE NOT NULL
                    );
                """)
                
                # Opcional: Limpa a tabela antes de inserir para evitar duplicatas ao reexecutar
                cur.execute(f"TRUNCATE TABLE {nome_tabela} RESTART IDENTITY CASCADE;")

                # 2. Insere os assentos em lote
                query_insert = f"INSERT INTO {nome_tabela} (fila, numero_cadeira, ocupado) VALUES (%s, %s, %s);"
                cur.executemany(query_insert, dados_assentos)
                
                print(f"Sucesso! {len(dados_assentos)} assentos cadastrados na tabela {nome_tabela}.")
            
            # O 'with' gerencia o commit automático em caso de sucesso
            print("Todas as salas foram configuradas com sucesso!")

except Exception as error:
    print(f"Erro ao conectar ou operar no banco: {error}")
