class NotFoundError(Exception):
	def __init__(self, message):
		super(NotFoundError, self).__init__(message)

class UpdateError(Exception):
	def __init__(self):
		super(UpdateError, self).__init__()