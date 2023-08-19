from flask import Flask
app = Flask(__name__)

#print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello pmc</h1>'\
    '<p> This is a paragraph</p>' \
    '<img src="https://media.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif">' 

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/username/<name>/<int:numb>')
def greet(name, numb):
    return f"Hello {name} and you have $ {numb} in your account"


#excecute only if run as a script
if __name__ == "__main__":
    app.run(debug=True)