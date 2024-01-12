# import socket
# url = input("Enter a URL in the format 'http://hostname/path': ")
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# hostname = url.split('/')[2].split(':')[0]
# path = '/' + url.split('/')[3] if len(url.split('/')) > 4 else '/'
# mysock.connect((hostname, 80))
# cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(path).encode()
# mysock.send(cmd)
# while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#     break
#    print(data.decode(),end='')
# mysock.close()




# from urllib.request import urlopen
# try:
#     url = input("Insert your URL: ")
#     data = urlopen(url).read()
#     print(data)
# except Exception as e:
#     print(f"An error accured: {e}")


