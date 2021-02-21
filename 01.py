def imc(height, weight):
    imc = weight / height ** 2
    if imc < 18.6:
        return f'Abaixo do peso, IMC = {imc:.2f}'
    elif imc <= 24.9:
        return f'Peso normal, IMC = {imc:.2f}'
    elif imc <= 29.9:
        return f'Sobrepeso, IMC = {imc:.2f}'
    else:
        return f'Obesidade, IMC = {imc:.2f}'
