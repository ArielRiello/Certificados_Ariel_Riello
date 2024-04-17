consumo = float(input())

def recomandar_plano(consumo):
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    elif consumo > 10 and consumo <= 20:
        print("Plano Prata Fibra - 100Mbps")
    elif consumo > 20:
        print("Plano Premium Fibra - 300Mbps")

recomandar_plano(consumo)