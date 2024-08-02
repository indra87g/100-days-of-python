"""
Day 6 - Python Web App
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from string import Template


class MyHandler(BaseHTTPRequestHandler):
    routes = {
        "/": "home",
        "/about": "about",
    }

    def do_GET(self):
        if self.path in self.routes:
            getattr(self, self.routes[self.path])()
        else:
            self.not_found()

    def render(self, template_name, context):
        with open(template_name, "r") as f:
            template = Template(f.read())
        return template.substitute(context)

    def home(self):
        context = {"title": "Home", "content": "Hello World!"}
        response = self.render("index.html", context)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())

    def about(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<!DOCTYPE html><html><head><title>About</title></head><body><h1>About Us</h1></body></html>"
        )

    def not_found(self):
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<!DOCTYPE html><html><head><title>404</title></head><body><h1>Page not found</h1></body></html>"
        )


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
