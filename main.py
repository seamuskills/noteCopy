##module checking code py slick9000
import os, sys

python = 'python3'

if 'win' in sys.platform:
    python = 'python'

print('[*] Checking dependencies...')

while True:

    try:

        import keyboard, pyperclip, time, notifypy

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
            note = notifypy.Notify()
        case "-nodupe":
            nodupe = True

print("began listening and writing to path: " + f)

def copyDown():
    global previous

    t = 0
    text = pyperclip.paste()
    while t < 100 or text == previous:
        text = pyperclip.paste()
        time.sleep(0.01)
        t += 1
    time.sleep(0.01)
    if notif:
        if text != previous:
            note.title="noteCopy | success"
            note.message = "copied: " + text
            note.send()
        else:
            note.title = "noteCopy | dupe"
            note.message = "duplicate copy detected"
            note.send()
    if nodupe and text == previous:
        return
    with open(f, "a") as file:
        file.write(text)
        file.write("\n" * 2)
    previous = text


keyboard.add_hotkey("ctrl+c", copyDown)

input("press any key to stop the program\n")