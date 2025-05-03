# Project 7 QR Code Generator In Python
# install this command on terminal : pip install qrcode

import qrcode
data = 'QR Code using make() function'
img = qrcode.make(data)
img.save('qrcode project 7.png')
