from pynput import keyboard

keys = {}

def writeLog(keyStr):
    path = 'kbr.log'
    file = open(path, 'a+')
    file.write(keyStr)
    file.close()

def press(key):
    if keys.get(key) != True:
        keys[key] = True
        keyStr = ('[{0} p]'.format(str(key).replace('\'', '').replace('Key.', '')))
        print(keyStr)
        writeLog(keyStr)

def release(key):
    if keys.get(key, False) != False:
        keys[key] = False
        keyStr = ('[{0} r]'.format(str(key).replace('\'', '').replace('Key.', '')))
        print(keyStr)
        writeLog(keyStr)

with keyboard.Listener(on_press = press, on_release = release) as listener:
    listener.join()