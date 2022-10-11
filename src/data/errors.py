from ..error import errors
error = None

def get_error():
  global error
  if error is None:
    error = errors()
  return error
