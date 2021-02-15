import socket, sys
look = False
port = 1000
buffer = 'HTTP/1.1 200 OK\r\n'
buffer += 'Content-Type: text/html; charset=utf-8\r\n\r\n'
buffer += '<script>alert(\'Hello dude!\');</script>'
help = '''Simple TCP Server with HTTP response

Usage:
-h, --help -> Show this help
-s, --show-recv -> Enable data looking
-p, --port -> Sets the port listening
-a, --about -> Show info about this program
'''
about = '''Created by John
Aprendendo melhor sobre a camada de transporte TCP

O HTTP usa o protocolo TCP para transmissão de dados,
e com esse simples script é possível saber mais sobre o que acontece
nos bastidores de um servidor web, por exemplo :)
'''
for k in sys.argv:
	if k in ('-h', '--help'):
		exit(help)
	elif k in ('-s', '--show-recv'):
		look = True
	elif k in ('-p', '--port'):
		try:
			port = sys.argv[sys.argv.index(k) + 1]
		except IndexError:
			exit('%s needs a value. Use -h/--help to show help.'%k)
	elif k in ('-a', '--about'):
		exit(about)
s = socket.socket()
try:
	s.bind(('0.0.0.0', int(port)))
except Exception as e:
	exit(e)
s.listen(5)
print('Now is listening on port %s'%port)
try:
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		print('%s:%d -> %d bytes'%(addr[0], addr[1], len(data)))
		if look:
			print(data.decode(**{'errors': 'ignore'}))
		print('\rSending buffer to client...', end = '')
		conn.send(buffer.encode())
		print('\rSending buffer to client... Done.')
		print('Closing connection.', end = '\n\n')
		conn.close()
except KeyboardInterrupt:
	print('Exiting.')