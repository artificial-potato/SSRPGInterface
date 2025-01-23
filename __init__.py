from os import _exit
import threading

def run_script(step, host="127.0.0.1", port=64649):
	"""
    Start the interface and execute the step function in a loop.
    """

	from . import ssrpgif

	if ssrpgif.connect(host, port):
		ssrpgif.run(step)

def user_input():
	while True:
		data = input()
		print(data)
		match data:
			case "exit":
				_exit(0)
			case _:
				pass

def run(step, host="127.0.0.1", port=64649):
	run_script(step, host, port)
	# main = threading.Thread(target=run_script, args=(step, host, port))
	# main.start()
	# main.join()

	# user_action = threading.Thread(target=user_input)
	# user_action.start()
	# user_action.join()