import base64
from PIL import Image
from pprint import pprint
import binascii


def bintoString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

def tyler_approach(blue_pixels):
    bin_list = []
    for i in range(0, len(blue_pixels), 8): # 8 bits in a byte!
        bin_list.append(blue_pixels[i:i+8])
    message = ""
    for binary_value in bin_list:
        binary_integer = int(binary_value, 2) # Convert the binary value to base2
        ascii_character = chr(binary_integer) # Convert integer to ascii value
        if ascii_character == '\x00':
            print('reached break')
            #break
        message += ascii_character
    return message

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

def frombits(bits):
    chars = []
    intbits = int(len(bits)/ 8)
    for b in range(intbits):
        byte = bits[b*8:(b+1)*8]
        char_value = chr(int(''.join([str(bit) for bit in byte]), 2))
        #print(char_value)
        if char_value == '\x00':
            print('reached break')
            #break
        #chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        chars.append(char_value)
    return ''.join(chars)

def decode5():
    img = "7fe3c3f6-Stego.PNG"
    image = Image.open(img, 'r')
    pixels = list(image.getdata())
    lsb_blue_char = ''
    lsb_message = ''
    for pixel_height in range(image.height):
        print('pixel_height: ', pixel_height)
        for pixel_width in range(image.width):
            rgba_pixel = image.getpixel((pixel_width, pixel_height))
            lsb_blue_char = str(rgba_pixel[2] & 1) + lsb_blue_char
            if lsb_blue_char == '00000000':
                print('reached return: ')
                return lsb_message
            #print(lsb_blue_char)
            if len(lsb_blue_char) == 8:
                lsb_message += chr(int(lsb_blue_char, 2))
                lsb_blue_char = ''
    """for RGB in pixels:
        for index, color in enumerate(RGB):
            if index != 2:
                continue
            lsb_blue_char += bin(color & 1) + lsb_blue_char
        if lsb_blue_char == '00000000':
            print('reached return: ')
            return lsb_message
        #print(lsb_blue_char)
        if len(lsb_blue_char) == 8:
            lsb_message += chr(int(lsb_blue_char, 2))
            lsb_blue_char = ''
    """
    return lsb_message
 
def decode4():
    img = "7fe3c3f6-Stego.PNG"
    image = Image.open(img, 'r')
    #pixels = list(image.getdata())
    blue_pixels_array = []
    
    for pixel_heigt in range(image.height):
        
        rgb_of_pixel = image.getpixel((pixel_heigt, 0))
        for index, color in enumerate(rgb_of_pixel):
            if index == 2:
                color = color & 1
                blue_pixels_array.append(color)
                
    #print(first_blue_pixels_only)
    
    print(blue_pixels_array)
    #return bits2string(bin(int(first_blue_pixels_only)))
    return frombits(blue_pixels_array)


def decode3():
    img = "7fe3c3f6-Stego.PNG"
    image = Image.open(img, 'r')
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    blue_pixels_only = ''
    for pixelarr in pixels:
        for pixel_rgb in pixelarr:
            for index, color in enumerate(pixel_rgb):
                if index != 2:
                    continue
                lsb_blue = color & 1
                blue_pixels_only += str(lsb_blue)
    
    return tyler_approach(blue_pixels_only)

def decode2():
    img = "7fe3c3f6-Stego.PNG"
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
        # string of binary data
        binstr = ''
        print('pixels 8: ', pixels[:8], ' len: ', len(pixels[:8]))
        index = 0
        for i in pixels[:8]:
            index += 1
            if index % 3 != 0:
                continue
            #print('index: ', index)
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        print('binstr: ', binstr)
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

def decode():
    img = "7fe3c3f6-Stego.PNG"
    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binstr = ''
        print('pixels 8: ', pixels[:8], ' len: ', len(pixels[:8]))
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        print('binstr: ', binstr)
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data


if __name__ == '__main__' :
    #data = decode()
    #pprint(data)
    #data = decode2()
    #pprint(data)
    #data = decode3()
    #print(data)
    #data = decode4()
    #print(data)
    data = decode5()
    print(data)
