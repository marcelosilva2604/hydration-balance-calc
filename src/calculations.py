import tkinter as tk
from tkinter import messagebox

# Função para calcular o balanço hídrico
def calculate_hydration(entries, totals, horas, peso):
    output_str = ""

    # Verifica se o campo é StringVar (usado na interface Tkinter) ou um valor numérico diretamente
    oferta_hidrica = sum([
        float(totals[field].get() if hasattr(totals[field], 'get') else totals[field])
        for field in ['Dieta', 'Soro', 'Medicação']
    ])
    
    output_str += f"\nOferta hídrica:\n"
    for field in ['Dieta', 'Soro', 'Medicação']:
        val = totals[field].get() if hasattr(totals[field], 'get') else totals[field]
        if val:
            output_str += f"{field}: {val} ml / {float(val) / peso:.1f} ml/kg\n"
        else:
            output_str += f"{field}: -\n"
    output_str += f"Oferta hídrica: {oferta_hidrica} ml / {oferta_hidrica / peso:.1f} ml/kg\n"

    perdas_hidricas = sum([
        float(totals[field].get() if hasattr(totals[field], 'get') else totals[field])
        for field in ['Diurese', 'Resíduo Gástrico']
    ])
    
    output_str += f"\nPerda hídrica:\n"

    diurese = totals['Diurese'].get() if hasattr(totals['Diurese'], 'get') else totals['Diurese']
    if diurese:
        diurese = float(diurese)
        diurese_por_kg_hora = diurese / peso / horas
        output_str += f"Diurese: {diurese} ml / {diurese_por_kg_hora:.1f} ml/kg/h\n"
    else:
        output_str += "Diurese: -\n"

    for field in ['Resíduo Gástrico']:
        val = totals[field].get() if hasattr(totals[field], 'get') else totals[field]
        if val:
            output_str += f"{field}: {val} ml / {float(val) / peso:.1f} ml/kg\n"
        else:
            output_str += f"{field}: -\n"

    for field in ['Êmese', 'Evacuações']:
        val = totals[field].get() if hasattr(totals[field], 'get') else totals[field]
        output_str += f"{field}: {val} vezes por dia\n"

    output_str += f"Perda hídrica: {perdas_hidricas} ml / {perdas_hidricas / peso:.1f} ml/kg\n"

    balanco_hidrico = oferta_hidrica - perdas_hidricas
    output_str += f"\nBalanço hídrico: {balanco_hidrico} ml / {balanco_hidrico / peso:.1f} ml/kg\n"

    return output_str
