handled = 0

def sthandled():
  global handled
  handled += 1

def error(msg: str, op: str) -> None:
  global handled
  if handled != 0:
    handled -= 1
    return None
  print(f'\033[35mThe code raised an exception\nSource\n{op}\n{msg}')
  return None
