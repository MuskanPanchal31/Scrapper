from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)
@app.route('/', methods=["GET","POST"])

def index():
    url = "https://www.goalcast.com/powerful-motivational-quotes/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    outerdata=soup.find_all("blockquote",class_="wp-block-quote",limit=4)
    finalquote=""
    for data in outerdata:
        quotes = data.p
        finalquote +=  '\u2022' + quotes.get_text() + '\n' 
    return render_template("index.html",Quotes=finalquote)