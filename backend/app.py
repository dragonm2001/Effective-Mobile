#!/usr/bin/env python3
"""
Простой HTTP-бэкенд для тестового задания Effective Mobile.
Поднимает сервер на порту 8080 и отвечает на GET / текстом.
"""

import http.server
import os
import signal
import sys


class BackendHandler(http.server.BaseHTTPRequestHandler):
    """Обработчик запросов"""

    def do_GET(self):  
        if self.path == "/":
            body = b"Hello from Effective Mobile!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404, "Not Found")

    def do_HEAD(self):  
        # HEAD нужен для healthcheck
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
        else:
            self.send_error(404, "Not Found")

    def log_message(self, fmt, *args):
        sys.stdout.write(f"[backend] {self.address_string()} - {fmt % args}\n")
        sys.stdout.flush()


def graceful_shutdown(signum, frame):
    print(f"\n[backend] получен сигнал {signum}, завершаем работу...", flush=True)
    sys.exit(0)


def main():
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))

    signal.signal(signal.SIGTERM, graceful_shutdown)
    signal.signal(signal.SIGINT, graceful_shutdown)

    server = http.server.HTTPServer((host, port), BackendHandler)
    print(f"[backend] слушаем на {host}:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
