def make_car(make, model, **additions):
    return make, model, additions


print(make_car('subaru', 'outback', color='blue', tow_package=True))
print(make_car('toyoda', 'prius', color='gray', extra_tire=True))
