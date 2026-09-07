#!/usr/bin/env python3
"""Dashboard server with caching disabled.

`python3 -m http.server` sends Last-Modified, so browsers happily serve the
previous features_derived.json from cache after a regenerate — the dashboard
then shows stale counts even though the files on disk are current. This sends
no-store on every response so a normal refresh always picks up new data.
"""
import http.server
import os
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # keep the log quiet; errors still surface on stderr


class ReusableServer(socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    with ReusableServer(("", PORT), NoCacheHandler) as httpd:
        print(f"ARC dashboard (no-cache) on http://localhost:{PORT}/index.html")
        httpd.serve_forever()
