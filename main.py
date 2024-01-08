from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
    # Заготовка для парсера контента сайта
    url = request.form['url']

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = []
    # здесь типа должен быть код самого парсера, результат которого сохраняется в список headlines
    # который выводиься в шаблон results.html
        
    return render_template('results.html', headlines=headlines)


if __name__ == '__main__':
    app.run(debug=True)