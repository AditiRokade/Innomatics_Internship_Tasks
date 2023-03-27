import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('name')
    if username is None:
        return "Please provide a name parameter in the URL."
    else:
        return 'Hello, {}!'.format(username.upper())

@app.route('/random')
def generate_random():
    number = random.randint(1, 10)
    return 'Random number: {}'.format(number)

def reverse_string(s):
    return s[::-1]

@app.route('/reverse')
def reverse():
    word = request.args.get('word')
    if word is None:
        return "Please provide a word parameter in the URL."
    else:
        return 'Reversed word: {}'.format(reverse_string(word))

if __name__ == '__main__':
    app.run()
