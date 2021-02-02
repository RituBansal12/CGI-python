'''This python program gets 2 numbers from the web browser form and returns the result of addition,subtraction,multiplication and division being performed on them'''

import cgi
import cgitb

form = cgi.FieldStorage() 

num_1 = form.getvalue('num_1')
num_2  = form.getvalue('num_2')
n1= int(num_1)
n2= int(num_2)
sum = n1 + n2
sub= n1 - n2
Mul= n1* n2
div= n1/n2

print "<html>"
print "<head>"
print "<title>MATH OPERATIONS</title>"
print "</head>"
print "<body>"
print "<h2>SUM %d</h2>" % (sum)
print "<h2>MINUS %d</h2>" % (sub)
print "<h2>PRODUCT %d</h2>" % (Mul)
print "<h2>DIVISION %d</h2>" % (div)
print "</body>"
print "</html>"
