import cx_Oracle
from user_data import user_,pass_

host_ = 'oracle.fiap.com.br'
port_ = '1521'
SID_ = 'orcl'

def CRUD_Connect(user_ID, user_pass, host=host_, port=port_, SID=SID_, only_test=False):
    try:
        cx_Oracle.init_oracle_client(lib_dir= r"C:\instantclient-basic-windows.x64-23.5.0.24.07\instantclient_23_5")
    except Exception as e:
        print("Erro na inicialização do 'client': ", e)
    else:
        print('Inicializado com sucesso!!!\n')

    # Conecta o servidor
    dsn_string = cx_Oracle.makedsn(host, port, SID)

    try:
        print("Fazendo conexão com o banco...\n")
        # Efetua a conexão com o Usuário
        connection = cx_Oracle.connect(
            #COMPLETE ESTA PARTE DE CRIAÇÃO DA CONEXÃO ...
            ..., 
            ...,
            ...,
            ...
            #FIM
            )

    except Exception as e:
    # Informa o erro
        print("Erro: ", e)
        # Flag para não executar a Aplicação
        conection_flag = False

    else:
        # Flag para executar a Aplicação
        conection_flag = True

        try:
            # Cria as instruções para cada módulo
            print("Criando cursores...\n")
            #COMPLETE ESTA PARTE DE CRIAÇÃO DOS CURSORES PARA USO NO CRUD
            '''
            ...  = connection...
            ...  = connection...
            ...  = connection...
            ...  = connection...
            '''
            #FIM
            

        except Exception as err:
            print(f'Houve  uma falha na conexao {err}!\n')
            print('Não foi possível criar os cursores do BD!')
            return False, False, False, False, False, conection_flag
        
        else:
            print('Conectado com sucesso!!!')
            if only_test:
                connection.close()
                print('A Conexão apenas para teste foi encerrada com sucesso encerrada! ')
            
            #COMPLETE AQUI COM O RETORNO DOS CURSORES< DA CONEXÃO E DO FLAG DE CONEXÃO
            #return ..., ..., ..., ..., ..., ...
            
    
'''Quando for testar é so completar o código e mandar executar!''' 


if __name__ == "__main__":

    lista = CRUD_Connect(user_, pass_, host=host_, port=port_, SID=SID_, only_test=True)

    print(f'A conexão é {lista[-1]}')
    print(lista[0])
