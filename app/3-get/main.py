from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>"""

def application(environ, start_response):

    d = parse_qs(environ['QUERY_STRING'])

    age = d.get('age', [''])[0] # Returns the first age value.
    hobbies = d.get('hobbies', []) # Returns a list of hobbies.

    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % (age or 'Empty',
               ', '.join(hobbies or ['No Hobbies']))

    status = '200 OK'

    # Now content type is text/html
    response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]
