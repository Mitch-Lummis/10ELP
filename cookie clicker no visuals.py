import threading
from pynput import keyboard
import time
grandmas = 0
numberCookies = 0
grandmaCookies = 0
clickerLevel = 1
upgradeCost = 10
gameContinue = True
grandmas = int(grandmas)
numberCookies = int(numberCookies)
clickerLevel = int(clickerLevel)
grandmaCookies = int(grandmaCookies)
upgradeCost = int(upgradeCost)

def infiniteloop1():
    global numberCookies
    global grandmas
    global grandmaCookies
    global time
    while True:
        numberCookies = int(numberCookies)
        grandmas = int(grandmas)
        grandmaCookies = int(grandmaCookies)
        grandmaCookies = grandmaCookies + grandmas
        time.sleep(10)

def infiniteloop2():
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

def on_press(key):
    try:
        '''print('Alphanumeric key pressed: {0} '.format(
            key.char))'''
        global grandmas
        global numberCookies
        global clickerLevel
        global grandmaCookies
        global time
        global upgradeCost
        if key.char == 'g':
            grandmas = grandmas +1
            numberCookies = numberCookies -10
            grandmas = str(grandmas)
            print('''Number of grandma's is: ''' + grandmas)
            grandmas = int(grandmas)
        if key.char == 'u':
            clickerLevel = clickerLevel *2         
            numberCookies = numberCookies - upgradeCost
            clickerLevel = int(clickerLevel)
            upgradeCost = upgradeCost + upgradeCost + clickerLevel
            clickerLevel = str(clickerLevel)
            print('Clicker Level is: ' + clickerLevel)
            upgradeCost = str(upgradeCost)
            print('New price to upgrade clicker is:  ' + upgradeCost)
            upgradeCost = int(upgradeCost)
            clickerLevel = int(clickerLevel)
        if key.char == 'm':
            grandmaCookies = str(grandmaCookies)
            print('''Grandma's have currently baked you ''' + grandmaCookies + ' cookies.')
            time.sleep(1)
            grandmaCookies = int(grandmaCookies)
            numberCookies = numberCookies + grandmaCookies
            numberCookies = str(numberCookies)
            grandmaCookies = 0
            print('Number of cookies is: ' + numberCookies)
            numberCookies = int(numberCookies)
        if key.char == 'h':
            print('''Key 'c' to get more cookies ''')
            grandmas = str(grandmas)
            print('''Key 'g' to buy a grandma. You currently have: ''' + grandmas)
            grandmas = int(grandmas)
            upgradeCost = str(upgradeCost)
            clickerLevel = str(clickerLevel)
            print('''Key 'u' to upgrade clicker. Currently ''' + upgradeCost + ' cookies to upgrade. Current level is: ' + clickerLevel)
            upgradeCost = int(upgradeCost)
            clickerLevel = int(clickerLevel)
            print('''Key 'm' to see how many cookies grandma's have baked and claim them''')
            print('''Key 'h' if you forget controls and need help''')
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    global grandmas
    global numberCookies
    global clickerLevel
    '''print('Key released: {0}'.format(
        key))'''
    if key.char == 'c':
        numberCookies = numberCookies + clickerLevel
        numberCookies = str(numberCookies)
        print('Number of cookies is: ' + numberCookies)
        numberCookies = int(numberCookies)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

print('''press key 'h' for controls''')

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()