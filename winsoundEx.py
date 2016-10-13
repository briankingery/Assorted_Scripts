# Morsecode.py


import winsound
import time

t = 250
p = .50

llC = 65

lC  = 131
lDb = 139
lD  = 147
lEb = 156
lE  = 165
lF  = 175
lGb = 185
lG  = 196
lAb = 208
lA  = 220
lBb = 233
lB  = 247


C  = 262
Db = 277
D  = 294
Eb = 311
E  = 330
F  = 349
Gb = 370
G  = 392
Ab = 415
A  = 440
Bb = 466
B  = 494

hC  = 523
hDb = 554
hD  = 587
hEb = 622
hE  = 659
hF  = 698
hGb = 740
hG  = 784
hAb = 831
hA  = 880
hBb = 932
hB  = 988

time.sleep(0.001)

for i in range (5):
    
    winsound.Beep( lC, 2*t)
    winsound.Beep( hC, t)
    winsound.Beep( hE, t)
    winsound.Beep( hG, t)
    time.sleep(p)
    
    winsound.Beep( lG, 2*t)
    winsound.Beep( G, t)
    winsound.Beep( B, t)
    winsound.Beep( hD, t)
    time.sleep(p) 
    
    winsound.Beep( lA, 2*t)
    winsound.Beep( A, t)
    winsound.Beep( hC, t)
    winsound.Beep( hE, t)
    time.sleep(p)
    
    winsound.Beep( lE, 2*t)
    winsound.Beep( E, t)
    winsound.Beep( G, t)
    winsound.Beep( B, t)
    time.sleep(p)          
    
    winsound.Beep( lF, 2*t)
    winsound.Beep( F, t)
    winsound.Beep( A, t)
    winsound.Beep( hC, t)
    time.sleep(p)      
    
    winsound.Beep( llC, 2*t)
    winsound.Beep( C, t)
    winsound.Beep( E, t)
    winsound.Beep( G, t)
    time.sleep(p)
    
    winsound.Beep( lF, 2*t)
    winsound.Beep( F, t)
    winsound.Beep( A, t)
    winsound.Beep( hC, t)
    time.sleep(p)         
    
    winsound.Beep( lG, 2*t)
    winsound.Beep( G, t)
    winsound.Beep( B, t)
    winsound.Beep( hD, t)
    time.sleep(p)  
















##import winsound
##import time
##
##winsound.Beep(293, 200) # D
##winsound.Beep(293, 200) # D
##winsound.Beep(293, 200) # D
##winsound.Beep(293, 600) # D
##winsound.Beep(246, 600) # B
##
##time.sleep(0.1)
##
##winsound.Beep(369, 200)# F#
##winsound.Beep(369, 200)# F#
##winsound.Beep(369, 200)# F#
##winsound.Beep(369, 600)# F#
##winsound.Beep(329, 600) # E
##
##time.sleep(0.1)
##
##winsound.Beep(329, 200) # E
##winsound.Beep(329, 200) # E
##winsound.Beep(329, 200) # E
##winsound.Beep(369, 500) # F#
##
##time.sleep(0.9)
##
##winsound.Beep(369, 200) # F#
##winsound.Beep(369, 200) # F#
##winsound.Beep(369, 200) # F#
##winsound.Beep(369, 600) # F#
##
##time.sleep(0.9)
##winsound.Beep(369, 200) # F#
##winsound.Beep(369, 200) # F#
##winsound.Beep(369, 200) # F#
##
##for i in range(4):
##    winsound.Beep(369, 200) # F#
##    time.sleep(0.1)
##
##for i in range(4):
##    winsound.Beep(369, 100) # F#
##    time.sleep(0.1)
##
##winsound.Beep(369, 600) # F#
##
### PYTHON GANGNAM STYLE!

























