import os

def main():
    root_dir = os.listdir('.')
    if 'out' not in root_dir:
        print('No out dir, Please check whether in android root dir or make successfully')
        return
    item  = raw_input('Please select img need to flash:\n 1. boot.img 2. system.img \n Item split with space,[eg:1 2] default flash boot.img: ')
    print(item)
    pre_flash()
    item_list = item.split(' ')
    switcher = {
            '1':flash_boot,
            '2':flash_system
            }
    for item in item_list:
        func = switcher.get(item, flash_boot)
        func()
    res = os.popen('fastboot reboot')


def pre_flash():
    reboot_cmd = 'adb reboot bootloader'
    go_unlock = 'fastboot oem unlock-go'
    tinno_unlock = 'fastboot oem unlock-tinno'
    print(os.popen(reboot_cmd).read())
    print(os.popen(go_unlock).read())
    print(os.popen(tinno_unlock).read())

def flash_boot():
    flash_cmd = 'fastboot  -S 100M flash boot out/target/product/%s/boot.img'%(get_product_name())
    print(flash_cmd)
    res = os.popen(flash_cmd)
    print(res.read())

def flash_system():
    flash_cmd = 'fastboot  -S 100M flash system out/target/product/%s/system.img'%(get_product_name())
    print(flash_cmd)
    res = os.popen(flash_cmd)
    print(res.read())

def get_product_name():
    dir_list = os.listdir('./out/target/product/')
    #print(dir_list[0])
    return dir_list[0]
 
if __name__ == '__main__':
    main()
