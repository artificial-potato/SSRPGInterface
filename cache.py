from . import ssrpgif

cache_dict = {}
"""
```
{
	(name,) + args + (return_type,) : data,
	...
}
```
"""

def get_cache(key):
	return cache_dict.get(key, None)

def set_cache(data, key):
	cache_dict[key] = data



preload_index = []
keep_preload_index = []
exclude_preload_index = []

def preload():
	cache_dict.clear()

	command_list = [
		{
			"name": index[0],
			"args": index[1: -1],
			"return_type": index[-1]
		}
		for index in keep_preload_index + preload_index
	]
	multi_call(command_list)

	preload_index.clear()

def add_preload_index(index):
	if index in preload_index:
		return
	if index in keep_preload_index:
		return
	if index in exclude_preload_index:
		return
	preload_index.append(index)

def command_to_cache_index(name:str, args:list|tuple, return_type=None):
	return (name,) + tuple(args) + (return_type,)



def call(name:str, *args, return_type=None):
	cache_index = command_to_cache_index(name, args, return_type)

	data = get_cache(cache_index)
	if not data is None:
		add_preload_index(cache_index)
		return data
		
	data = ssrpgif.call(name, *args, return_type=return_type)
	
	if not data is None:
		add_preload_index(cache_index)
		set_cache(data, cache_index)

	return data

"""
# Do multi_call really need check cache?
def multi_call(command_list:list):
	result = [None] * len(command_list)

	data_list = ssrpgif.multi_call(command_list)

	for i, data in enumerate(data_list):
		if data in (None, "cmd_done"):
			continue

		result[i] = data
		set_cache(data, command_to_cache_index(**command_list[i]))

	return result
"""
def multi_call(command_list:list, check_cache:bool=False):
	list_length = len(command_list)
	finish = [False] * list_length
	result = [None] * list_length

	if check_cache:
		call_command_list = []
		for i, command in enumerate(command_list):
			cmd_data = get_cache(command)
			if cmd_data is None:
				call_command_list.append(command_list[i])
			else:
				result[i] = cmd_data
				finish[i] = True
	else:
		call_command_list = command_list

	data_list = ssrpgif.multi_call(call_command_list)

	index = -1
	for data in data_list:
		while index < list_length:
			index += 1
			if not finish[index]:
				break
		if index == list_length:
			break

		if data in (None, "cmd_done"):
			continue

		result[index] = data
		set_cache(data, command_to_cache_index(**command_list[index]))

	return result



action_command_list = []

def call_command(name:str, *args):
	action_command_list.append({
		"name": name,
		"args": args
	})

def run_command():
	if action_command_list:
		ssrpgif.multi_call_command(action_command_list)
		action_command_list.clear()