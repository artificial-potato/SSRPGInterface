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
	if index in exclude_preload_index:
		return
	if index in keep_preload_index:
		return
	preload_index.append(index)



def call(name:str, *args, return_type=None):
	index = (name,) + args + (return_type,)

	data = get_cache(index)
	if not data is None:
		add_preload_index(index)
		return data
		
	data = ssrpgif.call(name, *args, return_type=return_type)

	if not data is None:
		add_preload_index(index)
		set_cache(data, index)

	return data

def multi_call(command_list:list, check_cache:bool=False):
	finish = [False for i in range(len(command_list))]
	result = [None for i in range(len(command_list))]

	if check_cache:
		for i in range(len(command_list)):
			command = command_list[i]
			cmd_data = get_cache(command)
			if not cmd_data is None:
				result[i] = cmd_data
				finish[i] = True

		new_command_list = []
		for i in range(len(finish)):
			if finish is False:
				new_command_list.append(command_list[i])
		command_list = new_command_list

	data_list = ssrpgif.multi_call(command_list)

	result_index = 0
	for data in data_list:
		if not False in finish:
			break
		result_index = finish.index(False, result_index)
		finish[result_index] = True

		if data is None:
			continue
		if data == "cmd_done":
			continue

		result[result_index] = data

		command = command_list[result_index]
		index = (command["name"],) + command["args"] + (command["return_type"],)
		set_cache(data, index)

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