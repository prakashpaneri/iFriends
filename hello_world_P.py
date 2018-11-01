from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Prakash'):
    return template('Hello {{name}}, how are you?', name=name)

run(host= 'localhost', port= 8080, debug= True) 