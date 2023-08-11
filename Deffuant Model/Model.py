import numpy as np
import matplotlib.pyplot as plt
import time
import os
from tqdm import trange
plt.style.use('ggplot')

def model(N, steps ,dt, E, U, nombre):
    '''
    INPUT
    N : numero de agentes
    steps : numero de pasos temporales
    dt : numero de interacciones que corresponden a un paso temporal
    E:  umbral de opinion
    U: parametro de convergencia
    nombre: Nombre de carpeta donde guardar los archivos
    '''
    start=time.time()
    path = './Simulacion/'+ str(nombre)+'/'
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    with open(path+'/log.txt', 'w') as file: ##Archivo que guardará los parámetros usados
        file.write( 'El numero de agentes es: '+str(N)+'\n')
        file.write('El paso temporal se definió como '+str(dt)+' emparejamientos'+'\n')
        file.write('Se consideraron '+str(steps)+' pasos temporales'+'\n')
        file.write('El umbral utilizado fue: '+str(E)+'\n')
        file.write('El parámetro de convergencia utilizado fue: '+str(U)+'\n')
    Agents = list(np.random.uniform(0, 1, size=N)) # Condicion inicial
    timesteps = [0]*(steps) # Lista para parear los pasos temporales
    timesteps[0] = Agents.copy() # Tiempo de la condicion inicial
    aux = 0 # Variable auxiliar para contar las interacciones
    for t in trange(1,steps):
        i, j = np.random.randint(N), np.random.randint(N) # Elige dos agentes aleatoriamente
        if (np.abs(Agents[i]-Agents[j]) < E): # Compara sus opiniones
            Agents[i] = Agents[i] + U*(Agents[j] - Agents[i])
            Agents[j] = Agents[j] + U*(Agents[i] - Agents[j])
            aux += 1
        if aux >= dt:
            aux = 0
            timesteps[t] = Agents.copy()
        else:
            timesteps[t] = Agents.copy()
    end=time.time()
    with open(path+'/log.txt', 'a') as file:
        file.write("El calculo de esta simulación se demoró : "+str(end-start)+ " segundos")
    print("El tiempo de calculo es "+str(end-start)+ " segundos")
    return timesteps

def plotter(N, steps ,dt, E, U, nombre):
    path = './Simulacion/'+ str(nombre)+'/'
    res=model(N, steps ,dt, E, U, nombre)
    ts=[[i]*N for i in range(steps)]
    plt.scatter(ts,res, s = 1.6)
    plt.xlabel('tiempo')
    plt.ylabel('Opinión')
    plt.savefig(path+'Umbral='+str(E)+'.png')
    plt.show