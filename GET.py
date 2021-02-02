'''This python file handles the inport given into the web browser to a form. It gets the location value from the web form and returns the address of the same'''

import requests
import cgi
import cgitb

form = cgi.FieldStorage() 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = form.getvalue('location')
PARAMS = {'address':location} 
req = requests.get(url = URL, params = PARAMS) 
sol = req.json() 
f_address = sol['results'][0]['formatted_address'] 
print "<html>"
print "<body>"
print "<h2>Address: %s </h2>" % (f_address)
print "</body>"
print "</html>"
