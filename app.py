from flask import Flask, render_template, redirect
from os import listdir
import random

files = []
currentClassName = ''

def imgToName(img):
    name = img.replace('.jpeg', '').split('_')
    name = ' '.join(name)
    return name

def updateFileList(className):
    global files
    files = listdir('static/imgs/' + className)

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return redirect('/show/CS_190')

@app.route("/show/<className>")
def show(className):
    print('HERE')
    global files, currentClassName
    if(currentClassName != className or len(files) == 0):
        currentClassName = className
        updateFileList(className)

    img = random.choice(files)
    files.remove(img)
    print(len(files))

    name = imgToName(img)
    return render_template('show.html', className=className, img=img, name=name)

app.run(debug=True)