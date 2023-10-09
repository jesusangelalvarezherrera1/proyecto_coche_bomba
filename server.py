from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
import crud_clientes
import json

crud_clientes = crud_clientes.crud_clientes()
port = 3000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmclientes":
            self.path = "clientes.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmbusqueda_clientes":
            self.path = "busqueda_clientes.html"
            return SimpleHTTPRequestHandler.do_GET(self)
       
        if self.path=="/clientes":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(crud_clientes.consultar_clientes()).encode('utf-8'))

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        datos= self.rfile.read(longitud)
        datos = datos.decode()
        datos = parse.unquote(datos)
        datos = json.loads(datos)
        if self.path=="/clientes":
            resp = {"msg": crud_clientes.administrar(datos)}
        if self.path=="/buscar_clientes":
            resp = crud_clientes.consultar_clientes(datos)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())
        
print("Ejecuntando server en puerto ", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()