# By Emrah KORKMAZ
# This code is a tool to read from stdin and writes to a file

import sys,os

def testing(handle):
    with open('report.txt','w') as f1: # appends the line to the text file
        while 1:
            try:
                fd = handle.fileno()
                line = os.read(fd,1024)
                #line = handle.read(1) #reads lines
                if len(line) == 0:
                    break
                f1.write(line)
                f1.flush()
            except KeyboardInterrupt:       # stops with keybord interrupt
                break


def reading(files): # reads files and test in the stdin code
    with open(files,'r') as f1:
        testing(f1)


import unittest

class Mytest(unittest.TestCase):
    def test_predicted1(value): # unit testing with a file
        reading('moby.txt')
        value.assertEqual(os.path.getsize('report.txt'), os.path.getsize('moby.txt'))
 
    def test_predicted2(value): # unit testing with an empty file
        reading('emptyfile.txt')
        value.assertEqual(os.path.getsize('report.txt'), os.path.getsize('emptyfile.txt'))        

    def test_predicted3(value): # unit testing with stdin
         testing(sys.stdin)
        
        

if __name__ == '__main__':
    unittest.main()


