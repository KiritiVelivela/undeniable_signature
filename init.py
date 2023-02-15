import Solve
#import random
class PublicKey:
    p = 1
    alpha = 1
    beta = 1
class PrivateKey:
    a = 1
class Doc:
    x = 1
publicKey = PublicKey()
privateKey = PrivateKey()
doc = Doc()
def init():
    print("------Value initialization------")
    p = int(input("enter the prime number p:"))
    while (not (Solve.isPrime(p))) and (not (Solve.isPrime((p-1)/2))) :
        p = int(input("re-enter the prime number p:"))
    publicKey.p = p

    g = Solve.primRoots(p)[0]
    publicKey.alpha = g*g
    a = int(input("enter the number a with 1 <= a <= (p-1)/2: "))
    privateKey.a = a
    publicKey.beta = Solve.powerMode(publicKey.alpha, privateKey.a, publicKey.p)

    print("public key: K(p, alpha, beta) : K(" + str(publicKey.p) + ", " + str(publicKey.alpha) + ", " + str(publicKey.beta) + ")")
    print("secret key aK(a) : K(" + str(privateKey.a) + ")")
    x = int(input("enter text x:"))
    doc.x = x
