#!/usr/bin/python2
import os

def main():
    root_dir = os.listdir('.')
    #print(root_dir)
    if 'out' not in root_dir:
        print('No out dir, Please check whether in android root dir or make successfully')
        return
    item = raw_input('Please select push item:\n1. Settings.apk\n2. framework.jar\n3. framework-res.apk\n4. services.jar\nItem split with space, [eg: 1 2 3 4] defaul push Settings.apk: ')
    print(item)
    item_list = item.split(' ')
    switcher = {
            '1':push_settings,
            '2':push_framework,
            '3':push_framework_res,
            '4':push_services
            }
    for item in item_list:
        func = switcher.get(item, push_settings)
        func()

def push_settings():
    product = get_product_name()
    push_cmd = 'adb push out/target/product/%s/system/priv-app/Settings/Settings.apk \
/system/priv-app/Settings/'%(get_product_name())
    print(push_cmd)
    res = os.popen(push_cmd)
    print(res.read())

def push_framework():
    push_cmd = 'adb push out/target/product/%s/system/framework/framework.jar \
/system/framework/'%(get_product_name())
    print(push_cmd)
    res = os.popen(push_cmd)
    print(res.read())

def push_framework_res():
    push_cmd = 'adb push out/target/product/%s/system/framework/framework-res.apk \
/system/framework/'%(get_product_name())

    print(push_cmd)
    res = os.popen(push_cmd)
    print(res.read())

def push_services():
    push_cmd = 'adb push out/target/product/%s/system/framework/services.jar \
/system/framework/'%(get_product_name())
    print(push_cmd)
    res = os.popen(push_cmd)
    print(res.read())

def get_product_name():
    dir_list = os.listdir('./out/target/product/')
    #print(dir_list[0])
    return dir_list[0]

if __name__ == '__main__':
    main()
