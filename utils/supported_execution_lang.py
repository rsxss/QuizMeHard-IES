from enum import Enum, unique
from model.execution import *

@unique
class ExecutionLang(Enum):
	
	PYTHON = lambda execution_data: PythonExecutionModel(execution_data)
	#JAVA = "java"