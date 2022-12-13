import random

alice_PRIV = random.randint(50, 100)
bob_PRIV = random.randint(50, 100)


def modular(mod_size, x):
    """
    This is like a clock; it goes from 1 to 12 and then starts over again. 
    You would never say 17 o'clock, you would say 5 o'clock.
    The numbers go round and round in a circle.
    9+8 = 5 (mod 12) aka 9 o'clock + 8 o'clock = 5 o'clock
    ->modeular maths :D
    """

    ans = x % mod_size
    
    # modular function is used to find the remainder of a division
    # If its 0 add 1 to the answer
    if ans == 0:
        ans += 1
        print("mod_sizeular: ", ans)
        return ans
    else:
        print("mod_sizeular: ", ans)
        return ans
    
print(modular(7, 243))