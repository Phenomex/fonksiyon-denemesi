def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
dortkati = myfunc(4)
beskati = myfunc(5)
altikati =myfunc(6)
yedikati =myfunc(7)
sekizkati =myfunc(8)
dokuzkati =myfunc(9)
val = 2 ** 2
print("Doubled: " + str(doubler(val))  + "\nTripled: " + str(tripler(val)) +  " \nQuadrupled: " +str(dortkati(val)) + "\nQunitupled: " +str(beskati(val)) + "\nSextupled: " +str(altikati(val)) + "\nSeptupled: " +str(yedikati(val)) +   "\nOctupled: " +str(sekizkati(val)) + "\nNonupled: " +str(dokuzkati(val)))