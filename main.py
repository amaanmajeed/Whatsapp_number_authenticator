from time import sleep
import pyautogui


def format_txt(message):
    message = message.replace(' ', '%20')
    return message


def check_number(number):
    if len(number) != 12 or number[:3] != '923':
        return 'Number invalid'
    else:
        return number


def get_number(number):
    if number[0] == "9" and number[1] == "2":
        return check_number(number)
    elif number[0] == '0':
        number = '92' + number[1:]
        return check_number(number)
    else:
        return check_number(number)


# what_api = 'https://wa.me/919988776655?text=How%20are%20you'


text = 'Atomated message from Amaan, Ignore this message'
number = '03214278600'


def operate(numbe, mess):
    try:
        if int(get_number(numbe)) % 1 == 0:
            txt = 'https://wa.me/{}?text={}'.format(
                get_number(numbe), format_txt(mess))
            sleep(3)
            pyautogui.write(txt)
            sleep(4)
            pyautogui.hotkey('enter')
            sleep(1)
        else:
            print('Number Not Correct')
    except Exception as e:
        pass
        print(str(e))


msg = 'Automated message from Amaan, Ignore this message'
numb = '03214278600'


pyautogui.hotkey('win', '6')  # open whatsapp
pyautogui.hotkey('enter')
sleep(3)
pyautogui.write('win', '5')  # open chrome
pyautogui.hotkey('enter')
sleep(9)

count = 0
ran = 2
for c in range(ran):
    if count == 0:
        pyautogui.hotkey('win', '5')
        operate(numb, msg)
        print(count)
        count += 1
    else:
        pyautogui.hotkey('win', '5')
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 'shift', 'tab')
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('ctrl', 'l')
        operate('03074278600', msg)
        print(count)
        count += 1
