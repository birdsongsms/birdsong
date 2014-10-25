import webapp2
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, Ben Parish! We are building a prototype web app first!')

		
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)