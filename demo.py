from yourbase import accelerate_tests

@accelerate_tests()
class TestApplication:
    def __init__(self):
        print("Initialize test app!")

    def frobozz(self, message):
        print("Message: %s" % (message))

    def test_bailout(self, message):
        print("Test message: %s" % (message))



x = TestApplication()
x.frobozz("OHAI")
x.test_bailout("BAD")

import math


print(math.cos(0))
