favorite_places = {"Alex": ["The Baseball Field (Wrigley Field in Chicago",
                            "The Beach (Fernandina Beach in Florida",
                            "FWCS Career Academy in Indiana"],
                   "Hong": ["FWCS Career Academy in Indiana",
                            "My home",
                            "Indiana Dune Beach"],
                   "Whopper": ["burger king"]}

for key0, data0 in favorite_places.items():
    print(f"\n{key0}'s favorite places are:")
    for data1 in data0:
        print(data1)
