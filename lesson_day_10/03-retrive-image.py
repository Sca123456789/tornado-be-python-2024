import ssl
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

img = urlopen('http://httpbin.org/image/png', context=ctx).read()
fhand = open('sample.png', 'wb')
fhand.write(img)
fhand.close()