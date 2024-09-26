import sys
import os
import pytest

# Adiciona o diretório raiz do projeto ao sys.path para que o Python possa encontrar o project.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as funções do project.py
from project import check_patient_name, check_bed_number, check_patient_weight

def test_check_patient_name():
    assert check_patient_name("John Doe") == True
    assert check_patient_name("") == False
    assert check_patient_name("   ") == False  # Testa apenas espaços em branco

def test_check_bed_number():
    assert check_bed_number("123") == True
    assert check_bed_number("ABC") == False
    assert check_bed_number("12A") == False

def test_check_patient_weight():
    assert check_patient_weight("4.5") == True
    assert check_patient_weight("6") == False  # Peso acima de 5 kg
    assert check_patient_weight("abc") == False  # Valor não numérico
