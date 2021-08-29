# D1-mini-with-micropython

## Upload Micropython Firmware

1. [Download flash](https://micropython.org/download/) for your device.  I download esp8266 firmware called by "esp8266-20210618-v1.16.bin".

2. Download esptool
```
pip install esptool
```

3. Erase flash by esptool.  My device is connected to COM4.
``` 
esptool.py --port COM4 erase_flash
```

4. Upload firmware

```
esptool.py --port COM4 --baud 115200 write_flash  -fm dio --flash_size 4MB 0 esp8266-20210618-v1.16.bin
```
