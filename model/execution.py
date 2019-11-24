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
		local_variables = {}
		code_object = compile(self.code, 'code', 'exec')
		exec(code_object, globals(), local_variables)
		print(local_variables)

