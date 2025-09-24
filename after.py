class class1:
  def __init__(self, var1, var2) -> None:
    self.var1 = var1
    self.var2 = var2
    self.var3 = self.method1()
    self.var4 = self.method2()
    self.var5 = 0
  def method1(self):
    var6 = [[0 for var7 in range(self.var1)] for var8 in range(self.var1)]
    for var9 in range(self.var2):
      var10 = random.randint(0, self.var1 - 1)
      ...
  def method2(self): ...
  def method3(self, map): ...
  def method4(self, var10, var11): ...