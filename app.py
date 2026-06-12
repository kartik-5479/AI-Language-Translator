from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import functools
import webbrowser

PORT = 8000
ROOT = Path(__file__).resolve().parent


def main():
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    url = f"http://127.0.0.1:{PORT}/"
    print(f"LinguaLift AI Translator is running at {url}")
    print("Press Ctrl+C to stop the server.")
    webbrowser.open(url)
    server.serve_forever()


if __name__ == "__main__":
    main()
