try:
    import keyboard, pyperclip, winsound, time, sys
except:
    print("required packages missing, this program requires keyboard and pyperclip!\nI recommend installing them in a venv.")
    exit()

previous = ""
f = "notes.txt"
nodupe = False
sound = False

for i in sys.argv:
    if i[0] != "-":
        continue
    match i:
        case "-path":
            f = sys.argv[sys.argv.index(i)+1]
        case "-sound":
            sound = True
        case "-nodupe":
            nodupe = True

print("began listening and writing to path: " + f)

def copyDown():
    time.sleep(0.01)
    global previous
    text = pyperclip.paste()
    if text != "" and sound:
        winsound.Beep(600, 250)
    if text == previous:
        if sound:
            winsound.Beep(300, 250)
        if nodupe:
            return
    with open(f, "a") as file:
        file.write(text)
        file.write("\n" * 2)
    previous = text


keyboard.add_hotkey("ctrl+c", copyDown)

input("press any key to stop the program\n")