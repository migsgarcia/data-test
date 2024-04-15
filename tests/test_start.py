import pytest

def test_div_zero_exception():
  """
  pytest.raises can assert that exceptions are raised (catching them)
  """
  with pytest.raises(ZeroDivisionError):
    x = 1 / 0