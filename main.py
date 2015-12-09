#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

html = """\
<html>
  <head>
  <style>
body {background-color:lightgrey}
h1   {color:blue}
</style>
</head>
  <body>
 
       <img src="http://weknowyourdreams.com/images/arbol/arbol-01.jpg"/>
	   <br></br><h1>Hello world!</h1>
    
  </body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)
 

		

class HolaHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hola mundo!')		

 
 
		
class KaixoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Kaixo mundua!')
		

	
		
app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/hola', HolaHandler),
	('/kaixo', KaixoHandler),

], debug=True)
