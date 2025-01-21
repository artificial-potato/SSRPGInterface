from . import ssrpgif
command_cache = {}
"""
```
{
	index( (name,) + args ): cache,
	...
}
```
"""
preload_index = []

def preload():
	command_cache.clear()

	command_list = [index for index in preload_index]
	multi_call(command_list)

	preload_index.clear()

def get_cache(key):
	return command_cache.get(key, None)

def set_cache(data, key):
	command_cache[key] = data


def call(name:str, *args):
	index = (name,) + args
	data = get_cache(index)
	if not data is None:
		preload_index.append(index)
		return data
		
	data = ssrpgif.call(name, *args)
	
	if not data is None:
		preload_index.append(index)
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
		if data is None:
			continue
		if data == "cmd_done":
			continue

		if not False in finish:
			break
		result_index = finish.index(False, result_index)

		result[result_index] = data
		finish[result_index] = True

		set_cache(data, command_list[result_index])

	return result