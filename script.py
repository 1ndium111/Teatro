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

try:
    conn = psycopg.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS assentos_sala1 (
        id SERIAL PRIMARY KEY,
        fila CHAR(1) NOT NULL,
        numero_cadeira INT NOT NULL,
        ocupado BOOLEAN DEFAULT FALSE NOT NULL
        );
    """)

    query_insert = "INSERT INTO assentos_sala1 (fila, numero_cadeira, ocupado) VALUES (%s, %s, %s);"

    dados_assentos = []

    for fila in filas:
        for cadeira in cadeiras:
            dados_assentos.append([fila, cadeira, False])

    cur.executemany(query_insert, dados_assentos)

    conn.commit()
    print(f"Sucesso! {len(dados_assentos)} assentos foram cadastrados.")

    cur.execute("""
            CREATE TABLE IF NOT EXISTS assentos_sala2 (
            id SERIAL PRIMARY KEY,
            fila CHAR(1) NOT NULL,
            numero_cadeira INT NOT NULL,
            ocupado BOOLEAN DEFAULT FALSE NOT NULL
            );
        """)
    
    query_insert = "INSERT INTO assentos_sala2 (fila, numero_cadeira, ocupado) VALUES (%s, %s, %s);"
    
    dados_assentos = []
    
    for fila in filas:
            for cadeira in cadeiras:
                dados_assentos.append([fila, cadeira, False])
    
    cur.executemany(query_insert, dados_assentos)
    
    conn.commit()
    print(f"Sucesso! {len(dados_assentos)} assentos foram cadastrados.")

    cur.execute("""
                CREATE TABLE IF NOT EXISTS assentos_sala3 (
                id SERIAL PRIMARY KEY,
                fila CHAR(1) NOT NULL,
                numero_cadeira INT NOT NULL,
                ocupado BOOLEAN DEFAULT FALSE NOT NULL
                );
            """)
        
    query_insert = "INSERT INTO assentos_sala3 (fila, numero_cadeira, ocupado) VALUES (%s, %s, %s);"
        
    dados_assentos = []
        
    for fila in filas:
                for cadeira in cadeiras:
                    dados_assentos.append([fila, cadeira, False])
        
    cur.executemany(query_insert, dados_assentos)
        
    conn.commit()
    print(f"Sucesso! {len(dados_assentos)} assentos foram cadastrados.")

except Exception as error:
    print(f"Erro ao conectar ou operar no banco: {error}")
    conn.rollback()

finally:
    cur.close()
    conn.close()
