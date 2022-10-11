data: dict = {}
from .errors import get_error

def get_var(var: str):
  try:
    return data[var]
  except KeyError:
    get_error().error(f"No such variable {var}", "Cannot trace the operation.")
  return None

def add_var(dat: dict):
  global data
  try:
    data[dat['name']] = {"value": dat['value'], 'type': dat['type']}
  except KeyError:
    get_error().error("Invalid payload.\nPayload : " + dat + '\nPayload\nExcpected : {\n\t"name": "VarName",\n\t"value": "VarValue",\n\t"type": "VarType"\n}', "Cannot trace the operation.")
  return None

def rem_var(var: str):
  global data
  try:
    del data[var]
  except KeyError:
    get_error().error(f"No such variable {var}", "Cannot trace the operation.")
  return None

def clear_var():
  global data
  data = {}
  return None
