import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
#import sys


#inputFile = sys.argv[1]
#dis_thr_str = sys.argv[2]
#dis_thr_seq = sys.argv[3]


inputFile = input("Enter File Name:")
dis_thr_str= input("Enter a value for distance threshold in structure (D):")
dis_thr_seq= input("Enter another value for distance threshold in the sequence (S):")



df_A = pd.DataFrame(columns=['Atom','AtomSN','Element','Res','Chain','ResNumber','x','y','z'])
df_B = pd.DataFrame(columns=['Atom','AtomSN','Element','Res','Chain','ResNumber','x','y','z'])
df_C = pd.DataFrame(columns=['Atom','AtomSN','Element','Res','Chain','ResNumber','x','y','z'])
df_D = pd.DataFrame(columns=['Atom','AtomSN','Element','Res','Chain','ResNumber','x','y','z'])


pdbTraj = open(inputFile, 'r')
pdbTraj_line = pdbTraj.readlines()
newFile = open('newfile.txt', 'w')
pdbDict = {}
resNumberList1 = []
resNumberList2 = []
chainTry = "A"
i = 0
for line in pdbTraj_line:
    if line.startswith(("ATOM" or "HETATM")):
        i += 1
        atomType = line[0:6]
        atomSerialNumber = line[6:11]
        atomName = line[12:16]
        resName = line[17:20]
        chain = line[21]
        resNumber = line[22:26]
        coorX = line[30:38]
        coorY = line[38:46]
        coorZ = line[46:54]
        df_temp = pd.DataFrame({'Atom': atomType ,'AtomSN': atomSerialNumber ,'Element':atomName ,'Res':resName,'Chain':chain,'ResNumber': resNumber,'x':coorX,'y': coorY,'z': coorZ,}, index=[0])
        if ((str(atomName).strip()) == 'CA'):
            if ((str(chain).strip()) == 'A'):
                df_A = pd.concat([df_temp, df_A])
            if ((str(chain).strip()) == 'B'):
                df_B = pd.concat([df_temp, df_B])
            if ((str(chain).strip()) == 'A'):
                df_C = pd.concat([df_temp, df_C])
            if ((str(chain).strip()) == 'A'):
                df_D = pd.concat([df_temp, df_D])




## Distance computations for A
A = np.zeros((141, 3))
A[:, 0] = df_A['x']
A[:, 1] = df_A['y']
A[:, 2] = df_A['z']
pairwiseDistA = cdist(A, A)
#Mask
mask = pairwiseDistA < float(dis_thr_str)
pairwiseDistA = pairwiseDistA * mask
pairwiseDistA = np.triu(pairwiseDistA)
(r, c) = np.nonzero(pairwiseDistA)
printList_A = []
#Extract the data
for (i, j) in zip(r ,c):
    resI = int(df_A['ResNumber'].values[i])
    resJ = int(df_A['ResNumber'].values[j])
    if abs(resI-resJ) >= int(dis_thr_seq):
        printList_A.append((i, j))

## Distance computations for B
B = np.zeros((141, 3))
B[:, 0] = df_A['x']
B[:, 1] = df_A['y']
B[:, 2] = df_A['z']
pairwiseDistB = cdist(B, B)
#Mask
mask = pairwiseDistB < float(dis_thr_str)
pairwiseDistB = pairwiseDistB * mask
pairwiseDistA = np.triu(pairwiseDistB)
(r, c) = np.nonzero(pairwiseDistB)
printList_B = []
#Extract the data
for (i, j) in zip(r ,c):
    resI = int(df_B['ResNumber'].values[i])
    resJ = int(df_B['ResNumber'].values[j])
    if abs(resI-resJ) >= int(dis_thr_seq):
        printList_B.append((i, j))


## Distance computations for C
C = np.zeros((141, 3))
C[:, 0] = df_C['x']
C[:, 1] = df_C['y']
C[:, 2] = df_C['z']
pairwiseDistC = cdist(C, C)
#Mask
mask = pairwiseDistC < float(dis_thr_str)
pairwiseDistC = pairwiseDistC * mask
pairwiseDistC = np.triu(pairwiseDistC)
(r, c) = np.nonzero(pairwiseDistC)
printList_C = []
#Extract the data
for (i, j) in zip(r ,c):
    resI = int(df_C['ResNumber'].values[i])
    resJ = int(df_C['ResNumber'].values[j])
    if abs(resI-resJ) >= int(dis_thr_seq):
        printList_C.append((i, j))
## Distance computations for D
D = np.zeros((141, 3))
D[:, 0] = df_D['x']
D[:, 1] = df_D['y']
D[:, 2] = df_D['z']
pairwiseDistD = cdist(D, D)
#Mask
mask = pairwiseDistD < float(dis_thr_str)
pairwiseDistD = pairwiseDistD * mask
pairwiseDistD = np.triu(pairwiseDistD)
(r, c) = np.nonzero(pairwiseDistD)
printList_D = []

#Extract the data
for (i, j) in zip(r ,c):
    resI = int(df_D['ResNumber'].values[i])
    resJ = int(df_D['ResNumber'].values[j])
    if abs(resI-resJ) >= int(dis_thr_seq):
        printList_D.append((i, j))
""""""
#Print the data
for (i, j) in printList_A:
    print('Chain: A -->', df_A['Res'].values[i], '(', df_A['ResNumber'].values[i], ')' , '-', df_A['Res'].values[j], '(', df_A['ResNumber'].values[j], ')', ':', pairwiseDistA[i][j], 'Angstroms')
for (i, j) in printList_B:
    print('Chain: B -->', df_B['Res'].values[i], '(', df_B['ResNumber'].values[i], ')' , '-', df_B['Res'].values[j], '(', df_B['ResNumber'].values[j], ')', ':', pairwiseDistB[i][j], 'Angstroms')
for (i, j) in printList_C:
    print('Chain: C -->', df_C['Res'].values[i], '(', df_C['ResNumber'].values[i], ')' , '-', df_C['Res'].values[j], '(', df_C['ResNumber'].values[j], ')', ':', pairwiseDistC[i][j], 'Angstroms')
for (i, j) in printList_D:
    print('Chain: D -->', df_D['Res'].values[i], '(', df_D['ResNumber'].values[i], ')' , '-', df_D['Res'].values[j], '(', df_D['ResNumber'].values[j], ')', ':', pairwiseDistD[i][j], 'Angstroms')