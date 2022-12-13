import random

General_mod = 7


alice_PRIV = 3
bob_PRIV = 6


def one_way_func(Y, x, mod_size):
    """
    A one way function is very easy to calc, but hard to reverse.
    e.g: mixing paint (easy to mix, hard to unmix).
    
    Modular arithmatics has a lot of one way functions
    An example of Modular arithmatics is 12 hour time
    8 o'clock + 7 o'clock != 15 o'clock (you wouldnt say 15 o'clock)
                         ->= 3 o'clock  (You would say 3 o'clock)
    ---->8 + 5 = 3 (mod 12)<----
    """
    
    # Y^x (mod p)
    ans = (Y**x) % mod_size
    print("one_way_func: ", ans)

   
print(one_way_func(3, 4, General_mod)) 
    
def modular_calc(num:int, mod:int=General_mod):
    """
    To calculate modular maths, you can use division:
        99 mod(13) = 99/13 = 7, remainder 8
        99 = 8 (mod 13) 
    """
    
    ans = num % mod
    
    # You dont say 0 o'clock
    if ans == 0:
        ans += 1
    
    return ans


def power(x, y):
    """z=x^y"""
    z = x**y
    return z


print(modular_calc(7, 27))