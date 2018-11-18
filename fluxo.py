import subprocess

file_size = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# file_size = [500]

for x in file_size:
  f = open("results/"+str(x)+"_rrw.txt", "w")
  subprocess.call(["ab", "-n 30", "-c 5", "-r", "http://10.0.1.1/dados/d_"+str(x)], stdout=f)
