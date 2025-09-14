cities = {"Fort Wayne": {"country": "Indiana", "pop": "268.3K", "fact": "Fort Wayne was named after Anthony Wayne."},
          "Chicago": {"country": "Illinois", "pop": "2.7M", "fact": "Its a city on Lake Michigan."},
          "Lotsee": {"country": "Oklahoma", "pop": "6", "fact": "Its the smallest city in the US."}}

for key0, data0 in cities.items():
    print(f"\nCity of {key0}:")
    print(f"In the state of {data0['country']}.")
    print(f"Has a population of {data0['pop']}.")
    print(f"Fact: {data0['fact']}.")
