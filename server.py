from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
#from webbrowser import open
open = print

open('http://localhost:8080/')
server = ThreadingHTTPServer(('', 8080), SimpleHTTPRequestHandler)
server.serve_forever()
