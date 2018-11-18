import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

csv_file = 'exp1.csv'

y_salto = 250

if sys.argv[1] == 'exp1':
  csv_file = 'exp1.csv'
  if sys.argv[2] == 't':
    png_file = 'exp1_time.png'
  else:
    png_file = 'exp1_banda.png'

if sys.argv[1] == 'exp2':
  csv_file = 'exp2.csv'
  if sys.argv[2] == 't':
    png_file = 'exp2_time.png'
  else:
    png_file = 'exp2_banda.png'  

if sys.argv[1] == 'exp3':
  csv_file = 'exp3.csv'  
  if sys.argv[2] == 't':
    png_file = 'exp3_time.png'
  else:
    png_file = 'exp3_banda.png'  


if sys.argv[3]:
  y_salto = int(sys.argv[3])
  
xr = []
yr = []

xrr = []
yrr = []

xrrw = []
yrrw = []

with open(csv_file,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
        
    next(plots, None)

    for row in plots:
      
      if sys.argv[2] == 't':
        ylabel = 'Tempo Resposta (ms)'
        xr.append(float(row[0]))
        yr.append(float(row[1]))
        
        xrr.append(float(row[0]))
        yrr.append(float(row[3]))
        
        xrrw.append(float(row[0]))
        yrrw.append(float(row[5]))

      if sys.argv[2] == 'b':
        ylabel = 'Taxa de download (Kbytes/seg)'
        xr.append(float(row[0]))
        yr.append(float(row[2]))
        
        xrr.append(float(row[0]))
        yrr.append(float(row[4]))
        
        xrrw.append(float(row[0]))
        yrrw.append(float(row[6]))

max_y = max([max(yr), max(yrr), max(yrrw)])
        
plt.xticks(np.arange(min(xr), max(xr)+1, 500))
plt.yticks(np.arange(0, max_y+1, y_salto))
plt.plot(xr,yr, 'g^-', label='Random')
plt.plot(xrr,yrr, 'bs-', label='Round Robin')
plt.plot(xrrw,yrrw, 'ro-', label='Round Robin Weighted')
plt.xlabel('Tamanho do arquivo acessado (Kbytes)')
plt.ylabel(ylabel)
# plt.title('Relação entre o tamanho do arquivo e ')
plt.legend()

# plt.show()
plt.savefig('graficos/'+png_file)

