import http.server
import socketserver

PORT = 80  # 端口号
Handler = http.server.SimpleHTTPRequestHandler

# 创建一个 HTTP 服务器，并且监听指定的端口
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("在端口", PORT, "启动 HTTP 服务器...")
    # 运行 HTTP 服务器，直到按下 Ctrl-C 停止
    httpd.serve_forever()