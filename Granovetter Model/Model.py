import numpy as np
import matplotlib.pyplot as plt
import os

def uniforme(tamaño, Umbral): # Se define la función con la distribución uniforme
    Agents=np.random.randint(0,100,tamaño) # Asigna un umbral a cada agente
    adhesion=0 
    retraccion=0
    for i in range(len(Agents)): #Verifica si hay suficiente gente protestando
        if Agents[i]>Umbral:
            retraccion+=1
        if Agents[i]<=Umbral:
            adhesion+=1
    if np.ceil((adhesion/len(Agents))*100)<1:
        Umbral=np.ceil((adhesion/len(Agents))*100)
    else:
        Umbral=adhesion
        #print(Umbral, adhesion,retraccion)
    return adhesion

def normal(tamaño, media, std,  Umbral): # Se define la función con la distribución normal
    Agents=np.ceil(np.abs(np.random.normal(media,std,tamaño))*100) # Asigna un umbral a cada agente
    adhesion=0
    retraccion=0
    for i in range(len(Agents)): #Verifica si hay suficiente gente protestando
        if Agents[i]>Umbral:
            retraccion+=1
        if Agents[i]<=Umbral:
            adhesion+=1
    if np.ceil((adhesion/len(Agents))*100)<1:
        Umbral=np.ceil((adhesion/len(Agents))*100)
    else:
        Umbral=adhesion
        #print(Umbral, adhesion,retraccion)
    return adhesion

def simul(funcion,carpeta,media=0,std=0): #Se define una única función que correrá los modelos
    path='./Simulacion/'+str(carpeta)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    wa=np.linspace(0,100,100) #El gráfico es para valores del umbral entre 0 y 100
    lista=[]
    for elem in range(len(wa)):
        if funcion==uniforme:
            with open(path+'/log.txt', 'w') as file: ##Archivo que guardará los parámetros usados
                file.write( 'Se utilizó la distribución uniforme')
            asd=uniforme(1000,wa[elem])
            lista.append(asd/10)
        if funcion==normal:
            asd=normal(1000,media, std, wa[elem])
            lista.append(asd/10)
            with open(path+'/log.txt', 'w') as file:
                file.write( 'Se utilizó la distribución normal'+'\n')
                file.write("La media utilizada fue: "+str(media)+'\n')
                file.write("La desviación utilizada fue: "+str(std)+'\n')
    plt.plot(wa,lista)
    plt.plot(wa,wa, 'r--')
    plt.grid(True)
    plt.savefig(path+'/simul.png')