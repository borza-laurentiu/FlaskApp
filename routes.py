from flask import Flask
from flask import render_template, request 

app = Flask(__name__)

def checksVowels(word):
    vowelsUpper = ('A', 'E', 'I', 'O', 'U')
    vowelsLower = ('a', 'e', 'i', 'o', 'u')
    article = ''

    if word.startswith(vowelsUpper) or word.startswith(vowelsUpper):
        article = 'an'
    else:
        article = 'a'
    return article

@app.route('/', methods=['GET', 'POST'])

def output():
    formData = request.form.get('article')
    formData = str(formData)
    article = checksVowels(formData)
    return render_template('output.html', article=article, formData=formData)

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)