from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x // y

# A simple server with simple arithmetic functions
# server_address = localhost (127.0.0.1)
# server_port = 8080
server = SimpleXMLRPCServer(("localhost", 8080))
print("Listening on port 8080...")

#server.register_functions()
server.register_function(add, 'add')
server.register_function(sub, 'sub')
server.register_function(mult, 'mult')
server.register_function(div, 'div')

#wait for requests
server.serve_forever()
