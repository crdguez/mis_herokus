import os

# Para local:
#PORT = '9000'

#Para heroku
PORT = os.environ['PORT']


os.system('python -m SimpleHTTPServer ' + PORT)
