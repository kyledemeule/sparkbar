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

  def barh(self, value):
    bar_length = math.floor(self.width * (value / self.max_value))
    return BLOCKS["8"] * bar_length


if __name__=="__main__":
  sb = SparkBar(max_value=400, width=32)

  test_data = [
    ("Blue", 400),
    ("Black", 320),
    ("Red", 125),
  ]

  for car, val in test_data:
    print("{}\t{} {}".format(car, sb.barh(val), val))
