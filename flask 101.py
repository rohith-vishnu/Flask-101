from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello am rohith'

@app.route('/temp')
def temp():
    authors=['dan brown','john grisham','john green','JK rowling']
    books=['digital fortress','the client','fault in our stars','Harry potter']
    return '''
    <html>
        <head>
            <title>List of books</title>
        </head>
        <body>
            <h1> books</h1>
            <p>author ''' +authors[0] +''' wrote '''+books[0]+'''</p>
        </body>
    </html>'''



if __name__ == "__main__":
    app.run(debug= True)