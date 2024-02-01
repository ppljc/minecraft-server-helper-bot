# <---------- Python modules ---------->
import logging

from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


# <---------- Variables ---------->
logger = None


# <---------- Interoperability with logger ---------->
def start_logger():
	"""
	Creating logger object.
	:return: True or False based on the result of creating the logger
	"""
	try:
		global logger
		logger = logging.getLogger(__name__)
		logger.setLevel(logging.INFO)
		Path(r"logs").mkdir(parents=True, exist_ok=True)
		log_filename = f'logs/{datetime.now().strftime("%Y-%m-%d")}_log.log'
		handler = TimedRotatingFileHandler(log_filename, when="midnight", interval=1, encoding='utf-8')
		handler.suffix = "%Y-%m-%d"
		handler.setLevel(logging.INFO)

		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
		handler.setFormatter(formatter)

		logger.addHandler(handler)
		return True
	except Exception as exception:
		print(f'Logger not created. Exception "{exception}".')
		return False


def create_log(function):
	def wrapper(*args, **kwargs):
		print(dir(function))
		print(function.__str__)
		log_message = f'FILENAME="{function.__code__.co_filename.split("/")[-1]}"; FUNCTION="{function.__name__}"; CONTENT=""; EXCEPTION="";'
		date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f'DATE="{date}"; {log_message}')
		logger.info(log_message)
		return function(*args, **kwargs)
	return wrapper


@create_log
def f(g='mega'):
	print(f'H {g}')
	return 'gay'



if __name__ == '__main__':
	start_logger()
	f()


# def create_log(filename: str, function: str, exception, content: str):
# 	"""
# 	Creating new log.
# 	:param filename: File name
# 	:param function: Function name
# 	:param exception: Exception or str object
# 	:param content:
# 	:return:
# 	"""
# 	log_message = f'FILENAME="{filename}"; FUNCTION="{function}"; CONTENT="{content}"; EXCEPTION="{exception}";'
# 	date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 	print(f'DATE="{date}"; {log_message}')
# 	logger.info(log_message)
