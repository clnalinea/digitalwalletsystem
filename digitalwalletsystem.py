from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Wallet data
wallet = {"balance": 0.0}

class SimpleWalletHandler(BaseHTTPRequestHandler):
    def _send_response(self, response, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_GET(self):
        if self.path == "/balance":
            self._send_response({"balance": wallet["balance"]})
        else:
            self._send_response({"error": "Invalid endpoint"}, status=404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if self.path == "/cash-in":
            amount = data.get('amount', 0)
            if amount > 0:
                wallet["balance"] += amount
                self._send_response({"message": "Cash-in successful", "new_balance": wallet["balance"]})
            else:
                self._send_response({"error": "Invalid amount"}, status=400)
        elif self.path == "/debit":
            amount = data.get('amount', 0)
            if 0 < amount <= wallet["balance"]:
                wallet["balance"] -= amount
                self._send_response({"message": "Debit successful", "new_balance": wallet["balance"]})
            else:
                self._send_response({"error": "Invalid or insufficient funds"}, status=400)
        else:
            self._send_response({"error": "Invalid endpoint"}, status=404)

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleWalletHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
