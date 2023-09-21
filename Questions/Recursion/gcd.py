# Find the greatest common divisior for two numbers suing recursion

def gcd(a,b):
    assert int(a) == a and int(b) == b , "Values should be integer"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b 
    if b == 0:
        return a
    else:
        return gcd(b , a%b)
print(gcd(48,-18))