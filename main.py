import SD

# D1 mini pin definition
# MISO  = D6 = GPIO 12
# MOSI  = D7 = GPIO 13
# SCK   = D5 = GPIO 14
# CS    = D8 = GPIO 15


    
if __name__ == '__main__':
    mysd = SD.SD()
    #mysd.FileList()
    for i in range(5):
        mysd.Write(mysd.Path('b.txt'), 'Test my SD card\r\n', 'a')
    