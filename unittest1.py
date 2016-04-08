# By Emrah KORKMAZ
# This code is a tool to read from stdin and writes to a file

import sys,os

def testing(handle):
    with open('report.txt','w') as f1: # appends the line to the text file
        while 1:
            try:
                line = handle.read(1) #reads lines
                if len(line) == 0:
                    break
                f1.write(line)
            except KeyboardInterrupt:       # stops with keybord interrupt
                break


with open('moby.txt','r') as f1:
    testing(f1)


import unittest

class Mytest(unittest.TestCase):
    def test_predicted(value):
        value.assertEqual(os.path.getsize('report.txt'), os.path.getsize('moby.txt'))


if __name__ == '__main__':
    unittest.main()


##testing(sys.stdin)
