"""
Local development server for the portfolio site.

This project itself is plain HTML/CSS/JS (that's what GitHub Pages can
host), but you can run and preview it from PyCharm with this script —
just right-click serve.py and choose "Run".

Usage:
    python serve.py            # serves on http://localhost:8000
    python serve.py 8080       # serves on a custom port
"""

import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = Path(__file__).parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)


def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"Serving {ROOT} at {url}  (Ctrl+C to stop)")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
