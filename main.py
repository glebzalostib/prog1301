a = input("Ievadit tekst: ")
def delete(a):
  if a.count("e")>0:
    a = a.replace("e"," ")
    print(a.upper())
  else:
    a = "TEKSTS NESATUR VAJADZIGO BURTU"
    print(a)
  return a
delete(a)