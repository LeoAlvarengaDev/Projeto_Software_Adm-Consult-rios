import sqlite3
from pathlib import Path
import unittest

# Caminho para o arquivo de banco de dados
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.consulta'
DB_FILE = ROOT_DIR / DB_NAME
inicio = 0

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
class TestMathUtils(unittest.TestCase):
        # Função para cadastrar um cliente
        def cadastrarCliente(nome, data, telefonePrincipal, email, telefoneSecundario):
            try:
                cursor.execute('''
                    INSERT INTO Clientes(Nome, DataDeNascimento, TelefonePrincipal, Email, TelefoneSecundario)
                    VALUES (?, ?, ?, ?, ?);
                ''', (nome, data, telefonePrincipal, email, telefoneSecundario))
                conn.commit()
                print('O Cliente foi cadastrado com sucesso.')
            except Exception as e:
                print('Erro ao cadastrar o Cliente ',e)

        # Função para cadastrar um endereço associado a um cliente
        def cadastrarEndereco(numero, rua, cidade, cep, bairro, uf):
            try:
                cursor.execute('''
                    INSERT INTO Endereco (Numero, Rua, Cidade, Cep, Bairro, UF, clientes_idclientes)
                    VALUES (?, ?, ?, ?, ?, ?, last_insert_rowid());
                ''', (numero, rua, cidade, cep, bairro, uf))
                conn.commit()
                print('O Endereco foi cadastrado com sucesso.')
            except Exception as e:
                print('Erro ao cadastrar o Endereco ',e)

        # Função para cadastrar um alimento associado a um cliente
        def cadastraAlimento(nome,caloria,grupo):
            try:
                # Executa uma instrução SQL para inserir um novo alimento na tabela Alimentos.
                cursor.execute('''
                                INSERT INTO Alimentos (nomeAlimento, cargaCaloria, Grupo_idGrupo)
                                VALUES (?,?,?);
                            ''', (nome, caloria, grupo))
                
                # Realiza a confirmação das alterações no banco de dados.
                conn.commit()
                
                # Informa o usuário que o alimento foi cadastrado com sucesso.
                print('O alimento foi cadastrado com sucesso.')
            except Exception as e:
                print('Erro ao cadastrar o alimento',e)

        # Função para cadastrar uma Dieta associado a um cliente
        def cadastrarDieta(grupo_alimentar1,grupo_alimentar2,grupo_alimentar3,metacalorica,cardapio,idClinte):
            try:
                cursor.execute('''
                                INSERT INTO Dieta(  Grupo_Alimentar1_idGrupo,
                                                    Grupo_Alimentar2_idGrupo,
                                                    Grupo_Alimentar3_idGrupo,
                                                    Clientes_idClientes,
                                                    MetaCalorias,
                                                    Cardapio)
                                VALUES (?,?,?,?,?,?)
                            ''',(grupo_alimentar1,grupo_alimentar2,grupo_alimentar3,idClinte,metacalorica,cardapio))
                # Realiza a confirmação das alterações no banco de dados.
                conn.commit()
                
                print('A Dieta foi cadastrado com sucesso.')
            except Exception as e:
                print('Erro ao cadastrar a Dieta ',e)   

        # Função para atualizar todos dados do cliente
        def atualizarTodosDados(novoNome, novoEmail, novoTelPrin, novoTelSecun, idCliente):
            try:
                cursor.execute('''
                    UPDATE Clientes
                    SET Nome = ?, Email = ?, TelefonePrincipal = ?, TelefoneSecundario = ?
                    WHERE idclientes = ?;
                ''', (novoNome, novoEmail, novoTelPrin, novoTelSecun, idCliente))
                conn.commit()
            except Exception as e:
                print('Erro ao atualizar dados: ',e)

        # Função para atualizar um dado do cliente
        def atualizarDadosCliente(colunaBanco,novoDado, idCliente):
            try:
                cursor.execute('''
                        UPDATE Clientes
                        SET {colunaBanco} = ?
                        WHERE idclientes = ?;
                    ''', (colunaBanco,novoDado,idCliente))
                conn.commit()
            except Exception as e:
                print('Erro ao atualizar dados: ',e)
                

        # Função para atualizar os dados da Dieta
        def atualizarDadosDieta(novoGrupo_alimentar1,novoGrupo_alimentar2,novoGrupo_alimentar3,novaMetacalorica,novoCardapio,idClinte):
            try:
                cursor.execute('''
                        UPDATE Dieta
                        SET grupo_alimentar1_idgrupo = ?,
                        grupo_alimentar2_idgrupo = ?,
                        grupo_alimentar3_idgrupo = ?,                            
                        metacalorias = ?,
                        Cardapio = ?
                        WHERE clientes_idclientes = ?;
                    ''',(novoGrupo_alimentar1,novoGrupo_alimentar2,novoGrupo_alimentar3,novaMetacalorica,novoCardapio,idClinte))    
                conn.commit()
            except Exception as e:
                print('')    

        # Função para atualizar dados do endereço do cliente
        def atualizarEndereco(bairro, numero, cep, cidade, rua, uf, idCliente):
            try:
                cursor.execute('''
                    UPDATE Endereco
                    SET bairro = ?, numero = ?, cep = ?, Cidade = ?, Rua = ?, UF = ?
                    WHERE idendereco IN (SELECT idclientes FROM Clientes WHERE idclientes = ?);
                ''', (bairro, numero, cep, cidade, rua, uf, idCliente))
                conn.commit()
            except Exception as e:
                print('Erro ao atualizar dados: ',e)

        # Esta função que exibe as informações de consulta relacionadas a esse cliente.
        def checarConsultas(idCliente):
            try:
                # Executa uma consulta SQL para buscar as informações de consulta para o cliente.
                cursor.execute('''
                        SELECT dataconsulta, horario, peso, gorduracorporal, sensacaofisica, restricaoalimentar
                        FROM Consultas C
                        LEFT JOIN Clientes cl ON C.idconsultas = CL.idClientes
                        WHERE idclientes = ?;
                        ''', (idCliente,))
                
                # Exibe as informações de consulta encontradas.
                for rows in cursor.fetchall():
                    print(rows)
            
            except Exception:
                # Em caso de erro, imprime uma mensagem de erro.
                print('Erro ao checar consultas:',Exception)
                
        # Esta função que exibe as informações da dieta relacionadas a esse cliente.
        def checarDieta(idCliente):
            try:
                # Executa uma consulta SQL para buscar as informações da dieta para o cliente.
                cursor.execute('''                       
                                SELECT GROUP_CONCAT(Ga.nomegrupo) AS grupos,MetaCalorias,Cardapio
                                FROM Dieta d
                                LEFT JOIN Grupos_Alimentares Ga ON d.grupo_alimentar1_idgrupo = Ga.idGrupo
                                                                OR d.grupo_alimentar2_idgrupo = Ga.idGrupo
                                                                OR d.grupo_alimentar3_idgrupo = Ga.idGrupo
                                WHERE clientes_idclientes = ?
                                ''',(idCliente,))
                
                # Exibe as informações da dieta encontradas.
                for rows in cursor.fetchall():
                    print(rows)
            
            except Exception:
                # Em caso de erro, imprime uma mensagem de erro.
                print('Erro ao checar a dieta:',Exception)

        def checarCliente():
            try:
                cursor.execute('''
                            SELECT * FROM Clientes
                            ''')
                
                for rows in cursor.fetchall():
                    print(rows)
                
                
            except Exception as e:
                # Em caso de erro, imprime uma mensagem de erro.
                print('Erro ao checar Clientes:',Exception)       
        # Função para realizar uma consulta e inserir os dados
        def consulta(idCliente, dataConsulta, horario, peso, gorduraCorporal, sensacaoFisica, restricaoAlimentar=None):
            try:
                cursor.execute('''
                    INSERT INTO Consultas (Clientes_idClientes, DataConsulta, Horario, Peso, GorduraCorporal, SensacaoFisica, RestricaoAlimentar)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                ''', (idCliente, dataConsulta, horario, peso, gorduraCorporal, sensacaoFisica, restricaoAlimentar))
                conn.commit()
                
            except Exception as e:
                print('Erro ao armazenar dados da consulta: ',e)

        # Função para buscar o ID do cliente pelo nome
        def buscaNomeId(nomeCliente):
            try:
                cursor.execute(
                    'SELECT * FROM Clientes WHERE Nome = ?;', (nomeCliente.upper(),)
                )
                resultado = cursor.fetchall()

                if len(resultado) == 1:
                    idCliente = resultado[0][0]
                elif len(resultado) > 1:
                    for row in resultado:
                        print(row)
                    idCliente = int(input('Informe o ID do cliente que será consultado:'))
                    
                return idCliente
            except Exception as e:
                print(f'O cliente {nomeCliente} nao possui cadastro {e}')
                return 0

        # Função para gerar as combinações dos alimentos
        def combinacaoAlimentos(refeicoes_Grupo1, refeicoes_Grupo2, refeicoes_Grupo3, grupo_alimentar1, grupo_alimentar2, grupo_alimentar3, metaCalorica):
            try:
                # Executa uma consulta SQL para calcular combinações de alimentos possíveis.
                cursor.execute('''
                                WITH Combinacoes AS (
                                    SELECT
                                        a1.nomeAlimento AS alimentoGrupo1,
                                        a2.nomeAlimento AS alimentoGrupo2,
                                        a3.nomeAlimento AS alimentoGrupo3,
                                        a1.cargaCaloria * ? + a2.cargaCaloria * ? + a3.cargaCaloria * ? AS totalCalorias
                                    FROM Alimentos AS a1
                                    CROSS JOIN Alimentos AS a2
                                    CROSS JOIN Alimentos AS a3
                                    WHERE a1.Grupo_idGrupo = ?
                                        AND a2.Grupo_idGrupo = ?
                                        AND a3.Grupo_idGrupo = ?
                                )
                                SELECT alimentoGrupo1, alimentoGrupo2, alimentoGrupo3, totalCalorias
                                FROM Combinacoes
                                WHERE totalCalorias <= ?;
                            ''', (refeicoes_Grupo1,
                                    refeicoes_Grupo2,
                                    refeicoes_Grupo3,
                                    grupo_alimentar1,
                                    grupo_alimentar2,
                                    grupo_alimentar3,
                                    metaCalorica))       
                # Exibe as combinações de alimentos encontradas.
                for rows in cursor.fetchall():
                    print(rows)
            
            except Exception as e:
                # Em caso de erro, imprime uma mensagem de erro.
                print('Erro ao calcular combinações de alimentos: ',e)
        
        # Funcão para buscar se o cliente tem resticoes alimentares
        def restricao(idCliente):          
            try:
                # Executa a consulta com o ID do cliente como parâmetro
                cursor.execute('''
                        SELECT restricaoalimentar 
                        FROM Consultas 
                        WHERE clientes_idclientes = ?;
                        ''',(idCliente,))
                for rows in cursor.fetchall():
                    print(rows)
            except Exception as e:
                # Em caso de erro, é uma boa prática capturar exceções e lidar com elas apropriadamente
                print(f"Erro ao executar a consulta: {str(e)}")
                
            
        while True:
            print('|--------------------------------|\n'
                '| 1  --> Cadastrar Cliente       |\n'
                '| 2  --> Atualizar Dados Cliente |\n'
                '| 3  --> Checar Clientes         |\n'
                '| 4  --> Remover Cliente         |\n'
                '| 5  --> Realizar Consultas      |\n'
                '| 6  --> Checar Consultas        |\n'
                '| 7  --> Cadastrar Alimento      |\n'
                '| 8  --> Cadastrar Dieta         |\n'
                '| 9  --> Atualizar Dieta         |\n'
                '| 10 --> Checar Dieta            |\n'  
                '| 11 --> Finalizar               |\n'
                '|--------------------------------|')
            try:
                opcao = int(input('Insira a opção desejada:'))
            except Exception as e:
                print('Formato de entrada de dados errado',e)
                
            match opcao:
                    # Case 1: Cadastra um novo cliente no banco
                    case 1:
                            # Solicitar o número total de clientes a serem cadastrados
                            totalCadastro = int(input('Informe quantos clientes serão cadastrados:'))

                            # Loop para cadastrar múltiplos clientes
                            for inicio in range(totalCadastro):
                                    # Coletar informações do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    dataNas = input('Informe a data de nascimento (dd-mm-yy): ')
                                    telefonePrin = int(input('Informe o telefone principal: '))

                                    # Verificar se o cliente possui telefone secundário
                                    print('|-----------------------------------|'
                                        '\n| O cliente possui Telefone Secundário   |'
                                        '\n| 1 --> Sim                              |'
                                        '\n| 2 --> Não                              |'
                                        '\n|---------------------------------------|')
                                    resposta = int(input('Insira a opção desejada:'))
                                    
                                    # Inicializar telefone secundário como None
                                    telefoneSecun = None

                                    # Se o cliente possui telefone secundário, coletar essa informação
                                    if resposta == 1:
                                        telefoneSecun = int(input('Informe o telefone secundário: '))
                                    
                                    email = input('Informe o email do cliente: ')
                                    rua = input('Informe a rua:')
                                    cidade = input('Informe a cidade: ')
                                    bairro = input('Informe o bairro: ')
                                    numeroEn = input('Informe o número do endereço: ')
                                    cep = input('Informe o cep: ')
                                    uf = input('Informe a UF: ')

                                    # Chamar funções para cadastrar o cliente e o endereço
                                    cadastrarCliente(nomeCliente.upper(), dataNas, telefonePrin, email, telefoneSecun)
                                    cadastrarEndereco(numeroEn, rua, cidade, cep, bairro, uf)

                                    print('-----------------------------------------------------')
                
                    # Caso 2: Atualizar informações do cliente
                    case 2:
                            # Mostra um menu de opções
                            print('|----------------------------------------|\n'
                                '| 1  --> Atualizar Nome                  |\n'
                                '| 2  --> Atualizar Email                 |\n'
                                '| 3  --> Atualizar Telefone Principal    |\n'
                                '| 4  --> Atualizar Telefone Secundario   |\n'
                                '| 5  --> Atualizar Endereco              |\n'       
                                '| 6 --> Atualizar tudo                   |\n'
                                '|----------------------------------------|\n')
                            
                            # Solicita ao usuário que escolha uma opção
                            opcaoCase2 = int(input('Insira a opção desejada:'))
                        
                            # Utiliza a estrutura de correspondência 'match' para lidar com a opção escolhida
                            match opcaoCase2:
                                case 1:
                                    # Atualizar nome do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    idCliente = buscaNomeId(nomeCliente)

                                    if(idCliente == 0):
                                        break
                                    novoNome = input('Informe o novo nome completo do cliente: ')
                                    
                                    atualizarDadosCliente('Nome',novoNome,idCliente)

                                case 2:
                                    # Atualizar email do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    idCliente = buscaNomeId(nomeCliente)
                                    
                                    if(idCliente == 0):
                                        break
                                    novoEmail = input('Informe o novo email do cliente: ')
                                    
                                    atualizarDadosCliente('Email',novoEmail,idCliente)
                                    
                                case 3:
                                    # Atualizar telefone principal do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    idCliente = buscaNomeId(nomeCliente)

                                    if(idCliente == 0):
                                        break
                                    novoTelPrin = input('Informe o novo Telefone Primário do cliente: ')
                                    
                                    atualizarDadosCliente('TelefonePrincipal',novoTelPrin,idCliente)

                                case 4:
                                    # Atualizar telefone secundário do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    idCliente = buscaNomeId(nomeCliente)
                                    if(idCliente == 0):
                                        break
                                    novoTelSecun = input('Informe o novo Telefone Secundario do cliente: ')
                                    
                                    atualizarDadosCliente('TelefoneSecundario',novoTelSecun,idCliente)

                                case 5:
                                    # Atualizar endereço do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    idCliente = buscaNomeId(nomeCliente)
                                    if(idCliente == 0):
                                        break
                                    # Solicita informações de endereço ao usuário
                                    novarua = input('Informe a rua: ')
                                    novacidade = input('Informe a Cidade: ')
                                    novobairro = input('Informe o bairro: ')
                                    novonumeroEn = int(input('Informe o número do endereço: '))
                                    novocep = input('Informe o CEP: ')
                                    novouf = input('Informe a UF: ')
                                    
                                    # Chama a função para atualizar o endereço
                                    atualizarEndereco(novobairro, novonumeroEn, novocep, novacidade, novarua, novouf, idCliente)

                                case 6:
                                    # Atualizar todas as informações do cliente
                                    nomeCliente = input('Informe o nome completo do cliente: ')
                                    idCliente = buscaNomeId(nomeCliente)
                                    if(idCliente == 0):
                                        break
                                    novoNome = input('Informe o novo nome completo do cliente: ')
                                    novoEmail = input('Informe o novo email do cliente: ')
                                    novoTelPrin = input('Informe o novo Telefone Primário do cliente: ')
                                    novoTelSecun = input('Informe o novo Telefone Secundário do cliente: ')
                                    
                                    # Chama a função para atualizar todas as informações do cliente
                                    atualizarTodosDados(novoNome, novoEmail, novoTelPrin, novoTelSecun, idCliente)
                                    
                                    # Solicita informações de endereço ao usuário
                                    novarua = input('Informe a rua: ')
                                    novacidade = input('Informe a Cidade: ')
                                    novobairro = input('Informe o bairro: ')
                                    novonumeroEn = int(input('Informe o número do endereço: '))
                                    novocep = input('Informe o CEP: ')
                                    novouf = input('Informe a UF: ')
                                    
                                    # Chama a função para atualizar o endereço
                                    atualizarEndereco(novobairro, novonumeroEn, novocep, novacidade, novarua, novouf, idCliente)

                                case _:
                                    # Se a opção escolhida não estiver no intervalo de 1 a 6, exibe uma mensagem de opção inválida
                                    print('Opção inválida')

                    # Exibe os clientes cadastratosc:\Users\leona\Downloads\prova_python.pdf
                    case 3:
                        checarCliente()
                    
                    # Caso 4: Deletar um cliente
                    case 4:
                            # Solicita o nome completo do cliente a ser excluído
                            nomeCliente = input('Informe o nome completo do cliente: ')
                                 
                            # Busca o ID do cliente com base no nome
                            idCliente = buscaNomeId(nomeCliente)
                            if(idCliente == 0):
                                continue  
                            # Executa uma consulta SQL para excluir o cliente com base no ID
                            cursor.execute('''
                                    DELETE FROM Clientes WHERE idclientes = ?;
                                ''', (idCliente,))
                        
                    # Caso 5: Inserir informações de consulta para um cliente
                    case 5:
                            cadastro = int(input('|------------------------------|\n'
                                                '|  O cliente ja possui cadastro|\n'
                                                '|------------------------------|\n'
                                                '| 1 --> Sim                    |\n'
                                                '| 2 --> Nao                    |\n'
                                                '|------------------------------|'))
                            
                            if(cadastro == 2):
                            # Coletar informações do cliente
                                nomeCliente = input('Informe o nome completo do cliente: ')
                                dataNas = input('Informe a data de nascimento (dd-mm-yy): ')
                                telefonePrin = int(input('Informe o telefone principal: '))

                                # Verificar se o cliente possui telefone secundário
                                print('|----------------------------------------|'
                                    '\n| O cliente possui Telefone Secundário   |'
                                    '\n| 1 --> Sim                              |'
                                    '\n| 2 --> Não                              |'
                                    '\n|----------------------------------------|')
                                resposta = int(input('Insira a opção desejada:'))
                                        
                                # Inicializar telefone secundário como None
                                telefoneSecun = None

                                # Se o cliente possui telefone secundário, coletar essa informação
                                if resposta == 1:
                                    telefoneSecun = int(input('Informe o telefone secundário: '))
                                        
                                email = input('Informe o email do cliente: ')
                                rua = input('Informe a rua:')
                                cidade = input('Informe a cidade: ')
                                bairro = input('Informe o bairro: ')
                                numeroEn = int(input('Informe o número do endereço: '))
                                cep = input('Informe o cep: ')
                                uf = input('Informe a UF: ')

                                # Chamar funções para cadastrar o cliente e o endereço
                                cadastrarCliente(nomeCliente.upper(), dataNas, telefonePrin, email, telefoneSecun)
                                cadastrarEndereco(numeroEn, rua, cidade, cep, bairro, uf)

                                print('-----------------------------------------------------')
                            
                            
                            # Solicita o nome completo do cliente
                            nomeCliente = input('Informe o nome completo do cliente: ')

                            # Busca o ID do cliente com base no nome
                            idCliente = buscaNomeId(nomeCliente)
                            
                            if(idCliente == 0):
                                continue 
                             
                            # Solicita informações da consulta
                            dataConsulta = input('Informe a data da consulta (dd-mm-yy): ')
                            horario = input('Informe o horário da consulta (hh-min-seg): ')
                            peso = float(input('Informe o peso do paciente: '))
                            gorduraCorporal = input('Informe a gordura corporal do paciente: ')
                            sensacaoFisica = input('Informe a sensação física do paciente: ')

                            # Solicita ao usuário se deseja inserir restrição alimentar
                            print('|-------------------------------|'
                                '\n| Inserir Restrição Alimentar   |'
                                '\n| 1 --> Sim                     |'
                                '\n| 2 --> Não                     |'
                                '\n|-------------------------------|')
                            resposta = int(input('Insira a opção desejada:'))

                            if resposta == 1:
                                restricaoAlimentar = input('Insira a restrição alimentar: ')
                                # Chama a função de consulta com restrição alimentar
                                consulta(idCliente, dataConsulta, horario, peso, gorduraCorporal, sensacaoFisica, restricaoAlimentar)
                            else:
                                # Chama a função de consulta sem restrição alimentar
                                consulta(idCliente, dataConsulta, horario, peso, gorduraCorporal, sensacaoFisica)

                            # Solicita ao usuário se deseja inserir dieta
                            print('|-------------------------------|'
                                '\n| Inserir Dieta                 |'
                                '\n| 1 --> Sim                     |'
                                '\n| 2 --> Não                     |'
                                '\n|-------------------------------|')
                            resposta = int(input('Insira a opção desejada:'))
                            
                            if(resposta == 2):
                                continue
                            
                            print('|--------------------------------------------|\n'
                                '|            Grupo de Alimentos              |\n'
                                '|--------------------------------------------|\n'
                                '| 1 -->Cereais, pães,raízes e tubérculos     |\n'
                                '| 2 -->Hortaliças                            |\n'
                                '| 3 -->Frutas e sucos de frutas              |\n'
                                '| 4 -->Leites, queijos e iogurtes            |\n'
                                '| 5 -->Carnes e Ovos                         |\n'
                                '| 6 -->Leguminosas                           |\n'
                                '| 7 -->Óleos e gorduras                      |\n'
                                '| 8 -->Açucares,balas,chocolates,salgadinhos |\n'
                                '|--------------------------------------------|\n')
                            
                            grupo_1 = int(input('Informe o 1 Grupo da Dieta: '))
                            grupo_2 = int(input('Informe o 2 Grupo da Dieta: '))
                            grupo_3 = int(input('Informe o 3 Grupo da Dieta: '))
                            
                            metaCalorica = int(input('Informe a meta calorica: '))
                            
                            refeicoes_Grupo1 = int(input('Informe quantas refeicoes '
                                                        'deveram ser feitas com base ' 
                                                        'nos alimentos do primeiro grupo informado: '))
                            
                            refeicoes_Grupo2 = int(input('Informe quantas refeicoes '
                                                        'deveram ser feitas com base ' 
                                                        'nos alimentos do segundo grupo informado: '))
                            
                            refeicoes_Grupo3 = int(input('Informe quantas refeicoes '
                                                        'deveram ser feitas com base ' 
                                                        'nos alimentos do terceiro grupo informado: '))
                            
                            combinacaoAlimentos(refeicoes_Grupo1,refeicoes_Grupo2,refeicoes_Grupo3,
                                                grupo_1,grupo_2,grupo_3,metaCalorica)
                            
                            cardapio = input('Informe o cardapio do paciente: ')
                            
                            cadastrarDieta(grupo_1,grupo_2,grupo_3,metaCalorica,cardapio,idCliente)

                    # Caso 6: Consultar informações de consulta para um cliente
                    case 6:
                            # Solicita o nome completo do cliente
                            nomeCliente = input('Informe o nome completo do cliente: ')

                            # Busca o ID do cliente com base no nome
                            idCliente = buscaNomeId(nomeCliente) 
                            
                            if(idCliente == 0):
                                continue  
                            checarConsultas(idCliente)
                            
                    # Caso 7: Cadastrar Alimento 
                    case 7:
                            print('|--------------------------------------------|\n'
                                '|            Grupo de Alimentos              |\n'
                                '|--------------------------------------------|\n'
                                '| 1 -->Cereais, pães,raízes e tubérculos     |\n'
                                '| 2 -->Hortaliças                            |\n'
                                '| 3 -->Frutas e sucos de frutas              |\n'
                                '| 4 -->Leites, queijos e iogurtes            |\n'
                                '| 5 -->Carnes e Ovos                         |\n'
                                '| 6 -->Leguminosas                           |\n'
                                '| 7 -->Óleos e gorduras                      |\n'
                                '| 8 -->Açucares,balas,chocolates,salgadinhos |\n'
                                '|--------------------------------------------|\n')
                            grupo = int(input('Informe o Grupo do alimeno: '))
                            nomeAli = input('Informe o nome do Alimento: ')
                            caloriaPor = int(input('Informe a quantidade de calorias por porcao: '))
                        
                            cadastraAlimento(nomeAli,caloriaPor,grupo)
                                
                    # Caso 8: Cadastrar Dietas
                    case 8:
                            # Solicita o nome completo do cliente
                            nomeCliente = input('Informe o nome completo do cliente: ')

                            # Busca o ID do cliente com base no nome
                            idCliente = buscaNomeId(nomeCliente)
                            
                            if(idCliente == 0):
                                continue 

                            # Exibe as restrições alimentares do cliente
                            print('Restrição Alimentar')
                            # Consulta o banco de dados para obter informações sobre as restrições alimentares do cliente
                            restricao(idCliente)
                            
                            # Exibe um menu de grupos alimentares
                            print('|----------------------------------------------|\n'
                                '|            Grupo de Alimentos                  |\n'
                                '|------------------------------------------------|\n'
                                '| 1 --> Cereais, pães, raízes e tubérculos       |\n'
                                '| 2 --> Hortaliças                               |\n'
                                '| 3 --> Frutas e sucos de frutas                 |\n'
                                '| 4 --> Leites, queijos e iogurtes               |\n'
                                '| 5 --> Carnes e Ovos                            |\n'
                                '| 6 --> Leguminosas                              |\n'
                                '| 7 --> Óleos e gorduras                         |\n'
                                '| 8 --> Açúcares, balas, chocolates, salgadinhos |\n'
                                '|------------------------------------------------|\n')

                            # Solicita a seleção dos grupos alimentares e outras informações
                            grupo_1 = int(input('Informe o 1° Grupo da Dieta: '))
                            grupo_2 = int(input('Informe o 2° Grupo da Dieta: '))
                            grupo_3 = int(input('Informe o 3° Grupo da Dieta: '))

                            metaCalorica = int(input('Informe a meta calórica: '))

                            refeicoes_Grupo1 = int(input('Informe quantas refeições devem ser feitas com base nos alimentos do primeiro grupo informado: '))
                            refeicoes_Grupo2 = int(input('Informe quantas refeições devem ser feitas com base nos alimentos do segundo grupo informado: '))
                            refeicoes_Grupo3 = int(input('Informe quantas refeições devem ser feitas com base nos alimentos do terceiro grupo informado: '))

                            # Calcula a combinação de alimentos com base nas informações fornecidas
                            combinacaoAlimentos(refeicoes_Grupo1, refeicoes_Grupo2, refeicoes_Grupo3, grupo_1, grupo_2, grupo_3, metaCalorica)

                            # Solicita o cardápio ao usuário
                            cardapio = input('Informe o cardápio do paciente: ')

                            # Cadastra a dieta no banco de dados com base nas informações fornecidas
                            cadastrarDieta(grupo_1, grupo_2, grupo_3, metaCalorica, cardapio, idCliente)

                    # Atualiza os dados da Dieta
                    case 9:
                        # Solicita o nome completo do cliente
                            nomeCliente = input('Informe o nome completo do cliente: ')

                            # Busca o ID do cliente com base no nome
                            idCliente = buscaNomeId(nomeCliente)
                            
                            if(idCliente == 0):
                                continue 
                            
                            # Exibe as restrições alimentares do cliente
                            print('Restrição Alimentar')
                            # Consulta o banco de dados para obter informações sobre as restrições alimentares do cliente
                            restricao(idCliente)

                            # Exibe um menu de grupos alimentares
                            print('|--------------------------------------------|\n'
                                '|            Grupo de Alimentos              |\n'
                                '|--------------------------------------------|\n'
                                '| 1 --> Cereais, pães, raízes e tubérculos   |\n'
                                '| 2 --> Hortaliças                          |\n'
                                '| 3 --> Frutas e sucos de frutas            |\n'
                                '| 4 --> Leites, queijos e iogurtes          |\n'
                                '| 5 --> Carnes e Ovos                       |\n'
                                '| 6 --> Leguminosas                         |\n'
                                '| 7 --> Óleos e gorduras                    |\n'
                                '| 8 --> Açúcares, balas, chocolates, salgadinhos |\n'
                                '|--------------------------------------------|\n')

                            # Solicita a seleção dos grupos alimentares e outras informações
                            novoGrupo_1 = int(input('Informe o novo 1° Grupo da Dieta: '))
                            novoGrupo_2 = int(input('Informe o novo 2° Grupo da Dieta: '))
                            novoGrupo_3 = int(input('Informe o novo 3° Grupo da Dieta: '))

                            novaMetaCalorica = int(input('Informe a nova meta calórica: '))

                            refeicoes_Grupo1 = int(input('Informe quantas refeições devem ser feitas com base nos alimentos do primeiro grupo informado: '))
                            refeicoes_Grupo2 = int(input('Informe quantas refeições devem ser feitas com base nos alimentos do segundo grupo informado: '))
                            refeicoes_Grupo3 = int(input('Informe quantas refeições devem ser feitas com base nos alimentos do terceiro grupo informado: '))

                            # Calcula a combinação de alimentos com base nas informações fornecidas
                            combinacaoAlimentos(refeicoes_Grupo1, refeicoes_Grupo2, refeicoes_Grupo3, novoGrupo_1, novoGrupo_2, novoGrupo_3, novaMetaCalorica)

                            # Solicita o cardápio ao usuário
                            novoCardapio = input('Informe o novo cardápio do paciente: ')

                            # Atualiza a dieta no banco de dados com base nas informações fornecidas
                            atualizarDadosDieta(novoGrupo_1, novoGrupo_2, novoGrupo_3, novaMetaCalorica, novoCardapio, idCliente)
                        
                    # Caso 10: Checar Dietas cadastradas
                    case 10:
                            # Solicita o nome completo do cliente
                            nomeCliente = input('Informe o nome completo do cliente: ')

                            # Busca o ID do cliente com base no nome
                            idCliente = buscaNomeId(nomeCliente)
                            
                            if(idCliente == 0):
                                continue 
                            
                            # Chama a função para checar a dieta do cliente com base no ID
                            checarDieta(idCliente)
                            
                    # Caso 10: Finaliza o sistema
                    case 11:
                            print('Sistema Finalizado')
                            break
                        
                    # Caso padrão: Opção inválida           
                    case _:
                            print('Opção inválida')

        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()   
        
if __name__ == '__main__':
    unittest.main()
