class Property():
    def __init__(self, managedby="", area="", bedroomno="", price="", status=""):
        self.managedby = managedby
        self.area = area
        self.bedroomno = bedroomno
        self.price = price
        self.status = status
        self.propertyId = 0

    def getmanagedby(self):
        return self.managedby
    
    def getarea(self):
        return self.area
    
    def getbedroomno(self):
        return self.bedroomno
    
    def getprice(self):
        return self.price
    
    def getstatus(self):
        return self.status
    