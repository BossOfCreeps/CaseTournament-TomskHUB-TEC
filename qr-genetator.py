import pyqrcode, png, sys

'''
big_code = pyqrcode.create('0987654321')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()
'''
d = pyqrcode.decode()
if d.decode('code.png'):
    print ('result: ' + d.result)
else:
    print ('error: ' + d.error)
