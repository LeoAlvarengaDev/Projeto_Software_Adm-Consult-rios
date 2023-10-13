import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.consulta'
DB_FILE = ROOT_DIR / DB_NAME

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        idClientes INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome VARCHAR(255),
        Email VARCHAR(100),
        DataDeNascimento DATE,
        TelefonePrincipal VARCHAR(9),
        TelefoneSecundario VARCHAR(9)
    )
''')

# Tabela Endereco com relação à tabela Clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Endereco (
        idEndereco INTEGER PRIMARY KEY AUTOINCREMENT,
        Clientes_idClientes INTEGER NOT NULL,
        Numero VARCHAR(20),
        Cep VARCHAR(9),
        Bairro VARCHAR(50),
        Cidade VARCHAR(50),
        Rua VARCHAR(50),
        UF CHAR(2),
        FOREIGN KEY(Clientes_idClientes)
            REFERENCES Clientes(idClientes)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
    )
''')

# Índice para a chave estrangeira em Endereco
cursor.execute('''
    CREATE INDEX IF NOT EXISTS Endereco_FKIndex1 ON Endereco (Clientes_idClientes)
''')

# Tabela Consultas com relação à tabela Clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Consultas (
        idConsultas INTEGER PRIMARY KEY AUTOINCREMENT,
        Clientes_idClientes INTEGER NOT NULL,
        DataConsulta DATE,
        Horario DATETIME,
        Peso FLOAT,
        GorduraCorporal FLOAT,
        SensacaoFisica TEXT,
        RestricaoAlimentar TEXT,
        FOREIGN KEY(Clientes_idClientes)
            REFERENCES Clientes(idClientes)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
    )
''')

# Tabela Grupos_Alimentares
cursor.execute('''
     CREATE TABLE IF NOT EXISTS  Grupos_Alimentares (
        idGrupo INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeGrupo VARCHAR(50)
    )
''')

# Tabela Alimentos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alimentos (
        idAlimento INTEGER PRIMARY KEY AUTOINCREMENT,
      	nomeAlimento VARCHAR(100),
      	cargaCaloria INTEGER,
      	Grupo_idGrupo INTEGER,
      FOREIGN KEY(Grupo_idGrupo)
            REFERENCES Grupos_Alimentares(idGrupo)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
    )
''')

# Tabela Combinações_Alimentares
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dieta (
        idDieta INTEGER PRIMARY KEY AUTOINCREMENT,
        Grupo_Alimentar1_idGrupo INTEGER,
        Grupo_Alimentar2_idGrupo INTEGER,
        Grupo_Alimentar3_idGrupo INTEGER,
        Clientes_idClientes INTEGER,
        MetaCalorias INTEGER,
        Cardapio TEXT,
        FOREIGN KEY(Grupo_Alimentar1_idGrupo)
            REFERENCES Grupos_Alimentares(idGrupo)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        FOREIGN KEY(Grupo_Alimentar2_idGrupo)
            REFERENCES Grupos_Alimentares(idGrupo)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        FOREIGN KEY(Grupo_Alimentar3_idGrupo)
            REFERENCES Grupos_Alimentares(idGrupo)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        FOREIGN KEY(Clientes_idClientes)
            REFERENCES Clientes(idClientes)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
    )
''')

cursor.execute('')

cursor.executemany('''
                   INSERT INTO Grupos_Alimentares(nomeGrupo)
                   VALUES (?)
                   ''',(['Cereais, pães,raízes e tubérculos'],
                        ['Hortaliças'],
                        ['Frutas e sucos de frutas'],
                        ['Leites, queijos e iogurtes'],
                        ['Carnes e Ovos'],
                        ['Leguminosas'],
                        ['Óleos e gorduras'],
                        ['Açucares, balas, chocolates, salgadinhos']))


cursor.executemany('''
                   INSERT INTO Alimentos (nomeAlimento,cargaCaloria,Grupo_idGrupo)
                   VALUES (?,?,?)
                   ''',(['Amido de milho',150,1],
                        ['Arroz branco cozido', 150,1],
                        ['Arroz integral cozido', 150,1],
                        ['Batata cozida', 150,1],
                        ['Batata doce cozida', 150,1],
                        ['Biscoito  de leite', 150,1],
                        ['Abobrinha cozida',15,2],
                        ['Acelga cozida',15,2],
                        ['Agrião',15,2],
                        ['Alface americana',15,2],
                        ['Beterraba cozida',15,2],
                        ['Abacate',70,3],
                        ['Abacaxi',70,3],
                        ['Acerola',70,3],
                        ['Caju',70,3],
                        ['Cereja',70,3],
                        ['Feijão branco cozido',55,4],
                        ['Lentilha cozida',55,4],
                        ['Soja cozida',55,4],
                        ['Avelã',55,4],
                        ['Frango assado',190,5],
                        ['Frango filé grelhado',190,5],
                        ['Manjuba frita',190,5],
                        ['Mortadela',190,5],
                        ['Coalhada',120,6],
                        ['Cream cheese',120,6],
                        ['Iogurte integral de frutas',120,6],
                        ['Iogurte integral natural',120,6],
                        ['Azeite de dendê',73,7],
                        ['Azeite de oliva',73,7],
                        ['Creme vegetal',73,7],
                        ['Margarina líquida',73,7],
                        ['Açúcar mascavo fino',110,8],
                        ['Brigadeiro',110,8],
                        ['Bala',110,8],
                        ['Refrigerante',110,8]))

# Commit e feche a conexão
conn.commit()

cursor.close()
conn.close()