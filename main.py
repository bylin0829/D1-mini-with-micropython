import os, sdcard, machine

# D1 mini pin definition
# MISO  = D6 = GPIO 12
# MOSI  = D7 = GPIO 13
# SCK   = D5 = GPIO 14
# CS    = D8 = GPIO 15

def test1():
    sd = sdcard.SDCard(machine.SPI(1), machine.Pin(15))
    os.mount(sd, '/sd')
    print('File list: {files}'.format(files=os.listdir('/sd')))
    try:
        with open('/sd/myfile.txt', 'w') as f:
            f.write('Hello world\r\n')
    except:
        print('open file failure')
    
    os.umount('/sd')

def test2():
    spisd = machine.SoftSPI(-1,miso=machine.Pin(12),mosi=machine.Pin(13),sck=machine.Pin(14))
    sd = sdcard.SDCard(spisd, machine.Pin(15))
    vfs = os.VfsFat(sd)
    os.mount(vfs, '/sd')
    print('File list: {files}'.format(files=os.listdir('/sd')))
    print('ss1')
    with open('/sd/myfile.txt', 'w') as f:
        f.write('Hello world\r\n')
        print('ss2')
    os.umount(vfs)
    
if __name__ == '__main__':
    test1()