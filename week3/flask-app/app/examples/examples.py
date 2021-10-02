from flask import Flask, request

app = Flask(__name__)


# form related
@app.route('/formtest', methods=['POST', 'GET'])
def form_test():
    if request.method == 'POST':
        return 'Username: %s' % (request.form['username'])
    else:
        return ''' <form action="/formtest" method="post">
        Name: <input name="username" type="text" /> <br/>
        <input value="Send" type="submit" />
        </form> '''


#  Some business logic
@app.route('/list')
def list():
    retstr = ""
    with open('list.txt') as f:
        for l in f.readlines():
            retstr += l + '<br/>'
            return retstr


@app.route('/write', methods=['POST', 'GET'])
def write_article():
    if request.method == 'POST':

        article = request.form['article']
        with open('list.txt', 'a') as f:
            f.write(article)
            return 'Write Successful'

    else:
        return ''' <form action="/write" method="post">
        Article: <input name="article" type="text" /> <br/>
        <input value="Write" type="submit" />
        </form> '''


app.run(debug=True, port=10000)
