 #By Emrah KORKMAZ
 #This code is a tool to read from stdin and writes to a file

import tty
import termios
import sys, os


def reading1(handle):
    fd = sys.stdin.fileno()
    # keep original terminal settings
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(handle.fileno())
        ch = handle.read(1)
    except Exception as e:
        print(e)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def reading2(handle):
   while 1:
        try:
            #line = handle.read(1)
            fd = handle.fileno()
            line = os.read(fd,1024*4)
            if len(line) == 0:
                break
            write_to_file(line)
        except KeyboardInterrupt:       # stops with keybord interrupt
            break

def read_file(files):             # to read from a file
    with open(files,'r') as f1:
        reading2(f1)

def write_to_file(x1):
    with open('report.txt','a') as f1: # writes the line to the text file
        f1.write(x1)
        
def choose_type(handle):
    while 1:
        if type(handle) == str:
            read_file(handle)
            break

        else:
            ch = reading1(sys.stdin)
            chk = ord(ch)
            #print (repr(ch))
            if chk in [3, 4]:
            # ctrl+c and ctrl+d
                break
            write_to_file(ch)


choose_type(sys.stdin) # read from sys.stin
#choose_type('moby.text') # read from a file



