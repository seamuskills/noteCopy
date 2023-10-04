# Note Copy

This program is intended for use when reading an article to copy important things down, or if you want to get info from multiple places on a page without switching windows or tabs

I would give a warning about using this for plagiarism, but you can't do anything with this that copying couldn't aready do

## how to use
Install the packages "keyboard", "pyler", and "pyperclip"  (preferably in a virtual environment)
Run the command: python main.py

Once the program is running, copying anything to clipboard via ctrl+v will commit it to a file
You can press ctrl+v at any time to end it or press any key in the console.
if the program crashes, or you end it unnaturally, don't worry. Changes are committed per ctrl+c press, so changes are saved.

## command line args

-path [file path]  
This makes the program commit the text to the specified path
If this isn't present, the program makes a file called notes.txt

-notif
Gives a system notification for a successful copy and a duplicate copy.

-nodupe  
When this is present, the program will not commit the text to file if it is the same as the previous text copied. This prevents immediate duplicates.
