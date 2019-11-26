import traceback

from utils.supported_execution_lang import *
from model.execution import *

from flask import request, jsonify, abort

class DRCC():
	"""
		DefaultRouteCallbackCollection
	"""
	@staticmethod
	def index():
		return "Welcome to index page."

	@staticmethod
	def test():
		return "_test"

	"""
		execution_data: {
			code: string,
			lang: string,
			comment: string
		}
	"""
	@staticmethod
	def execute():
		try:
			if request.method == "POST":
				req_data = request.get_json()
				# print("POST DATA:",req_data)
				execution_data = {
					'code': req_data.get('code'),
					'lang': req_data.get('lang'),
					'comment': req_data.get('comment')
				}; 
				executor = ExecutionLang.__dict__[execution_data.get('lang').upper()](execution_data)
				response = {
					'results': executor.execute(),
					'status': 200
				}
				return jsonify(**response), 200
		except:
			response = {
				'status': 500,
				'error': traceback.format_exc(-1)
			}
			return abort(jsonify(**response)), 500
		

def routes():
	callback_collection = [func for func in dir(DRCC) if callable(getattr(DRCC, func)) and not func.startswith("__")]
	return ({
	'rule': f'/api/{callback_name}',
	'endpoint': callback_name,
	'callback': getattr(DRCC, callback_name),
	'options': {
		'methods': ['GET','POST']
	}} for callback_name in callback_collection)

# for i in routes():
# 	print(i)