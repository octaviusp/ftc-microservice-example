import os

class Config:
	# SOME CONFIGS
	DB_PORT = os.environ.get('DB_PORT')
	DB_HOST = os.environ.get('DB_HOST')
	# DB_PW... ETC
