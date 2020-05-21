from bottle import route, run, template 
@route('/hello/<name>') 
def index(name): 
	return template('<b>Hello {{name}}</b>!', name=name) 
run(host='localhost', port=8080) 

#go to browser and type http://localhost:8080/hello/arturo