from io import BytesIO
import zipfile
import requests
import pandas as pd


url = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'

'''
#download and extract files from the url
request = requests.get(url)
zipDocument = zipfile.ZipFile(BytesIO(request.content))
zipDocument.extractall()
'''
#read all data
books = pd.read_csv('BX-Books.csv', encoding='cp1251', sep=';', error_bad_lines=False)
ratings = pd.read_csv('BX-Book-Ratings.csv', encoding='cp1251', sep=';')
users = pd.read_csv('BX-Users.csv', encoding='cp1251', sep=';')

#merge all data
dataset_books_ratings = pd.merge(books,ratings, on= ['ISBN'])
dataset_complete = pd.merge(dataset_books_ratings, users, on = ['User-ID'])

#removes useless columns
dataset_complete = dataset_complete.drop(columns=['Image-URL-S','Image-URL-L'])

#making all data lower case
dataset_complete = dataset_complete.applymap(lambda x: x.lower() if type(x) == str else x)

#rearranging the dataset
cols = list(dataset_complete.columns.values)
#dataset_complete = dataset_complete[ cols[0:2] + cols[-4:-1] + cols[3:8] ]


pd.set_option('display.width', 400)
pd.set_option('max_columns', None)
print(dataset_complete)