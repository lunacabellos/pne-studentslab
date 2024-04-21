import http.server
import socketserver
import termcolor
from pathlib import Path


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Generating the response message
        if self.path == "/":
            contents = Path("html/form-e2.html").read_text()
            self.send_response(200)
        elif self.path.endswith("&chk=on"):
            message = self.path[1:]
            msg = message[message.find("=") + 1: message.find("&")].upper()
            contents = Path("html/form-e1.html").read_text().format(msg)
            self.send_response(200)
        elif self.path.startswith("/myserver?msg=") and self.path.count("=") == 1:
            message = self.path[1:]
            msg = message[message.find("=") + 1:]
            contents = Path("html/form-e1.html").read_text().format(msg)
            self.send_response(200)
        else:
            contents = Path("html/error.html").read_text()
            self.send_response(404)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()