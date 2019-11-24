class RouterBuilder():

	__slots__ = ('__app')
	def __init__(self, app):
		self.__app = app

	def build(self):
		return self.Router(self.__app)

	class Router():

		__slots__ = ('__app')
		def __init__(self, app):
			self.__app = app

		def register(self, routes):
			for route in routes:
				rule = route.get('rule')
				endpoint = route.get('endpoint')
				callback = route.get('callback')
				options = route.get('options')
				self.__app.add_url_rule(rule,endpoint, callback, **options)