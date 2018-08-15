from wsgiref.simple_server import make_server

def captive_portal(environ, responce):
    responce('204 No Content', [('Content-Type', 'text/html')])
    return [b'<h1>OriginCode\'s Google Capitive Portal (204).']

httpd = make_server('', 8000, captive_portal)
print('Started serving on port 8000...')
httpd.serve_forever()
