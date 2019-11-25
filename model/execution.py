from abc import ABCMeta, abstractmethod
from importlib import import_module

class ExecutionModel(metaclass=ABCMeta):
	"""
		Dictionary:input_data
	"""
	def __init__(self, execution_data):
		self.__code = execution_data.get('code')
		self.__lang = execution_data.get('lang')
		self.__comment = execution_data.get('comment')

	@property
	def code(self):
		return self.__code
	@property
	def lang(self):
		return self.__lang
	@property
	def comment(self):
		return self.__comment
	
	@code.setter
	def code(self, new_code):
		self.__code = new_code
	@lang.setter
	def lang(self, new_lang):
		self.__lang = new_lang
	@comment.setter
	def lang(self, new_code):
		self.__comment = new_comment

	@abstractmethod
	def execute(self):
		pass

class PythonExecutionModel(ExecutionModel):
	"""
		Execution class for python
	"""
	def __init__(self, execution_data):
		super().__init__(execution_data)

	def execute(self):
		mbt = import_module('model.base_test')
		utcu = import_module('utils.test_class_utils')
		unittest = import_module('unittest')
		__base__ = mbt.InputTestCase
		__utils__ = utcu.InputUtil(__base__)
		exec_variables = {
			'globals': {
				
			},
			'locals':{
				f'__{mbt.InputTestCase.__name__}__': __base__,
				'__utils__': __utils__,
				'assert_equal': __utils__.assert_equal,
				'unittest': unittest
			}
		}
		code_object = compile(self.code, 'code', 'exec')
		execution = exec(code_object, exec_variables.get('globals'), exec_variables.get('locals'))
		#print(dir(exec_variables.get('locals')['__InputTestCase__']))
		suite = unittest.TestLoader().loadTestsFromTestCase(exec_variables.get('locals')['__InputTestCase__'])
		#suite = unittest.defaultTestLoader.loadTestsFromTestCase(exec_variables.get('locals')['__InputTestCase__'])
		test_result = unittest.TextTestRunner(verbosity=0).run(suite)
		return __utils__.results()['case_results']
		#print(exec_variables.get('locals'))
		# return {
		# 	'results': exec_variables.get('locals')['results']	
		# }

# def assert_equal(x, y):
# 	func = lambda self: self.assertEqual(x, y)
# 	addTestByString(testClass, f'test_case_{count}', func)