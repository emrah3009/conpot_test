# By Emrah KORKMAZ
# This code is a tool to read from stdin and writes to a file
import sys

with open('report.txt','w') as f1: # appends the line to the text file
    while 1:
        try:
            line = sys.stdin.read(1)
            if len(line) == 0:
                break
            f1.write(line)
        except KeyboardInterrupt:       # stops with keybord interrupt
            break
