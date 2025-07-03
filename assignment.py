class University():
    def __init__(self,uni,loc):
        self.uni = uni
        self.loc = loc
class Faculty(University):
    def __init__(self,uni,loc,fac,dean):
        self.fac = fac
        self.dean = dean
        super().__init__(uni,loc)
class Student(Faculty):
    def __init__(self,uni,loc,fac,dean,name,rollno,standard):
        super().__init__(uni,loc,fac,dean)
        self.name = name
        self.rollno = rollno
        self.standard = standard
      
    def fulldetails(self):
        data ={
            "uni": self.uni,
            "location":self.loc,
            "faculty": self.fac,
            "dean":self.dean,
            "name":self.name,
            "rollno":self.rollno,
            "standard":self.standard
        }
        # data['uni'] = "tu"
        return data
obj1 = Student('wrc','pokhara','math','ram','shyam',15,10)
print(obj1.fulldetails())
