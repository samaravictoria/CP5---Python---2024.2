from user_data import user_,pass_
import os
import pandas as pd
from conexao_BD_Oracle import CRUD_Connect

#Aqui fazemos a conexão!!
inst_cadastro,inst_consulta,inst_alteracao,inst_exclusao,connection,flag_conection = CRUD_Connect(user_,pass_)


# Enquanto o flag conexao estiver apontado com True a aplicação é executada
while flag_conection:
    # Limpa a tela via SO
    os.system('cls')
    # Apresenta o menu
    print("---- CRUD - Compras Padaria ----")
    print("""
    1 - Cadastrar Nova Compra
    2 - Listar Compras
    3 - Alterar Compra
    4 - Excluir Compra
    5 - EXCLUIR BANDO DE DADOS
    6 - SAIR
    """)

    try:
        # Captura a escolha do usuário
        escolha = int(input("Escolha -> "))
    except Exception as err:
        print('\n Inserção inválida!! Digite um número entre 1 e 5 ...')
    else:
        print('\nCarregando opções...')

     # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:
        # CADASTRAR
        case 1:
            try:
                print("----- CADASTRAR COMPRA -----\n")

                lista_compras_provisorio = [] #aqui vamos armazenar os dados

                # Executa a leitura da Tabela
                consulta = "SELECT * FROM produtos_padaria"
                inst_consulta.execute(consulta)

                # Aqui coletamos a consulta
                dados = inst_consulta.fetchall()
                for linha in dados:
                    lista_compras_provisorio.append(linha)
                
                novo_ID = len(lista_compras_provisorio)+1
                
                # Recebe os valores para cadastro
                id_compra = novo_ID
                pao_frances = int(input("A quantidade de pães franceses comprados: "))
                bolo_milho = int(input("A quantidade de bolos de milho comprados: "))
                bolo_fuba = int(input("A quantidade de bolos de fubá comprados: "))
                pao_queijo = int(input("A quantidade de pães de queijo comprados: "))
                leite = int(input("A quantidade de leites comprados: "))
                manteiga = int(input("A quantidade de manteigas compradas: "))
                margarina = int(input("A quantidade de margarinas compradas: "))
                agua = int(input("A quantidade de aguas compradas: "))
                refrigerante = int(input("A quantidade de refrigerantes comprados: "))
                
                # Usando f....string {valores} é mais rápido
                #COMPLETE A INSTRUÇÃO ABAIXO PARA INSERIR UM ELEMENTO NO BANCO DE DADOS!
                    
                #cadastro = f'''INSERT INTO produtos_padaria (id_compra, ...) VALUES ('{id_compra}', 
                #...')'''

                # FIM DA STRING DE INCLUSÂO!!


                # Executa e grava o Registro na Tabela
                #COMPLETE AS INSTRUÇÔES ABAIXO PARA EXECUTAR A INSTRUÇÂO E COMMIT
                #....execute(cadastro)
                #....commit()

            except ValueError:
                print("Digite apenas valores numéricos!")

            except Exception as err:
                print(f"Erro na transação do BD. Err:{err}")

            else:
                print("\nDados GRAVADOS")
                input("Pressione ENTER para continuar ...")

        case 2:

            os.system('cls')
            print("----- LISTANDO COMPRAS -----\n")
            lista_compras = [] #aqui vamos armazenar os dados

            # Executa a leitura da Tabela
            #COMPLETE A EXECUÇÂO DO COMANDO DE BUSCA ABAIXO E EXECUTE
            #...
            #....execute(consulta)

            # Aqui coletamos a consulta
            dados = inst_consulta.fetchall()

            for linha in dados:
                lista_compras.append(linha)

            lista_compras = sorted(lista_compras)

            colunas = ['ID_Compra', 'Pão Francês', 'Bolo de Milho', 'Bolo de Fubá', 'Pão de Queijo', 'Leite', 'Manteiga', 'Margarina', 'Água', 'Refrigerante']
            # Aqui o nosso Dataframe!!!!!
            df_compras = pd.DataFrame.from_records(lista_compras, columns=colunas, index='ID_Compra')

            
            print('Listando os compras cadastradas...\n')
            print(df_compras)
            input("\nPressione ENTER para continuar ...")


        case 3:
            os.system('cls')
            print("----- ALTERANDO CADASTRO DE COMPRA JÁ EFETUADA -----\n")

            busca_id = int(input('Digite o Id da COMPRA cujo cadastro quer alterar: '))

            lista_compra = [] #aqui vamos armazenar os dados

            # Executa a leitura da Tabela
            consulta = f"SELECT * FROM produtos_padaria WHERE id_compra = {busca_id}"
            inst_consulta.execute(consulta)
            dado = inst_consulta.fetchall()

            lista_compra.append(dado)

            if len(lista_compra) == 0:
                print(f"Não há COMPRA com o Id informado = {busca_id}")
                _ = input("\nPressione ENTER para continuar ...")
            else:
                # Recebe os NOVOS valores para cadastro
                pao_frances = int(input("A NOVA quantidade de pães franceses comprados: "))
                bolo_milho = int(input("A NOVA quantidade de bolos de milho comprados: "))
                bolo_fuba = int(input("A NOVA quantidade de bolos de fubá comprados: "))
                pao_queijo = int(input("A NOVA quantidade de pães de queijo comprados: "))
                leite = int(input("A NOVA quantidade de leites comprados: "))
                manteiga = int(input("A NOVA quantidade de manteigas compradas: "))
                margarina = int(input("A NOVA quantidade de margarinas compradas: "))
                agua = int(input("A NOVA quantidade de aguas compradas: "))
                refrigerante = int(input("A NOVA quantidade de refrigerantes comprados: "))

                #COMPLETE A INSTRUÇÃO ABAIXO PARA INSERIR UM ELEMENTO NO BANCO DE DADOS!
                    
                #alteracao = f'''UPDATE produtos_padaria SET pao_frances='{pao_frances}',
                #..., ..., .... WHERE ...

                # FIM DA STRING DE ALTERAÇÃO!!


                # Executa e grava o Registro na Tabela
                #COMPLETE AS INSTRUÇÔES ABAIXO PARA EXECUTAR A INSTRUÇÂO E COMMIT
                #....execute(cadastro)
                #....commit()
            
                print('Alteração executada com sucesso...\n')
                input("\nPressione ENTER para continuar ...")


        case 4:

            os.system('cls')
            print("----- APAGANDO CADASTRO DE PET -----\n")

            busca_id = int(input('Digite o Id da COMPRA cujo cadastro quer alterar: '))

            lista_compra = [] #aqui vamos armazenar os dados

            # Executa a leitura da Tabela
            consulta = f"SELECT * FROM produtos_padaria WHERE id_compra = {busca_id}"
            inst_consulta.execute(consulta)
            dado = inst_consulta.fetchall()

            lista_compra.append(dado)

            if len(lista_compra) == 0:
                print(f"Não há COMPRA com o Id informado = {busca_id}")
                _ = input("\nPressione ENTER para continuar ...")

            else:

                exclusao = f"DELETE FROM produtos_padaria WHERE id_compra='{busca_id}'"
                inst_exclusao.execute(exclusao)
                connection.commit()

                print('Exclusão executada com sucesso...\n')
                input("\nPressione ENTER para continuar ...")

        case 5:
            print("\nEXLUIR TODOS OS ELEMENTOS DO BANCO DE DADOS!!!\n")

            ZERA_BANCO = input("CONFIRMA A EXCLUSÃO DOS DADOS: digite 'SIM' para prosseguir...")

            if ZERA_BANCO == 'SIM':
                exclusao_total = "DELETE FROM produtos_padaria"
                inst_exclusao.execute(exclusao_total)
                connection.commit()

                print("\nTodos os dados foram apagador com sucesso!\n")
                input("\nPressione ENTER para continuar ...")

            else:
                print("Operação não concluída! Para apagar execute novamente e siga as instruções!")
                input("\nPressione ENTER para continuar ...")

        case 6:

            print("\n Saindo do programa...\n")
            connection.close()
            flag_conection = False
            print("\nObrigado por usar o nosso BD!!!\n")
        case _:

            print('\nDigite uma opção válida...')
            input("\nPressione ENTER para continuar ...")