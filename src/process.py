from .data import get_error
from .power import powertree
def interpret(content: str = None, *, FileName: str = None) -> any:
  errors = get_error()
  if content is None:
    if FileName is None: raise ValueError("Must have a content or a filename")
    with open(FileName, 'r') as f:
      content = f.read()
  for co in content.split(' uwu'):
    if co.startswith('pwease') is False:
      errors.error('You made daddwy/mommwy angwi daddwy/mommwy don\'t know where to start >:c', co)
    try:
      powertree[co.split(' ')[1]](co[6:])
    except:
      errors.error('You made daddwy/mommwy angwi daddwy/mommwy don\'t know what is this power >:c', co)
