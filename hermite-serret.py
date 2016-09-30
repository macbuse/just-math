
#hermite-serret
#http://math.stackexchange.com/questions/5877/efficiently-finding-two-squares-which-sum-to-a-prime

#this calculates x, y so that x**2 + y**2 = p for prime p = 1 mod 4

pp = '''2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673,
677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827,
829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
'''



class Gaussian(object):
    def __init__(self,z):
        self.x, self.y = z
        
    def cmod(self,a,b):
        r = a % b 
        if 2*r > b :
            return r - b
        return r
        
        
    def __add__(self,other):
        return Gaussian( (self.x + other.x, self.y + other.y) )
    
    def __sub__(self,other):
        return Gaussian( (self.x - other.x, self.y - other.y) )
    
    
    
    def __mod__(self,other):
        if isinstance(other,int):
            return Gaussian( (self.cmod(self.x,other), self.cmod(self.y,other)) )
        
        #if isinstance(other,Gaussian):
        #    return 
        
    def __mul__(self,other):
        x1,y1 = self.x, self.y
        x2,y2 = other.x, other.y
        return Gaussian((x1*y1- x2*y2, x1*y2 + x2*y1))
    
    
    def __div__(self,other):
        if isinstance(other,int):
            tt = self - self % other
            return Gaussian( (tt.x / other, tt.y / other) )
        x1,y1 = self.x, self.y
        x2,y2 = other.x, - other.y
        rr = Gaussian((x1*y1- x2*y2, x1*y2 + x2*y1)) / abs(other)
        
        return self - rr*other
        
    
    def __abs__(self):
        return self.x**2 + self.y**2
    
    def __repr__(self):
        return repr([self.x,self.y])


z = Gaussian((5,7))
w = Gaussian((1,1))
print z / Gaussian((1,1))
print (z / Gaussian((1,1)))

    
pp = [int(x) for x in pp.split(',')]
pp = [x for x in pp if x%4 ==1]
print pp

def mods(a, n):
    if n <= 0:
        return "negative modulus"
    a = a % n
    if (2 * a > n):
        a -= n
    return a

def powmods(a, r, n):
    out = 1
    while r > 0:
        if r % 2 == 1:
            r -= 1
            out = mods(out * a, n)
        r /= 2
        a = mods(a * a, n)
    return out

def quos(a, n):
    if n <= 0:
        return "negative modulus"
    return (a - mods(a, n))/n

def grem(w, z):
    # remainder in Gaussian integers when dividing w by z
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    if n == 0:
        return "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return(w0 - z0 * u0 + z1 * u1,
           w1 - z0 * u1 - z1 * u0)

def ggcd(w, z):
    while z != (0,0):
        w, z = z, grem(w, z)
    return w


def root4(p):
    # 4th root of 1 modulo p
    if p <= 1:
        return "too small"
    if (p % 4) != 1:
        return "not congruent to 1 mod 4"
    k = p/4
    j = 2
    while True:
        a = powmods(j, k, p)
        b = mods(a * a, p)
        if b == -1:
            return a
        if b != 1:
            return "not prime"
        j += 1

def sq2(p):
    a = root4(p)
    return ggcd((p,0),(a,1))

for x in pp:
    a, b = sq2(x)
    print x, a,b , a**2 + b**2
