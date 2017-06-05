def validate(data):
	assert 'name' in data
	assert 'nodes' in data
	assert 'links' in data
	assert 'node_counter' in data
	assert 'link_counter' in data
	return data

def error(message):
	return {'error': message}

def serializable(story):
	story['_id'] = str(story['_id'])