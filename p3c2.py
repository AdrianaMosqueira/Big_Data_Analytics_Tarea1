from mpi4py import MPI

import numpy as np
import pandas as pd
import random
from numpy import genfromtxt

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

tarea2 = genfromtxt('tarea2.csv', delimiter=',')
tarea2_chunk = np.array_split(tarea2, 3)
chunk1=tarea2_chunk[0]
chunk2=tarea2_chunk[1]
chunk3=tarea2_chunk[2]

if rank == 0:    
    max1=chunk1.max()
    comm.Send(max1, dest=3)
    print("El procesador", rank, "encontró",max1)
elif rank == 1:
    max2=chunk2.max()
    comm.Send(max2, dest=3)
    print("El procesador",rank,"encontró",max2)
elif rank == 2:
    max3=chunk3.max()
    comm.Send(max3, dest=3)
    print("El procesador",rank,"encontró",max3)
elif rank == 3:
    max1 = np.empty(1)
    max2 = np.empty(1)
    max3 = np.empty(1)
    comm.Recv(max1, source=0)
    comm.Recv(max2, source=1)
    comm.Recv(max3, source=2)
    maxtot=max(max1,max2,max3)
    print("El procesador",rank,"encontró",maxtot)
