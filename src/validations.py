import re

def is_valid_input(input_str):
    """
    Verifica se a entrada fornecida é válida.
    Aceita números com ou sem vírgula/ponto decimal, e intervalos numéricos.
    Exemplo de valores válidos: '12', '12.5', '12,5', '12 - 15'.
    """
    return re.match('^-?$|^\d+([.,]\d+)?(\s*-\s*\d+([.,]\d+)?)?$', input_str) is not None or input_str == ''
