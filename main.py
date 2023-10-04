##module checking code py slick9000
import os, sys

python = 'python3'

if 'win' in sys.platform:
    python = 'python'

print('[*] Checking dependencies...')

while True:

    try:

        import keyboard, pyperclip, time
        from plyer import notification

        break

    except ModuleNotFoundError as e:

        module = str(e)[17:-1]

        print(f'[*] Installing {module} module for python')

        try:

            if os.system(f'{python} -m pip install {module}') != 0:
                raise ModuleNotFoundError

        except ModuleNotFoundError:

            print(f'[!] Error installing "{module}" module. Do you have pip installed?')

            input(f'[!] Failed. Press any key to exit...')

            sys.exit()

previous = ""
f = "notes.txt"
nodupe = False
notif = False

for i in sys.argv:
    if i[0] != "-":
        continue
    match i:
        case "-path":
            f = sys.argv[sys.argv.index(i)+1]
        case "-notif":
            notif = True
        case "-nodupe":
            nodupe = True

print("began listening and writing to path: " + f)

def copyDown():
    time.sleep(0.01)
    global previous
    text = pyperclip.paste()
    if notif:
        if text != previous:
            notification.notify(title="noteCopy | success", message="copied: " + text, timeout=1)
        else:
            notification.notify(title="noteCopy | dupe", message="duplicate copy detected", timeout=1)
    if nodupe and text == previous:
        return
    with open(f, "a") as file:
        file.write(text)
        file.write("\n" * 2)
    previous = text


keyboard.add_hotkey("ctrl+c", copyDown)

input("press any key to stop the program\n")