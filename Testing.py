#Testing
from Sistemas_de_referencia import SRG, SRL
from cuerpos import Punto
import numpy as np
from funciones import integrar, plot, transformar_coordenadas, derivar,integrar
from matrices_rotacion import *
from tiempo import tiempo, dt
sr0=SRG()
sr0.crear('A')
sr1=SRL(sr0,'A')
sr1.crear('B')

#
acel=[np.array([-10,0,0]) for i in range(len(tiempo))]
vel=integrar(acel)


print(vel[100]==vel[101])

