import math

def areatriangungulo():
    altura = float(input('Digite a altura do triângulo : '))
    base = float(input('Digite a base do triãngulo: '))
    areat = round(((base * altura) / 2),2)
    print('A área do triângulo  é de  ', areat)

def perimetro_triangulo ():
  lado1 = int(input("Digite o primeiro lado do triangulo: "))
  lado2 = int(input("Digite o segundo lado do triangulo: "))
  lado3 = int(input("Digite o primeiro lado do triangulo: "))
  pt = (lado1 + lado2 + lado3)
  print(f'A area é: {pt}')
    
  
def areaquadradro():
    lado = float(input('Digite a altura do quadrado: '))
    areaq = lado**2
    print('A área do quadrado é de ', areaq)


def perimetro_quadro():
  lado = float(input("Digite o lado do quadrado: "))
  pq = lado*4 
  print(f"A area do quadrado é: {pq} ")

def arearetangulo():
    alturaret = float(input('Digite a altura do retângulo: '))
    baseret = float(input('Digite a altura do retângulo: '))
    arearet = round((alturaret*baseret),2)
    print('A área do retângulo é de ', arearet)

    
def areacirculo ():
    #area do círculo  π . r2
    raio = float(input('Digite o raio do circulo: '))
    areac = round((math.pi * raio**2),2)
    print('A área do círculo  é de ', areac)

def perimetro_retangulo():
  lado = float(input("Digite o primeiro lado do retangulo: "))
  lado2 = float(input("Digite o segundo lado do retangulo: "))
  cal1 = lado * 2 
  cal2 = lado2 * 2
  
  pq = cal1 + cal2 
  print(f"A area do retangulo é: {pq} ")


while True:
    print("\n")
    print("Calculadora de áreas")
    print("""
    1.Calcular àrea do triângulo
    2.Calcular àrea do quadrado
    3.Calcular àrea do retângulo
    4.Calcular àrea do círculo
    5.Perimetro do triangulo
    6. Perimetro do Quadrado
    7. Perimetro do Retangulo
    58.Exit/Quit/Saída
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        print('\n')
        areatriangungulo()
    elif escolha=="2":
      print('\n')
      areaquadradro()
    elif escolha=="3":
        print('\n')
        arearetangulo()
    elif escolha == "4":
        print('\n')
        areacirculo()
    elif escolha == "5":
        print('\n')
        perimetro_triangulo()
    elif escolha == "6":
        print('\n')
        perimetro_quadro()
    elif escolha == "7":
        print('\n')
        perimetro_retangulo()
        
    elif escolha=="8":
      print("\n Adeus")
      break
    else:
       print("\n Escolha não válida.\n Tente outra vez.")
