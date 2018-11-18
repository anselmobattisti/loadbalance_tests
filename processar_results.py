import matplotlib.pyplot as plt
import numpy as np

file_size = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# file_size = [500, 1000]

linha = "Size;Random Time;Random Trans Rate;Round Robin Time;Round Robin Rate;Round Robin Weight Time;Round Robin Weight Rate\n";


path = './results/exponencial/'
path_save = 'exp1.csv'

# path = './results/balanceado/'
# path_save = 'exp2.csv'

# path = './results/desbalanceado/'
# path_save = 'exp3.csv'

for f in file_size:

  tipos = ['r', 'rr', 'rrw']
    
  linha = linha + str(f) + ";"
  
  for t in tipos:

    file_name = path+str(f)+"_"+t+".txt"
    
    arquivo = open(file_name, "r")
    
    lines=arquivo.readlines()
    
    time_per_request = lines[22][24:31];
    tranference_rate = lines[23][24:31];
  
    linha = linha + time_per_request
    linha = linha + ";" +tranference_rate
    
    if t != 'rrw':
      linha = linha + ";"

  linha = linha + "\n";

f_csv = open(path+path_save, "w")
f_csv.write(linha)
f_csv.close()

print(linha)
