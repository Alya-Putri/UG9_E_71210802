data = [1,3,9,27,81]
print ("Deret = 1,3,9,27,81, . . . .")
a = data[1]
n = 11
r1 = data[2]/data[1]
r2 = data[3]/data[2]
if r1 == r2:
    r = r1
    print ("r = " ,"%.0f"% r)
Un = a * (r**(n-1))
print ("a = ","%.0f"%a)
print ("n = ","%.0f"% n)
print ("Un = ","%.0f"% Un)
print ("")
print ("Menggunakan Perulangan")

for x in range(1,n+1):
    n_n = a * (r**(x-1))
    print("%.0f"%n_n)
print("Jadi suku ke-11 adalah ","%.0f"% n_n)
