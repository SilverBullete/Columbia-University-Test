class FamersMarket():
    def __init__(self, FMID, name, web, address, city, zip, x, y):
        self.FMID = int(FMID)
        self.name = name
        self.web = web
        self.address = address
        self.city = city
        self.zip = zip
        self.x = float(x)
        self.y = float(y)
    def __eq__(self, other):
        if self.FMID == other.FMID:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.FMID != other.FMID:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.FMID > other.FMID:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.FMID < other.FMID:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.FMID >= other.FMID:
            return True
        else:
            return False
    def __le__(self, other):
        if self.FMID <= other.FMID:
            return True
        else:
            return False


    def set_x(self,x):
        if x<=-180 or x>=-40:
            return False;
        else:
            return x
    def set_y(self,y):
        if y<=10 or y>=80:
            return False;
        else:
            return y
    def error_x(self,response):
        if response == False:
            print("\"Invalid x coordinate: {0}\".format(x)")
    def error_y(self,response):
        if response == False:
            print("\"Invalid y coordinate: {0}\".format(y)")





