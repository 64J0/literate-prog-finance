X_0=10000.0
Y=1000.0
H=1.01
N=120
# Python + Emacs:
# ===========================
#
# If you want to show in the end of the execution, the result of
# an operation, set :results value in the SRC block headers, and
# make sure that the main function has a return statement.
# If you want to just show a print result, set the :results output
# in the header.
#
# Reference: https://emacs.stackexchange.com/a/64539

def calcMoney (x0: float, y: float, h: float, nMonth: int) -> float:
  if (nMonth == 0):
    return x0
  elif (nMonth > 0):
    previousValue = calcMoney (x0, y, h, nMonth - 1)
    return ((previousValue * h) + y)
  else:
    return 0.0

def main ():
  resultMoney = calcMoney(X_0, Y, H, N)

  return f"""
  Initial money: {X_0:.2f}
  Addition per month: {Y:.2f}
  Increase rate per month: {H:.2f}
  Investment time: {N} months
  Final value: {resultMoney:.2f} moneys
  """

return main()
