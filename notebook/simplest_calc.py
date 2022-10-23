del os # make sure os package is not imorted to avoid serious injuries
exp = None
while (not exp):
    exp= input("Enter expression to calculate:")
    try:
      print(" your answer is :>> ", eval(exp))
    except Exception as e:
      print(str(e))
