def fcn_bisiesto(n):
    print(__name__)
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
if __name__=="__main__":
    print(fcn_bisiesto(2015))
    
