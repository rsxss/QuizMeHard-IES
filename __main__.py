from controller.router import RouterBuilder
from controller.routes import routes
from flask import Flask

ies = Flask(__name__)

ies_router = RouterBuilder(ies).build()
ies_router.register(routes())

if __name__ == "__main__":
	ies_params = {
		"debug":True,
		"port":8001
	}; ies.run(**ies_params)