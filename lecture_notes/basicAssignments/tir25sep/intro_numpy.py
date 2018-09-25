import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([9, 8, 7, 6])
# print(a)

# lægger hver element sammen i hvert array. Virker også med -, * osv.
# Array skal have samme længde.
a + b

c = np.arange(9, 30)  # Længden af et array med elementer fra 9 til 30.
c.size
c.shape

# Flerdimentionelt array. 3 dimentioner og hver har 7 elemnter
d = np.arange(9, 30).reshape(3, 7)
dd = np.arange(30).reshape(3, 2, 5)

dd + 4  # Lægger 4 til hvert element. F.eks. lidt lysere i et billede.
dd[0][0]

ddd = np.arange(11, 36).reshape(5, 5)
# ddd[0, :]  # filterer på flere dimentioner
# ddd[1, 1:4]  # find 17 til 19
# ddd[1:4, 1]  # 17 til 27
# ddd[:, 1]  # Hele 2. kolonne
#ddd[::2, ::2]  # find 11, 13, 15, 21, 23, 25, 31, 33, 35
 # Hvilke elementer er større end 23. Returner array med true false.
ddd[(ddd > 23) & (a < 33)] # indekser med boolean array. Mister dimentioner. HUSK! Der skal være parentes!
print(ddd)
