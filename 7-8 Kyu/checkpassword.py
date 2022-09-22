def alphanumeric(password):
    if len(password) < 1:
        return False
    for c in password:
        if not(c.isalpha() or c.isdigit()):
            return False
    return True
    pass
    
if __name__ == "__mian__":
    check()
