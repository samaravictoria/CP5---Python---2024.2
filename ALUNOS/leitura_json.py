import json


def leitura_json(caminho:str) -> list:
    '''Função para executar a leitura de dados em JSON, 
    convertendo em lista para uso no tratamento'''
    leitura = False

    try:
        #PARA LER EXECUTE COM WITH E OPEN, LEMBRANDO DE USAR LEITURA ('r') e USAR O ENCODING PARA 'utf-8'
            #CRIE UMA VARIÁVEL DE lEITURA COM 'json.load(arquivo)' 
        #with...

    except FileNotFoundError:
        print('Arquivo inexistente!\n')
    except Exception as err:
        print(f'Erro na leitura: {err}\n')
    else:
        leitura = True

    if leitura:
        chaves_json = list(dicionario_json.keys())
        valores_json = list(dicionario_json.values())

        lista_registro = valores_json.copy()

        # COMPLETE AQUI LEMBRANDO QUE O DICIONÁRIO TEM O ID COMO CHAVE
        # E ESTA CHAVE DEVE SER INCLUÍDA NA PRIMEIRA COLUNA DE lista_registro[i]
        # PAR ISSO USE O 'list.insert()' ASSIM NÂO PRECISA RECOSNTRUIR



        lista_produtos = ['ID_Compra', 'Pão Francês', 'Bolo de Milho', 'Bolo de Fubá',
                          'Pão de Queijo', 'Leite', 'Manteiga', 'Margarina', 'Água', 'Refrigerante']

        return [lista_produtos,lista_registro]
    else:
        return []
    
#CUIDADO DAQUI PARA BAIXO - NÃO ALTERAR ESTA PARTE - SERVE PARA TESTE!

if __name__ == '__main__':
    
    import os

    os.system('cls')
    lista_out = leitura_json('compras_novos.json')
   
   
   
    print('\n ------------Verificando a leitura do CSV------------')
    print('\n ----------------Nomes das colunas:------------------')
    print(lista_out[0])
    print('\n ----------------Dados das colunas:------------------')
    for linha in lista_out[1]:
        print(linha)