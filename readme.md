# Note Copy

This program is intended for use when reading an article to copy important things down, or if you want to get info from multiple places on a page without switching windows or tabs

I would give a warning about using this for plagerism, but you can't do anything with this that copying couldn't aready do

## how to use
Install the packages "keyboard" and "pyperclip"  (preferably in a virtual environment)
Run the command: python main.py

Once the program is running, copying anything to clipboard via ctrl+v will commit it to a file
You can press ctrl+v at any time to end it or press any key in the console.
if the program crashes, or you end it unnaturally, don't worry. Changes are committed per ctrl+c press, so changes are saved.

## command line args

-path [file path]  
This makes the program commit the text to the specified path
If this isn't present, the program makes a file called notes.txt

-sound  
This makes the program beep when it commits something to file and gives a seperate sound for immediate duplicates
This also makes a sound if the program is ended with ctrl+v

-nodupe
When this is present, the program will not commit the text to file if it is the same as the previous text copied. This prevents immediate duplicates.
