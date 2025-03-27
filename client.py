class client():
  def __init__(self, name="", phonenum="", prefarea="", maxprice="", minrooms=""):
    self.name = name
    self.phonenum = phonenum
    self.prefarea = prefarea
    self.maxprice = maxprice
    self.minrooms = minrooms
    self.clientId = 0

  def getname(self):
    return self.name
    
  def getphonenum(self):
    return self.phonenum
    
  def getprefarea(self):
    return self.prefarea
    
  def getmaxprice(self):
    return self.maxprice
    
  def getminrooms(self):
    return self.minrooms
  