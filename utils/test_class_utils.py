from types import MethodType

from utils.test_class_utils import *

class InputUtil():

	@staticmethod
	def addTestByString(testClass, name, func):
		testClass[name] = MethodType(testClass, func)	