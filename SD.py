import os, sdcard, machine

class SD:
    def __init__(self, spi=1, cs=15):
        self.spi = spi
        self.cs = cs
        self.sd_root_path = '/sd'
        sd = sdcard.SDCard(machine.SPI(self.spi), machine.Pin(self.cs))
        try:
            os.mount(sd, self.sd_root_path)
        except:
            pass
        
    def __del__(self):
        try:
            os.umount(self.sd_root_path)
        except:
            pass
        
    def Path(self, *args):
        mypath = self.sd_root_path
        for i in args:
            i = str(i).replace('\\', '').replace('/','')
            mypath += ('/' + str(i))
        return mypath
    
    def FileList(self):
        print(os.listdir(self.sd_root_path))
    
    def Write(self, file_absolute_path, data, mode='a'):
        try:
            with open(file_absolute_path, mode) as f:
                f.write(data)
        except:
            print('open file failure')

    def Read(self, file_relative_path):
        pass