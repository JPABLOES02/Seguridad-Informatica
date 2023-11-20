def calculadora(miPersona):
    nombre = miPersona["nombre"]
    peso = miPersona["peso"]
    altura = miPersona["altura"]**2
    IMC = peso / altura
    IndiceM = round(IMC, 2)
    
    if IMC >= 30:
        Npeso = "Obesidad"
    elif IMC >= 25:
        Npeso = "Sobrepeso"
    elif IMC > 18.5:
        Npeso = "Normal"
    else:
        Npeso = "Bajo peso"
        
    print(f"Eres {nombre}, tu IMC es {IndiceM} y tu peso es: {Npeso}")