import init
import Signing
import Solve
import Disavowal

def verify():
    print("------Test protocol------")
    signY = int(input("enter the received signature: "))
    print("message x with signature y: x = " + str(init.doc.x))
    print("test with public key: K(p, alpha, beta) : K(" + str(init.publicKey.p) + ", " + str(init.publicKey.alpha) + ", " + str(init.publicKey.beta) + ")")
    print("random selection e1, e2 with 1 <= e1, e2 <= p - 1:")
    e1 = int(input("import e1:"))
    e2 = int(input("import e2:"))
    c = Solve.powerMode(signY, e1, init.publicKey.p)*Solve.powerMode(init.publicKey.beta, e2, init.publicKey.p) % init.publicKey.p
    print("the testing party calculates c and sends it to the signer: c = y^e1.beta^e2 mod p = " + str(c))
    d = Solve.powerMode(c, int(Solve.ext_gcd((init.publicKey.p - 1)/2, init.privateKey.a)), init.publicKey.p)
    print("the signing party d sends it to the tester: d = c^(a^-1 mod q) mod p = " + str(d))
    check = Solve.powerMode(init.doc.x, e1, init.publicKey.p)*Solve.powerMode(init.publicKey.alpha, e2, init.publicKey.p) % init.publicKey.p
    print("testers check d = (x^e1 * alpha^e2 mod p) or not, check = " + str(check))
    if(check == d): print("match d => valid signature")
    else:
        print("does not match d => perform rejection protocol step")
        Disavowal.disavowal(init.doc.x, signY, e1, e2, c, d)