import socket
import ssl

scheme_2_port = {"http": 80, "https": 443}

class URL:

    def __init__(self, url):
        self.url = url
        self.scheme = ""
        self.hostname = ""
        self.path = ""
        self.port = 0

    def parse_url(self):
        """
        Parses a URL into its various components.
        """
        self.scheme, url = self.url.split("://", 1)
        if self.scheme in scheme_2_port:
            self.port = int(scheme_2_port[self.scheme])
        else:
            print("This scheme is not supported by this web browser.")
        if "/" not in url:
            url += "/"
        self.hostname, self.path = url.split("/", 1)
        self.path = "/" + self.path
        if ":" in self.hostname:
            self.hostname, port = self.hostname.split(":", 1)
            self.port = int(port)

        # TESTING 
        print("Scheme: ", self.scheme)
        print("Hostname: ", self.hostname)
        print("Path: ", self.path)
        print("Port: ", self.port)
        print()

    def req(self):
        """
        Requests a web page and downloads it.
        """
        # Create socket and send request
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        sock.connect((self.hostname, 80))
        if self.scheme == "https":
            ctx = ssl.create_default_context()
            sock = ctx.wrap_socket(s, server_hostname=self.hostname)
        req = f"GET {self.path} HTTP/1.0\r\nHost: {self.hostname}\r\n\r\n".encode("utf8")
        sock.send(req)

        # Receive and interpret response
        resp = sock.makefile(mode="r", encoding="utf8", newline="\r\n")
        status_line = resp.readline()
        http_version, status_code, reason_phrase = status_line.split(" ", 2)
        resp_headers = {}
        line = resp.readline()
        while line != "\r\n":
            header, value = line.split(":", 1)
            resp_headers[header] = value.strip()
            line = resp.readline()
        assert "Transfer-Encoding" not in resp_headers
        assert "Content-Encoding" not in resp_headers
        body = resp.read()
        
        sock.close()

        # TESTING
        print("HTTP Version: ", http_version)
        print("Status Code: ", status_code)
        print("Reason Phrase: ", reason_phrase)
        print("Headers: ", resp_headers)
        # print("Body: ", body)

        return resp_headers, body

