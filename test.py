import math

BLOCKS = {
  "8": "█",
  "7": "▉",
  "6": "▊",
  "5": "▋",
  "4": "▌",
  "3": "▍",
  "2": "▎",
  "1": "▏"
}

class SparkBar:
  def __init__(self,
    max_value=1.0,
    width=8,
    cap_overflow=False
  ):
    self.max_value = max_value
    self.width = width
    self.cap_overflow = cap_overflow

  def barh(self, value):
    try:
      return [self.__barh_cell(x) for x in iter(value)]
    except TypeError:
      return self.__barh_cell(value)

  def __barh_cell(self, value):
    if self.cap_overflow:
      value = min(value, self.max_value)

    assert value <= self.max_value, "barh cell value exceeds max value and cap_overflow is set to False."

    bar_length = math.floor(self.width * (value / self.max_value))
    return BLOCKS["8"] * bar_length



if __name__=="__main__":
  sb = SparkBar(max_value=400, width=32, cap_overflow=True)

  test_data = [
    ("Blue", 400),
    ("Black", 320),
    ("Red", 125),
  ]

  for car, val in test_data:
    print("{}\t{} {}".format(car, sb.barh(val), val))


  brs = sb.barh([220, 300, 404])
  for b in brs:
    print(b)
