from leitura_csv import leitura_csv
from leitura_json import leitura_json
from user_data import user_,pass_
from conexao_BD_Oracle import CRUD_Connect


instrucao_GRAVA,_,_,_,connection,flag_conection = CRUD_Connect(user_,pass_)


if flag_conection:
    arquivo_csv = leitura_csv('compras.csv')
    arquivo_json = leitura_json('compras_novos.json')

    #Começando pelo csv
    try:
        print("\nPraparando para Gravação de dados do arquivo CSV...")

        #COMPLETE AQUI CRIANDO UM LAÇO PARA PERCORRER A LISTA DE VALORES NO arquivo_csv
        #for ...

            cadastro = f'''INSERT INTO produtos_padaria (
            id_compra,
            pao_frances,
            bolo_milho,
            bolo_fuba,
            pao_queijo,
            leite,
            manteiga,
            margarina,
            agua,
            refrigerante) VALUES ('{linha[0]}',
            '{linha[1]}',
            '{linha[2]}',
            '{linha[3]}',
            '{linha[4]}',
            '{linha[5]}',
            '{linha[6]}',
            '{linha[7]}',
            '{linha[8]}',
            '{linha[9]}')'''

            #COMPLETE AQUI COM AS INSTRUÇÔES DE EXECUÇÂO E E COMMIT
            ...
            ...

    except ValueError:
        print("Algum valor incorreto!")

    except Exception as err:
        print(f"Erro na transação do BD. Err:{err}")

    else:
        print("\nDados do arquivo CSV GRAVADOS com sucesso no Banco de Dados")
        input("Pressione ENTER para continuar ...")



    #Agora gravando JSON
    try:
        print("\nPraparando para Gravação de dados do arquivo JSON...")
        #COMPLETE AQUI CRIANDO UM LAÇO PARA PERCORRER A LISTA DE VALORES NO arquivo_json
        #for ...

            cadastro = f'''INSERT INTO produtos_padaria (
            id_compra,
            pao_frances,
            bolo_milho,
            bolo_fuba,
            pao_queijo,
            leite,
            manteiga,
            margarina,
            agua,
            refrigerante) VALUES ('{linha_j[0]}',
            '{linha_j[1]}',
            '{linha_j[2]}',
            '{linha_j[3]}',
            '{linha_j[4]}',
            '{linha_j[5]}',
            '{linha_j[6]}',
            '{linha_j[7]}',
            '{linha_j[8]}',
            '{linha_j[9]}')'''

            #COMPLETE AQUI COM AS INSTRUÇÔES DE EXECUÇÂO E E COMMIT
            ...
            ...

    except ValueError:
        print("Algum valor incorreto!")

    except Exception as err:
        print(f"Erro na transação do BD. Err:{err}")

    else:
        print("\nDados do arquivo JSON GRAVADOS com sucesso no Banco de Dados")
        input("Pressione ENTER para continuar ...")

connection.close()
print("\nFim da recuperação de Dados!!!")
