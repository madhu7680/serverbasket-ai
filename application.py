import os
import subprocess

port = int(os.environ.get("PORT", 8000))

subprocess.Popen([
    "streamlit", "run", "app.py",
    "--server.port", str(port),
    "--server.address", "0.0.0.0"
])

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Streamlit app is running"]