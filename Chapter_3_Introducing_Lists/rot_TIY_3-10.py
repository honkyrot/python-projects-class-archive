cities = [
    "Fort Worth",
    "Chicago",
    "Indianapolis",
    "Huntertown",
    "Detroit"
]
print(f"\n{cities}")

cities[0] = "Fort Wayne" # whoops i ment Fort wayne
print(f"\n{cities} item change")

cities.insert(0,"Wabash")       #insert
print(f"\n{cities} insert()")

cities.append("New Haven")      #append
print(f"\n{cities} append()")

cities.reverse()                #reverse
print(f"\n{cities} reverse()")

cities.sort()                   #sort()
print(f"\n{cities} sort()")

cities.sort(reverse=True)       #reverse sort
print(f"\n{cities} reverse sort()")

print(f"\n{sorted(cities)} sorted()")   # uses sorted()

print(f"\n{sorted(cities,reverse=True)} sorted() in reverse")   # uses sorted() to reverse

print(f"\n{cities} is the current city list")
popedCity = cities.pop()        #pop a city
print(f"\n{popedCity} was popped!")

popedCity = cities.pop(0)        #pop the first city
print(f"\n{popedCity} was popped!")

cities.remove("Detroit") # rip Detroit
print(f"\n{cities}, removed Detroit")

print(f"\nthere are currently {len(cities)} cities right now") #length

