
#Importing Pillow that will help us for making sure the image is correct
from PIL import Image


#We set the key that we've found
hexKey = 'fallen'

#bytearray returns an array of bytes. (right here, we get from ch3.bmp that we read)
cypher = bytearray(open("ch3.bmp", "rb").read())

for i in range(len(cypher)):
    #We decode with a xor the new image
    cypher[i] ^= ord(hexKey[i%len(hexKey)])

#We set it in a new file
open("decrypted.bmp","wb").write(cypher)
try:
    ch = Image.open("decrypted.bmp")
    #We verify the file
    ch.verify()
except IOError:
    print("The image couldn't be proceeded")
else:
    print('The image has been treated correctly')