# By Emrah KORKMAZ
# This code is a tool to read from stdin and writes to a file

import sys, os

with open('report.txt','w') as f1: # writes the line to the text file
    while 1:
        try:
            fd = sys.stdin.fileno()
            line = os.read(fd,1024) #reads lines
            if len(line) == 0:
                break
            f1.write(line)
            f1.flush()
        except (KeyboardInterrupt):       # stops with keybord interrupt
            break



