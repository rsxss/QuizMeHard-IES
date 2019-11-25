from types import MethodType

class InputUtil():

	def __init__(self, test_class):
		self.__test_class = test_class
		self.__test_results = {'case_results': {}}
		self.__test_case_counter = 0

	@classmethod
	def addTestByString(self, test_class, name, callback):
		class_name = test_class.__name__
		callback_name = callback.__name__
		exec_variables = {
			'globals': {
				
			},
			'locals':{
				f'{class_name}': test_class,
				f'{callback_name}': callback,
				'MethodType': MethodType
			}
		}
		exec(compile(f'{class_name}.{name} = MethodType({callback_name}, {class_name})', 'addTestByString', 'exec'), 
			exec_variables.get('globals'), exec_variables.get('locals'))


	def assert_equal(self, x, y, score):
		def do_func(test_instance):
			try:
				assert x==y
				self.__test_results['case_results'][f'case_{case_no}'] = {
					'score': score,
					'result': True
				}
			except AssertionError:
				self.__test_results['case_results'][f'case_{case_no}'] = {
					'score': score,
					'result': False
				}
			# if test_instance.assertEqual(test_instance, x, y):
			# 	test_instance.__test_results['case_results'][f'case_{case_no}'] = {
			# 		'score': score,
			# 		'result': True
			# 	}
			# else:
			# 	test_instance.__test_results['case_results'][f'case_{case_no}'] = {
			# 		'score': score,
			# 		'result': False
			# 	}
		self.__test_case_counter += 1
		case_no = self.__test_case_counter
		self.addTestByString(self.__test_class, f'test_case_{case_no}', do_func)

	def results(self):
		return self.__test_results