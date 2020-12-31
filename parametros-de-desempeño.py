import csv

def imprimir(matriz, listaEntregasATiempo,camion):
  camion = camion-1
  
  print(f"Eficiencia en tiempo de Despacho = {matriz[camion][0]} %")
  print(f"Tasa de entrega = {matriz[camion][1]}")
  print(f"Nivel de cumplimiento = {matriz[camion][2]} %")
  print(f"Entregas a tiempo = {listaEntregasATiempo[camion]} %")

def convercionAsignado(lector1):  
  cont = 0
  asignado = []
  for fila in lector1:
    if cont > 0:
      lista = [] 
      lista.append(fila[0])
      for i in range(4):
        lista.append(int(fila[i+1]))  
      asignado.append(lista)
    cont = 1
  return asignado

def convercionRegistrado(lector2):
  cont = 0
  registrado = []
  for fila in lector2:
    if cont > 0:
      lista = [] 
      lista.append(fila[0])
      for i in range(4):
        lista.append(int(fila[i+1]))
      registrado.append(lista)
    cont=1
  return registrado

def calculoRendimiento(asignado,registrado,cliente):
  listaEntregasATiempo = []
  matrizResultados = []
  contador = 0
  contadorEntregas = 0
  if cliente == "1":
    Cliente = "Lactocaribe"
    numeroCamiones = 5
  if cliente == "2":
    Cliente = "Frigoaves" 
    numeroCamiones = 4
  for i in range(numeroCamiones):
    
    lista = []
    sumaTiempoAsignado = 0
    sumaTiempoRegistrado = 0
    sumaLitros = 0
    sumaLitrosAsignados = 0
    contadorEntregas = 0
 
    for j in range(len(asignado)):
      if asignado[j][0] == Cliente:
        if i+1 == registrado[j][2]:
          
          if asignado[j][4] > 0 and registrado[j][4] > 0:
            sumaTiempoAsignado += asignado[j][4]
            sumaTiempoRegistrado += registrado[j][4]
            
          if asignado[j][4] > 0 and registrado[j][4] > 0 and  registrado[j][3] > 0 and asignado[j][3] > 0:
            contadorEntregas += 1
            
            if registrado[j][4] <= asignado[j][4]:
              contador += 1
          if registrado[j][3] > 0 and asignado[j][3] > 0:
            sumaLitros += registrado[j][3]
            sumaLitrosAsignados += asignado[j][3]
     
    entregasATiempo = round((contador /contadorEntregas )*100,1)
    listaEntregasATiempo.append(entregasATiempo)
    contador = 0
    contadorEntregas = 0
    eficiencia = round(((sumaTiempoAsignado - sumaTiempoRegistrado) / sumaTiempoAsignado) * 100,1)
    tasaEntrega = round((sumaLitros /sumaTiempoRegistrado) ,1)
    nivelCumplimiento = round((sumaLitros /sumaLitrosAsignados) * 100 ,1)
    lista.append(eficiencia)
    lista.append(tasaEntrega)
    lista.append(nivelCumplimiento)
    matrizResultados.append(lista)  

    
  return matrizResultados, listaEntregasATiempo

def control(asignacionfile,registrofile):

  asignacionfile =  open(asignacionfile, mode='r', encoding='utf-8-sig' ) 
  registrofile =  open(registrofile, mode='r', encoding='utf-8-sig' ) 
  nuevoArchivo = open('archivoResultados.csv', mode='w', encoding='utf-8-sig' )
  registro = csv.reader(registrofile)
  asignacion = csv.reader(asignacionfile)
  
  
  asignado = convercionAsignado(asignacion)
  registrado = convercionRegistrado(registro)
  cliente = input("ingresa la compañia, donde 1 corresponde a Lactocaribe y 2 a Frigogaves")
  camion = int(input("ingresa el ID del camión de los cuales se van a obetner los indicadores de desempeño"))
  calculoRendimiento(asignado,registrado,cliente)
  
  listaEntregasATiempo = calculoRendimiento(asignado,registrado,cliente)[1]
  matriz= calculoRendimiento(asignado,registrado,cliente)[0]
  imprimir(matriz, listaEntregasATiempo,camion)
  
  escritor = csv.writer(nuevoArchivo)
  lista = ["Eficiencia en tiempo de Despacho","Tasa de entrega ","Nivel de cumplimiento","Entregas a tiempo"]
  escritor.writerow(lista)
  for i in range(len(matriz)):
    lista = []
  
     
    lista.append(matriz[i][0])
    lista.append(matriz[i][1])
    lista.append(matriz[i][2])
    lista.append(listaEntregasATiempo[i])
    escritor.writerow(lista)