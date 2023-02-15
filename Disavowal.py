import init
import Solve
import Verify
import Signing

def disavowal(docX, signY, e1, e2, c, d):
    print("------rejection protocol------")
    print("randomly choose f1, f2 with 1 <= f1, f2 < (p - 1)/2:")
    f1 = int(input("import f1: "))
    f2 = int(input("import f2: "))
    C = Solve.powerMode(signY, f1, init.publicKey.p)*Solve.powerMode(init.publicKey.beta, f2, init.publicKey.p) % init.publicKey.p
    print("the testing party calculates C and sends it to the signer: C = y^f1 * beta^f2 mod p =" + str(C))
    D = Solve.powerMode(C, Solve.ext_gcd(int((init.publicKey.p-1)/2), init.privateKey.a), init.publicKey.p)
    print("party signs D and sends it to testers: D = C^(a^-1 mod q) mod p = " + str(D))
    check = Solve.powerMode(docX, f1, init.publicKey.p)*Solve.powerMode(init.publicKey.alpha, f2, init.publicKey.p) % init.publicKey.p

    print("the tester 'check' try to verify it D = x^f1 * alpha^f2 mod p Are not, check = " + str(check))
    if(check == D): print(" => signature y on x is valid")
    else:
        print("does not match => perform the last step is to check the match")
        print("the tester concludes that y is fake if and only if:")
        print("(d.alpha^-e2)^f1 == (D.alpha^-f2)^e1 (mod p)")
        check1 = Solve.powerMode(d, f1, init.publicKey.p)*Solve.ext_gcd(init.publicKey.p, pow(init.publicKey.alpha,e2*f1)) % init.publicKey.p
        check2 = Solve.powerMode(D, e1, init.publicKey.p)*Solve.ext_gcd(init.publicKey.p, pow(init.publicKey.alpha, f2*e1)) % init.publicKey.p
        if(check1 == check2):
            print(str(check1) + " == " + str(check2))
            print("=> signature y on x is invalid")