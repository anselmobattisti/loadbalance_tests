import requests
import time
for x in range(0, 6):
  ts1 = int(time.time())
  r = requests.get("http://10.0.1.1/dados")
  ts2 = int(time.time())
  print(r.headers)
  print('#{}---------'.format(x))
  print(ts2-ts1)
  print('-----------------\n')