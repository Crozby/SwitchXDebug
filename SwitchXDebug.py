debug_text = '\n\nzend_extension="php_xdebug-2.7.1-7.2-vc15-x86_64.dll"\n\n' + \
                '[XDebug]\nxdebug.remote_enable = 1\nxdebug.remote_autostart = 1'


if __name__ == '__main__':
    php_ini = open("php.ini", "r")
    text = php_ini.read()
    php_ini.close()
    if text[-28:] == "\nxdebug.remote_autostart = 1":
        text = text.replace(debug_text, "")
        flag = "Off"
    else:
        text += debug_text
        flag = "On"

    php_ini = open("php.ini", "w")
    php_ini.write(text)
    print("XDebug is " + flag + " now!")
