from yourbase import accelerate_tests


@accelerate_tests()
class TestApplication:
    def test_a_thing(self):
        print("If you are reading this, this test was not skipped")
