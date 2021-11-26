import pandas as pd

#http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip

url="http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip"
c=pd.read_csv(url, 'BX-Books.csv')