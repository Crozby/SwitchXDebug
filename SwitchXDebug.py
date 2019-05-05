debug_text = '\n\nzend_extension="php_xdebug-2.7.1-7.2-vc15-x86_64.dll"\n\n' + \
                '[XDebug]\nxdebug.remote_enable = 1\nxdebug.remote_autostart = 1'
path = "D:\\Python\\SwitchXDebug\\tmp\\php.ini"
xdebug = ['zend_extension="php_xdebug', "[XDebug]", "xdebug."]


if __name__ == '__main__':
    with open(path, "r") as php_ini:
        text = php_ini.read()

    if '; zend_extension="php_xdebug' in text:
        for word in xdebug:
            text = text.replace("; " + word, word)
        flag = "On"
    else:
        for word in xdebug:
            text = text.replace(word, "; " + word)
        flag = "Off"

    with open(path, "w") as php_ini:
        php_ini.write(text)

    print("XDebug is " + flag + " now!")
