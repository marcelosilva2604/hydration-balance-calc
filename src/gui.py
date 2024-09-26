import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from calculations import calculate_hydration

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.results_window = None
        self.create_widgets()

    def create_widgets(self):
        # Cria as abas
        self.tabs = ['Dados do Paciente', 'Medições', 'Outros Valores']
        self.notebook = ttk.Notebook(self.master)
        self.frames = {}

        for tab in self.tabs:
            self.frames[tab] = tk.Frame(self.notebook)
            self.notebook.add(self.frames[tab], text=tab)

        self.notebook.pack(fill='both', expand=True)

        # Seletor de tempo (12 ou 24 horas)
        self.horas = tk.IntVar(value=24)
        radio_button_frame = tk.Frame(self.frames['Dados do Paciente'])
        self.balanco_hidrico_radios = [
            tk.Radiobutton(radio_button_frame, text="12 horas", variable=self.horas, value=12),
            tk.Radiobutton(radio_button_frame, text="24 horas", variable=self.horas, value=24)
        ]
        for radio in self.balanco_hidrico_radios:
            radio.pack(side='left')
        radio_button_frame.pack(pady=10)

        # Campos de entrada organizados por aba
        self.fields = {
            'Dados do Paciente': ['Nome do Paciente', 'Leito do Paciente', 'Peso (kg)'],
            'Medições': ['Temperatura', 'Temperatura da incubadora', 'Frequência cardíaca', 'Frequência respiratória', 'Pressão arterial média', 'Saturação de Oxigênio', 'Glicemia Capilar'],
            'Outros Valores': ['Dieta', 'Soro', 'Medicação', 'Diurese', 'Resíduo Gástrico', 'Êmese', 'Evacuações']
        }

        self.entries = {}
        self.totals = {}

        # Cria os campos de entrada para cada aba
        for tab in self.tabs:
            for field in self.fields[tab]:
                label = tk.Label(self.frames[tab], text=f"{field}: ")
                label.pack()
                entry = tk.Entry(self.frames[tab])
                entry.pack()
                self.entries[field] = entry

                # Se for a aba "Outros Valores", permite totalizar os valores
                if tab == 'Outros Valores':
                    total = tk.StringVar()
                    total_label = tk.Label(self.frames[tab], textvariable=total)
                    total_label.pack()
                    self.totals[field] = total
                    self.entries[field].bind('<Return>', lambda event, field=field: self.add_value(field))

        # Botão para calcular o balanço hídrico
        self.calc_button = tk.Button(self.frames['Outros Valores'])
        self.calc_button["text"] = "Calcular"
        self.calc_button["command"] = self.calculate
        self.calc_button.pack()

    # Função para adicionar o valor total de um campo da aba "Outros Valores"
    def add_value(self, field):
        try:
            current_total = float(eval(self.totals[field].get() or "0"))
            new_value = eval(self.entries[field].get().replace(',', '.'))
            self.totals[field].set(round(current_total + new_value, 2))
            self.entries[field].delete(0, tk.END)
        except Exception:
            messagebox.showerror("Erro", "Por favor, insira uma expressão válida.")

    # Função para calcular o balanço hídrico e exibir o resultado
    def calculate(self):
        try:
            # Verifica se os campos obrigatórios estão preenchidos
            paciente = self.entries['Nome do Paciente'].get()
            leito = self.entries['Leito do Paciente'].get()
            peso_str = self.entries['Peso (kg)'].get().replace(',', '.')

            # Se qualquer um dos campos obrigatórios estiver vazio, exibe um erro
            if not paciente or not leito or not peso_str:
                messagebox.showerror("Erro", "Por favor, preencha os campos Nome, Leito e Peso.")
                return

            # Tenta converter o peso para float, exibe erro se falhar
            try:
                peso = float(peso_str)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um valor válido para o Peso.")
                return

            horas = self.horas.get()

            # Gera o texto de saída com os dados do paciente
            output_str = f"Paciente: {paciente}\nLeito - {leito} / Peso - {peso:.2f}kg\n\n"

            # Adiciona as medições ao texto final, permite que os campos fiquem em branco
            for field in self.fields['Medições']:
                val = self.entries[field].get().replace(',', '.') or "Não informado"
                output_str += f"{field}: {val}\n"

            # Verifica os campos opcionais em "Outros Valores" e trata campos em branco como 0
            for field in ['Dieta', 'Soro', 'Medicação', 'Diurese', 'Resíduo Gástrico', 'Êmese', 'Evacuações']:
                val = self.totals[field].get() or "0"  # Se o campo estiver em branco, trata como "0"
                self.totals[field].set(val)  # Define o valor como "0" no total se estiver vazio

            # Chama a função de cálculo para processar o balanço hídrico
            output_str += calculate_hydration(self.entries, self.totals, horas, peso)

            # Exibe o resultado em uma nova janela
            if self.results_window:
                self.results_window.destroy()

            self.results_window = tk.Toplevel(self.master)
            label = tk.Label(self.results_window, text=output_str, font=('Helvetica', 14), justify="left")
            label.pack()

            copy_button = tk.Button(self.results_window, text="Copiar Valores", command=self.copy_to_clipboard)
            copy_button.pack()

            new_patient_button = tk.Button(self.results_window, text="Novo Paciente", command=self.new_patient)
            new_patient_button.pack()

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Função para resetar os campos e começar um novo paciente
    def new_patient(self):
        result = messagebox.askyesno("Novo Paciente", "Deseja inserir valores para um novo paciente?")
        if result:
            for field in self.entries.values():
                field.delete(0, tk.END)
            for total in self.totals.values():
                total.set('')
            if self.results_window:
                self.results_window.destroy()
            self.notebook.select(self.frames['Dados do Paciente'])
        else:
            pass

    # Função para copiar os resultados para a área de transferência
    def copy_to_clipboard(self):
        text = self.results_window.children['!label'].cget('text')
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        copy_button = self.results_window.children['!button']
        copy_button['text'] = 'Dados copiados ✔️'
        copy_button['state'] = tk.DISABLED
