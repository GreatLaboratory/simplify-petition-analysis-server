import requests
from flask import Flask, redirect
from flask_cors import CORS
from WordCloud import visualize, get_nouns

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/wordCloud/<category>')
def wordCloud(category):
    res = requests.get('http://localhost:1323/wordCloud/'+category)
    words = get_nouns(res.text)
    visualize(words, category)
    return redirect('http://localhost:5000/wordCloud_'+category+'.png')


@app.route('/api/summary/<petitionID>')
def summary(petitionID):
    res = requests.get('http://localhost:1323/summary/'+petitionID)
    result = res.json()
    question = result['question']
    answer = result['answer']
    return ''


if __name__ == '__main__':
    app.run()
