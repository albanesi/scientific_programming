import time
import sys
from pystrich.qrcode import QRCodeEncoder

# Creates QR-Code based on text input
encoder = QRCodeEncoder("Docker ist cool!")
encoder.save( "./QRCode_test.png" )

# Prints ASCII-version of the QR-Code
print(encoder.get_ascii())
print('Container is running, use another VS Code terminal!')
sys.stdout.flush()

# Prevents the container from stopping
while True:
    time.sleep(1)