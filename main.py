import webapp2
import json
from contacts import *

class Home(webapp2.RequestHandler):
    def get(self):
        INDEX_HTML = open('index.html').read()
        self.response.write(INDEX_HTML)

class FormatContactNameRoute(webapp2.RequestHandler):
    def post(self):
        first = self.request.POST.get("first")
        last = self.request.POST.get("last")
        if(IsValidContactName(first, last)):
            formattedName = FormatContactName(first, last)
            self.response.write(unicode('Success! ' + first + ' and ' + last + ' are both valid! The formatted name is: ' + formattedName))
        else:
            self.response.write('Failure! Either ' + first + ' or ' + last + ' is invalid!')

app = webapp2.WSGIApplication([
    ('/', Home),
    ('/FormatContactNameRoute', FormatContactNameRoute),
], debug=True)

# To run local server do python main.py
def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')
if __name__ == '__main__':
    main()
