import inspect
import os
import unittest
import yourbase


def set_up(self: unittest.TestCase):
    if yourbase.PLUGIN is None:
        return

    fname: str = self._testMethodName
    fn = getattr(self, fname)
    fpath: str = os.getcwd() + os.sep + inspect.getfile(fn)

    if yourbase.PLUGIN.can_skip(fpath, fname):
        self.skipTest("[YB] No dependencies changed ✨")
    else:
        yourbase.PLUGIN.start_test(fpath, fname)


def tear_down(self: unittest.TestCase):
    if yourbase.PLUGIN is None:
        return

    fname: str = self._testMethodName
    fn = getattr(self, fname)
    fpath: str = os.getcwd() + os.sep + inspect.getfile(fn)

    yourbase.PLUGIN.end_test(fpath, fname)


unittest.TestCase.setUp = set_up
unittest.TestCase.tearDown = tear_down
