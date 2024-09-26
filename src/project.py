import tkinter as tk
from gui import Application  # Importa a interface gráfica

def main():
    # Inicializa o programa com Tkinter
    root = tk.Tk()
    root.title("Neonatal Balance Calc")  # Define o título da janela principal
    app = Application(master=root)
    app.mainloop()

# Função para verificar se o nome do paciente foi inserido
def check_patient_name(name):
    return bool(name.strip())  # Retorna True se o nome não estiver vazio

# Função para verificar se o leito foi inserido e é numérico
def check_bed_number(bed):
    return bed.isdigit()  # Retorna True se o leito for numérico

# Função para garantir que o peso não ultrapasse 5 kg
def check_patient_weight(weight):
    try:
        weight_float = float(weight)
        return weight_float <= 5.0  # Retorna True se o peso for menor ou igual a 5 kg
    except ValueError:
        return False  # Retorna False se o valor não puder ser convertido para float

if __name__ == "__main__":
    main()
