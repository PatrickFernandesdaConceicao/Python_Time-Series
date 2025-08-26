
################## -> coloque o cabeçalho do arquivo

#Em python o que é um cabeçalho do arquivo python,
#para que ele serve, qual a diferença do cabeçalho
#do arquivo para uma dockstring e para que serve uma dockstring

#O cabeçalho de um arquivo Python é um bloco de comentários colocado no início do arquivo.
#Ele não é obrigatório, mas é considerado uma boa prática, principalmente em projetos maiores.

#As docstrings são mais comumente introduzidas no início de uma classe, de uma 
#função ou no início do programa para definir o escopo do software ou o escopo de métodos,
#seu símbolo padrão são as três aspas duplas ou simples.

#Para quem está lendo o código do programa não existe muita diferença (exceto estética)
#entre comentários e docstrings, mas para o usuário a diferença é marcante, pois uma docstring
#não é ignorada pelo interpretador, mas passa a fazer parte do objeto sobre o qual ela foi definida,
#podendo ser acessada através do help.




######################################################################

# implemente as funções abaixo e coloque as docstrings

def maximo(nums):
    """oque faz
    oque recebe
    oque retorna"""
    # TODO: percorra a lista guardando o maior atual
    ...

def e_par(n: int) -> bool:
    """ ... """
    # TODO: retorne se n é par
    ...
def fatorial(n: int) -> int:
    """   ...  """
    # TODO: implemente de forma iterativa (sem recursão)
    ...
import re

def limpa_texto(s: str) -> str:
    """..."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """....."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """..."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    executa......
    Recebe: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    ...
    Recebe ...
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...
