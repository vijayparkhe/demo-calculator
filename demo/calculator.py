

class Democalculator:
    def addition(self,num1,num2):
        if type(num1) == int and type(num2) == int:
            if num1<0 or num2<0:
                return "Only Positive numbers are allowded"
            else:
                result = num2+num1
                return result
        else:
            raise Exception("Invalid Parameter")

    
    def authentication(self,username,password):
        if username and password :
            if len(username)>=3 and len(password)>=3:
                if username == "Vijay" and password == "Vijay123":
                    return "Login Successfully"
            else:
                raise Exception ("Invalid Length of username and password")
        else:
            raise Exception ("Invalid username and password")

