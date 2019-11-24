from abc import ABCMeta, abstractmethod

class ExecutionModel(metaclass=ABCMeta):
	"""
		Dictionary:input_data
	"""
	def __init__(self, execution_data):
		self.__code = execution_data.get('code')
		self.__comment = execution_data.get('comment')

	@property
	def code(self):
		return self.__code

	@code.setter
	def code(self, new_code):
		self.__code = new_code

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
		return f'(Mockup) Executing {self.__code}'
