X_0=10000.0
Y=1000.0
H=1.01
N=120
def calcMoney (x0: float, y: float, h: float, nMonth: int) -> float:
  if (nMonth == 0):
    return x0
  elif (nMonth > 0):
    previousValue = calcMoney (x0, y, h, nMonth - 1)
    return ((previousValue * h) + y)
  else:
    return 0.0

def main():
  resultMoney = calcMoney(X_0, Y, H, N)

  print(f"""
  Initial money: {format(X_0, '.2f')}
  Addition per month: {format(Y, '.2f')}
  Increase rate per month: {format(H, '.2f')}
  Investment time: {N} months
  Final value: {format(resultMoney, '.2f')} moneys
  """)

main()
