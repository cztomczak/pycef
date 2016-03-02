"""Test core functionality.

- init() and quit() without calling run() or work()
- init(), run(), quit()
- init(), work() in a timer, quit()
- test instantiating cef.LoadEvents abstract class, should throw error
- test defining LoadEvents invalid callback:
    - invalid name of a callback
    - invalid number of parameters
"""

import unittest
import _run
from os.path import basename

# Globals
gcounter = 0


class Core1_NewPythonInstance(unittest.TestCase):
    
    def test1(self):
        global gcounter
        gcounter += 1
        print("\ngcounter: "+str(gcounter))

    def test2(self):
        pass


class Core2_NewPythonInstance(unittest.TestCase):

    def test3(self):
        global gcounter
        gcounter += 1
        print("\ngcounter: "+str(gcounter))


if __name__ == "__main__":
    _run.main(basename(__file__))
