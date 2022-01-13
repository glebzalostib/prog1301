a = input("Ievadit teksts: ")
def replaceTwos(a):
  if a.count("2")>0:
    a = a.replace("2","divi")
    print(a)
  else:
    a = print("tekstu nav")
  return a 
replaceTwos(a)