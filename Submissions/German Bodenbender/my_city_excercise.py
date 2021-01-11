#This is a new code for the first submission were we created a series of variables based on a city
#German Bodenbender

city_name = "Johannesburg"
city_location = "South Africa"
city_area = 90000000 # the units are in km2
city_population = 1600000 # the units are in millions
city_density = city_population/city_area
city_mayor = "Geoff Makhubo"
city_height = 1580
city_compared_population = 100000
#########################################################################

print('CITY DETAILS' + '\n')
print('City Name: ' + city_name)
print('City Location: ' + city_location)
print('City Mayor: ' + city_mayor)
print('Population Density: ' + str(city_population) + ' inhabitants per hectare')

print('\n')

if city_population > 10000000:
    print('My city is a megacity')
elif city_population > 1500000:
    print('My city is a large metropolitan area')
    if city_population > city_compared_population:
        print('My city is bigger than the compared one')
    else:
        print('My compared city is bigger than the current one')
elif city_population > 500000:
    print('My city is a Metropolitan area')
elif city_population >200000:
    print('My city is a Medium size urban area')
else: print('My city is a Small urban area')

print('\n')

if city_population > 10000000:
    print('My city is a Megacity')
elif city_population > 1500000:
    print('My city is a Large metropolitan area')
elif city_population > 500000:
    print('My city is a Metropolitan area')
elif city_population >200000:
    print('My city is a Medium size urban area')
else: print('My city is a Small urban area')



#Megacity > 10.000.000
#Large Metropolitan area > 1.500.000
#Metropolitan area > 500.000
#Meduim size urban area > 200.000
#Small urban area > 15.000