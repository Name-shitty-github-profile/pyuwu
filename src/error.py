class errors:
  def __init__(self):
    self.handled: int = 0

  def sthandled(self):
    self.handled += 1
    return self

  def error(self, msg: str, op: str) -> None:
    if self.handled != 0:
      self.handled -= 1
      return None
    print(f'\033[35mThe cwode waiswed an exsweptwion >:c\nSwource\n{op}\n{msg}')
    return None
