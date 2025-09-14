def make_shirt(size, message):
    if size == "L":
        print(f"The shirt's size is {size} and its front message is \"I Love Python!\"")
    else:
        print(f"The shirt's size is {size} and its front message is \"{message}\"")


make_shirt(size="S", message="Balls")
make_shirt(size="L", message="Balls2")
