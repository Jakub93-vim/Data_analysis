import pandas as pd
from flask import Flask, redirect, url_for, render_template, request

data = pd.read_csv('dataset_complete.csv', low_memory=False )

name = 'decision in normandy'

author_name = (data.loc[data['Book-Title'] == name]).iloc[1,2]
books_from_author = data.loc[data['Book-Author'] == author_name].iloc[1:4,1]


pd.set_option('display.width', 400)
pd.set_option('max_columns', None)

print (data)
print(author_name)
print(books_from_author)
'''

# app web interface

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def insert_book():
    if request.method == "POST":
        input_book = request.form["book"]

        recommend_book = input_book + "second book" + " last book "
        
        return render_template("web_interface.html", content = recommend_book )
    else:
        return render_template("web_interface.html")



if __name__ == "__main__":
    app.run(debug=True)

'''