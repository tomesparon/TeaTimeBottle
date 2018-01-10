import os
from bottle import route, run, get, post, template, request





@route('/')
def index():
    return template('main_template')

@get('/tea')
def form():
    return '''<h2>Remote Kettle 0.1-alpha</h2>
              <form method="POST" action="/tea">
                <input name="hiddenfield" type="hidden" value='somevalue' />
                <input type="submit" value="Turn the kettle on!"/>
              </form>'''

@post('/tea')
def submit():
    # grab data from form
    #name1 = request.forms.get('name1')
    from subprocess import call
    call(["python", "piservo.py"])


    return '<h1> The kettle is now on!</h1>'
         


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    run(host='127.0.0.1', port=port, debug=False)
