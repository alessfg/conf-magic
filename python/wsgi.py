import os
import datetime
def application(environ, start_response):
    output = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    output += "\n\nENV Variables:\n\n"
    for param in os.environ.keys():
         output += param
         output += "\t"
         output += os.environ[param]
         output += "\n"
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [output]
