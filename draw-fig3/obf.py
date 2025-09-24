import unittest

class IIlIlllIII:

    def __init__(self):
        self.llIllIIIl = {'+': lambda I, l: I + l, '-': lambda I, l: I - l, '*': lambda I, l: I * l, '/': lambda I, l: I / l, '^': lambda I, l: I ** l}

    def llIIlIlII(self, lllIllIllI):
        lllllIllIlIll = []
        IIlIIIIlIllIII = []
        IIlIIlIllI = ''
        for lIlI in lllIllIllI:
            if lIlI.isdigit() or lIlI == '.':
                IIlIIlIllI += lIlI
            else:
                if IIlIIlIllI:
                    lllllIllIlIll.append(float(IIlIIlIllI))
                    IIlIIlIllI = ''
                if lIlI in '+-*/^':
                    while IIlIIIIlIllIII and IIlIIIIlIllIII[-1] != '(' and (self.IIlIIllIII(IIlIIIIlIllIII[-1]) >= self.IIlIIllIII(lIlI)):
                        (lllllIllIlIll, IIlIIIIlIllIII) = self.IIlIlIIIlIlIII(lllllIllIlIll, IIlIIIIlIllIII)
                    IIlIIIIlIllIII.append(lIlI)
                elif lIlI == '(':
                    IIlIIIIlIllIII.append(lIlI)
                elif lIlI == ')':
                    while IIlIIIIlIllIII and IIlIIIIlIllIII[-1] != '(':
                        (lllllIllIlIll, IIlIIIIlIllIII) = self.IIlIlIIIlIlIII(lllllIllIlIll, IIlIIIIlIllIII)
                    IIlIIIIlIllIII.pop()
        if IIlIIlIllI:
            lllllIllIlIll.append(float(IIlIIlIllI))
        while IIlIIIIlIllIII:
            (lllllIllIlIll, IIlIIIIlIllIII) = self.IIlIlIIIlIlIII(lllllIllIlIll, IIlIIIIlIllIII)
        return lllllIllIlIll[-1] if lllllIllIlIll else None

    def IIlIIllIII(self, operator):
        lIIIIIIlIIl = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return lIIIIIIlIIl.get(operator, 0)

    def IIlIlIIIlIlIII(self, lllllIllIlIll, IIlIIIIlIllIII):
        operator = IIlIIIIlIllIII.pop()
        if operator == '^':
            IIIIllII = lllllIllIlIll.pop()
            IIllIlII = lllllIllIlIll.pop()
            IlIllI = self.llIllIIIl[operator](IIllIlII, IIIIllII)
            lllllIllIlIll.append(IlIllI)
        else:
            IIIIllII = lllllIllIlIll.pop()
            IIllIlII = lllllIllIlIll.pop()
            IlIllI = self.llIllIIIl[operator](IIllIlII, IIIIllII)
            lllllIllIlIll.append(IlIllI)
        return (lllllIllIlIll, IIlIIIIlIllIII)

class lIII(unittest.TestCase):

    def lIll(self):
        lIIllIllll = IIlIlllIII()
        lII = lIIllIllll.llIIlIlII('1+2*3')
        return lII