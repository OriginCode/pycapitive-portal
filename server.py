from wsgiref.simple_server import make_server

PORT = 8000 # Default Port

def captive_portal(environ, responce):
    responce('204 No Content', [('Content-Type', 'text/html')])
    return [b'<h1>OriginCode\'s Google Capitive Portal (204).']

httpd = make_server('', PORT, captive_portal)
print('Started serving on port %d...' % PORT)
httpd.serve_forever()
