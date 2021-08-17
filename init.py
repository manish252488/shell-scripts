import http.server
import socketserver
import webbrowser
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
print('http://localhost:'+ str(PORT))
webbrowser.open('http://localhost:'+ str(PORT), new=2)
httpd.serve_forever()
