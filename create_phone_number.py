def create_phone_number(n):
    
    return "(" + "".join(map(lambda y: str(y) ,n[0:3])) + ") " + "".join(map(lambda y: str(y) ,n[3:6])) + "-" + "".join(map(lambda y: str(y) ,n[6:])) 
