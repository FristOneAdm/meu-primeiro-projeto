import http.server
import socketserver
import webbrowser

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Abre automaticamente a página no seu navegador padrão
webbrowser.open(f"http://localhost:{PORT}")

print(f"Servidor rodando em: http://localhost:{PORT}")
print("Para desligar o servidor, pressione: CTRL + C")

# Inicializa o servidor web na porta 8000
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado com sucesso.")
