#http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip

from io import BytesIO
import zipfile
import requests
import pandas as pd

#file = 'BX-Books.csv'

url = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'

'''
#download and extract files from the url
request = requests.get(url)
zipDocument = zipfile.ZipFile(BytesIO(request.content))
zipDocument.extractall()
'''

books = pd.read_csv('BX-Books.csv', encoding='cp1251', sep=';', error_bad_lines=False)
ratings = pd.read_csv('BX-Book-Ratings.csv', encoding='cp1251', sep=';')
users = pd.read_csv('BX-Users.csv', encoding='cp1251', sep=';')

dataset_books_ratings = pd.merge(books,ratings, on= ['ISBN'])
dataset_complete = pd.merge(dataset_books_ratings, users, on = ['User-ID'])

pd.set_option('max_columns', None)
print(dataset_complete)