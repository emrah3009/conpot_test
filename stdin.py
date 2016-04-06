# By Emrah KORKMAZ
# This code is a tool to read from stdin and writes to a file
import sys
while 1:
    try:
        line = sys.stdin.readline()  #reads lines
    except KeyboardInterrupt:       # stops with keybord interrupt
        break

    if not line:                    
        break

    with open('report.txt','a') as f1: # appends the line to the text file
        f1.write(str(line))
f1.close
