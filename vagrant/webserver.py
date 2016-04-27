from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        greeting = ""
        output = ""

        try:
            if self.path.endswith("/hello"):
                greeting = "<h1>Hello!</h1>"

            if self.path.endswith("/hola"):
                greeting = "<h1>&#161Hola!</h1>"

            output += "<html><body>"
            output += greeting
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"></form>'''
            output += "</body></html>"

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(output)
            # print output
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                msg_content = fields.get('message')

            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % msg_content[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"></form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        print "Web Server running on port 2201, if Vagrant port collision"
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
