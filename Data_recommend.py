import pandas as pd
from flask import Flask, redirect, url_for, render_template, request

data = pd.read_csv('dataset_complete.csv', low_memory=False )


#pd.set_option('display.width', 400)
#pd.set_option('max_columns', None)

#print (data)



# app web interface

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def insert_book():
    if request.method == "POST":
        name = request.form["book"]

        author_name = (data.loc[data['Book-Title'] == name]).iloc[1, 2]
        book_from_author_1 = data.loc[data['Book-Author'] == author_name].iloc[1, 1]
        book_from_author_2 = data.loc[data['Book-Author'] == author_name].iloc[2, 1]

        recommend_book = book_from_author_1 + " , " + book_from_author_2
        
        return render_template("web_interface.html", content = recommend_book )
    else:
        return render_template("web_interface.html")



if __name__ == "__main__":
    app.run(debug=True)

