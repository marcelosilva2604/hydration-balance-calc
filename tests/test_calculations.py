import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculations import calculate_hydration

def test_hydration_calculation():
    # Simulação de entradas
    entries = {}
    totals = {
        'Dieta': 100,          # ml
        'Soro': 50,            # ml
        'Medicação': 30,       # ml
        'Diurese': 20,         # ml
        'Resíduo Gástrico': 10,# ml
        'Êmese': 0,            # vezes por dia
        'Evacuações': 0        # vezes por dia
    }
    horas = 24  # Número de horas (12 ou 24)
    peso = 3.5  # Peso do paciente em kg

    # Executa a função de cálculo
    result = calculate_hydration(entries, totals, horas, peso)

    # Verifica se a oferta e a perda hídrica aparecem no resultado
    assert "Oferta hídrica" in result
    assert "Perda hídrica" in result
    assert "Balanço hídrico" in result

    # Verifica se os valores calculados estão corretos
    assert "180.0 ml / 51.4 ml/kg" in result  # Oferta hídrica esperada
    assert "30.0 ml / 8.6 ml/kg" in result    # Perda hídrica esperada
    assert "150.0 ml / 42.9 ml/kg" in result  # Balanço hídrico esperado
