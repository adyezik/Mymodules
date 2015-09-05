__all__=['IsEmail','ListedEmail']
__author__='Clavin(Martin)Adyezik - Adyezik@gmail.com'
__doc__="""
EmailChecker:
Simple Module with two function .
Check if an E-mail is valid or check for list of E-mails
"""
__name__='EmailChecker'



def IsEmail(x):
    """x must be a string
Return True if x is a Valid E-mail"""
    
    if len(x)<=6:
        return False
    
    if not'@'in x:
        return False
    
    if x.count('@')!=1:
        return False

    if x.startswith('.')or x.endswith('.'):
        return False
    
    local_part=x[:x.find('@')]
    if len(local_part)>=65:
        return False
    
    domain=x[x.find('@'):]
    
    if not'.'in domain:
        return False
    return True

def ListedEmail(x):
    """x must be a list of strings
return E-mail : boolean value"""
    for i in x:
        return (x,': ',IsEmail(x)) 
