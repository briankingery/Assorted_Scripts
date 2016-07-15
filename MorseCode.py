import winsound
import time

#dot = winsound.Beep(293, 200) # D
#dash = winsound.Beep(293, 800) # D
delay = 0.1

def decoder():
    message =  raw_input("Please enter your message? ").lower()

    print message

    for letter in message:
        if letter == " ":
            time.sleep(1)
        elif letter == "a":
            print letter
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "b":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 200) # D
            time.sleep(delay)
        elif letter == "c":
           print letter
           winsound.Beep(293, 800) # D
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 800) # D
           winsound.Beep(293, 200) # D
           time.sleep(delay)
        elif letter == "d":
           print letter
           winsound.Beep(293, 800) # D
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 200) # D
           time.sleep(delay)
        elif letter == "e":
            print letter
            winsound.Beep(293, 200) # D
            time.sleep(delay)
        elif letter == "f":
           print letter
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 800) # D
           winsound.Beep(293, 200) # D
           time.sleep(delay)
        elif letter == "g":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            time.sleep(delay)
        elif letter == "h":
           print letter
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 200) # D
           winsound.Beep(293, 200) # D
           time.sleep(delay)
        elif letter == "i":
            print letter
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 200) # D
            time.sleep(delay)
        elif letter == "i":
            print letter
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 200) # D
            time.sleep(delay)
        elif letter == "j":
            print letter
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "k":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "l":
            print letter
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 200) # D 
            time.sleep(delay)
        elif letter == "m":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "n":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D 
            time.sleep(delay)
        elif letter == "o":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "p":
            print letter
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            time.sleep(delay)
        elif letter == "q":
            print letter
            winsound.Beep(293, 800) # D 
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "r":
            print letter
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D 
            time.sleep(delay)
        elif letter == "s":
            print letter
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 200) # D 
            time.sleep(delay)
        elif letter == "t":
            print letter
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "u":
            print letter
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "v":
            print letter
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "w":
            print letter
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)    
        elif letter == "x":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 200) # D 
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "y":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            time.sleep(delay)
        elif letter == "z":
            print letter
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 800) # D
            winsound.Beep(293, 200) # D
            time.sleep(delay)   

    print ("Your message was coded")
    time.sleep(2)
    again = raw_input("Do you want to code another message, y/n? ").lower()
    if again == "y":
        decoder()
    else:
        quit

print "###Welcome to the Digital Morse Coder###"
time.sleep(2)
decoder()