##import winsound
##import time
##
###dot = winsound.Beep(293, 100) # D
###dash = winsound.Beep(293, 400) # D
##delay = 0.1
##
##def decoder():
##    message =  raw_input("Please enter your message? ").lower()
##
##    print message
##
##    for letter in message:
##        if letter == " ":
##            time.sleep(1)
##        elif letter == "a":
##            print letter
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "b":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 200) # D
##            time.sleep(delay)
##        elif letter == "c":
##           print letter
##           winsound.Beep(293, 800) # D
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 800) # D
##           winsound.Beep(293, 200) # D
##           time.sleep(delay)
##        elif letter == "d":
##           print letter
##           winsound.Beep(293, 800) # D
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 200) # D
##           time.sleep(delay)
##        elif letter == "e":
##            print letter
##            winsound.Beep(293, 200) # D
##            time.sleep(delay)
##        elif letter == "f":
##           print letter
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 800) # D
##           winsound.Beep(293, 200) # D
##           time.sleep(delay)
##        elif letter == "g":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D
##            time.sleep(delay)
##        elif letter == "h":
##           print letter
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 200) # D
##           winsound.Beep(293, 200) # D
##           time.sleep(delay)
##        elif letter == "i":
##            print letter
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 200) # D
##            time.sleep(delay)
##        elif letter == "i":
##            print letter
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 200) # D
##            time.sleep(delay)
##        elif letter == "j":
##            print letter
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "k":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "l":
##            print letter
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 200) # D 
##            time.sleep(delay)
##        elif letter == "m":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "n":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D 
##            time.sleep(delay)
##        elif letter == "o":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "r":
##            print letter
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D 
##            time.sleep(delay)
##        elif letter == "s":
##            print letter
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 200) # D 
##            time.sleep(delay)
##        elif letter == "t":
##            print letter
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "u":
##            print letter
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "v":
##            print letter
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "w":
##            print letter
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)    
##        elif letter == "x":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 200) # D 
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "y":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            time.sleep(delay)
##        elif letter == "z":
##            print letter
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 800) # D
##            winsound.Beep(293, 200) # D
##            time.sleep(delay)   
##
##    print ("Your message was coded")
##    time.sleep(2)
##    again = raw_input("Do you want to code another message, y/n? ").lower()
##    if again == "y":
##        decoder()
##    else:
##        quit
##
##print "###Welcome to the Digital Morse Coder###"
##time.sleep(2)
##decoder()


##from Tkinter import *
##import winsound
##
##def playSound(canvas, synchronous):
##    if (synchronous):
##        flags = winsound.SND_FILENAME
##    else:
##        # asynchronous
##        flags = winsound.SND_FILENAME | winsound.SND_ASYNC
##    canvas.data["soundCounter"] += 1
##    sounds = ["sound1.wav", "sound2.wav", "sound3.wav" ]
##    sound = sounds[canvas.data["soundCounter"] % len(sounds)]
##    winsound.PlaySound(sound, flags)
##
##def startSoundLoop():
##    flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
##    winsound.PlaySound("sound1.wav", flags)
##
##def stopSoundLoop():
##    flags = winsound.SND_FILENAME
##    winsound.PlaySound(None, flags)
##
##def keyPressed(event):
##    canvas = event.widget.canvas
##    if (event.char == "p"):
##        playSound(canvas, True) # synchronous
##    elif (event.char == "a"):
##        playSound(canvas, False) # asynchronous
##    elif (event.char == "l"):
##        startSoundLoop()
##    elif (event.char == "s"):
##        stopSoundLoop()
##    else:
##        # quick short high beep
##        hertz = 1760
##        milliseconds = 64
##        winsound.Beep(hertz, milliseconds)
##    redrawAll(canvas)
##
##def redrawAll(canvas):
##    canvas.delete(ALL)
##    font = ("Arial", 24, "bold")
##    # Draw the event info
##    msg = "Press p to play synchronous sound"
##    canvas.create_text(300, 100, text=msg, font=font)
##    msg = "Press a to play asynchronous sound"
##    canvas.create_text(300, 200, text=msg, font=font)
##    msg = "Press l to start loop"
##    canvas.create_text(300, 300, text=msg, font=font)
##    msg = "Press s to stop loop"
##    canvas.create_text(300, 400, text=msg, font=font)
##
##def init(canvas):
##    canvas.data["soundCounter"] = 0
##    redrawAll(canvas)
##
############# copy-paste below here ###########
##
##def run():
##    # create the root and the canvas
##    root = Tk()
##    canvas = Canvas(root, width=600, height=500)
##    canvas.pack()
##    # Store canvas in root and in canvas itself for callbacks
##    root.canvas = canvas.canvas = canvas
##    # Set up canvas data and call init
##    canvas.data = { }
##    init(canvas)
##    # set up events
##    root.bind("<Key>", keyPressed)
##    # timerFired(canvas)
##    # and launch the app
##    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
##
##run()




##import math
##import wave
##import struct
##
##def synthComplex(freq=[440],coef=[1], datasize=10000, fname="test.wav"):
##    frate = 44100.00  
##    amp=8000.0 
##    sine_list=[]
##    for x in range(datasize):
##        samp = 0
##        for k in range(len(freq)):
##            samp = samp + coef[k] * math.sin(2*math.pi*freq[k]*(x/frate))
##        sine_list.append(samp)
##    wav_file=wave.open(fname,"w")
##    nchannels = 1
##    sampwidth = 2
##    framerate = int(frate)
##    nframes=datasize
##    comptype= "NONE"
##    compname= "not compressed"
##    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
##    for s in sine_list:
##        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
##    wav_file.close()
##
##synthComplex([440,880,1200], [0.4,0.3,0.1], 30000, "tone.wav")

