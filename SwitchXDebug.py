debug_text = '\n\nzend_extension="php_xdebug-2.7.1-7.2-vc15-x86_64.dll"\n\n' + \
                '[XDebug]\nxdebug.remote_enable = 1\nxdebug.remote_autostart = 1'


if __name__ == '__main__':
    with open("php.ini", "r") as php_ini:
        text = php_ini.read()

    if text[-28:] == "\nxdebug.remote_autostart = 1":
        text = text.replace(debug_text, "")
        flag = "Off"
    else:
        text += debug_text
        flag = "On"

    with open("php.ini", "w") as php_ini:
        php_ini.write(text)

    print("XDebug is " + flag + " now!")
