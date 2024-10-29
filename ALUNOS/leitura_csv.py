import csv


def leitura_csv(caminho:str) -> list:
    '''Função para executar a leitura de dados em CSV, 
    convertendo em lista para uso no tratamento'''
    leitura = False
    try:
        #PARA LER EXECUTE COM WITH E OPEN, LEMBRANDO DE USAR LEITURA ('r') e USAR O ENCODING PARA 'utf-8'
            #CRIE UMA VARIÁVEL DE lEITURA COM 'csv.reader' E DELIMITADOR ',' (NÃO USE ';')
            #USE UMA LISTA VAZIA PARA POVOAR COM AS LINHAS DE READER (list(row))
        #with...


    except FileNotFoundError:
        print('Arquivo inexistente!\n')
    except Exception as err:
        print(f'Erro na leitura: {err}\n')
    else:
        leitura = True

    if leitura:

        chaves_registro = registro_compra[0]
        lista_registro = []

        #COMPLETE AQUI COM LAÇOS ANINHADOS, OU O QUE ACHAR MELHOR
        #ESTA VARREDURA DEVE SER EXECUTADA NO 'registro_compra',
        #LEMBRADO QUE AO LER UM CVS TEMOS UMA LISTA PARA CADA LINHA DA TABELA
        #E QUE A PRIMEIRA LINHA É DO CABEÇALHO< E NÃO NOS INTERESSA

        
      
        return [chaves_registro,lista_registro]
    else:
        return []


#CUIDADO DAQUI PARA BAIXO - NÃO ALTERAR ESTA PARTE - SERVE PARA TESTE!


if __name__ == '__main__':
    
    import os

    os.system('cls')
    lista_out = leitura_csv('compras.csv')
    print('\n ------------Verificando a leitura do CSV------------')
    print('\n ----------------Nomes das colunas:------------------')
    print(lista_out[0])
    print('\n ----------------Dados das colunas:------------------')
    for linha in lista_out[1]:
        print(linha)
