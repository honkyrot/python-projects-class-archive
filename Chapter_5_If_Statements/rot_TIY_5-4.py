alienColor = "red"
alienColor_2 = "green"

if alienColor_2 == "green":  # pretend I shot one down, but it's not green, this will fail.
    print("You gained 5 points!")

if alienColor == "green":
    print("You gained 5 points!")
else:  # any color other than green
    print("You gained 10 points!")
