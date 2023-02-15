import init
import Solve

class Sign:
    y = 1
sign = Sign()
def signing():
    print("------Make a signature------")
    sign.y = Solve.powerMode(init.doc.x, init.privateKey.a, init.publicKey.p)
    print("signature on text x: y = sigk(x) = " + str(sign.y))