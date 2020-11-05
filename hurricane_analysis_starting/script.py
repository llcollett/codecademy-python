# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updated_damages(list):
	for i in range(len(list)):
		if (list[i][-1] == "M"):
			amount = list[i][:-1]
			list[i] = int(float(amount) * 1000000)
		elif (list[i][-1] == "B"):
			amount = list[i][:-1]
			list[i] = int(float(amount) * 1000000000)
	return list

updated_damages = updated_damages(damages)

# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
	hurricane_dict = {}
	for i in range(len(names)):
		name_dict = {}
		name_dict.update({"Month": months[i], "Year": years[i], "Max sustained wind": max_sustained_winds[i], "Areas affected": areas_affected[i], "Damages": damages[i], "Deaths": deaths[i]})
		hurricane_dict[names[i]] = name_dict
	return hurricane_dict

hurricanes = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# write your construct hurricane by year dictionary function here:
def hurricane_by_year(hurricanes):
	# new dictionary
	year_dict = {}
	# for every hurricane
	for key, value in hurricanes.items():
		current_year = value["Year"]
		current_hurricane = {key: value}
		year_dict[current_year] = []
		# if doesn't exist already add year
		if (current_year not in year_dict):
			year_dict[current_year] = [current_hurricane]
		else:
			year_dict[current_year].append(current_hurricane)
	# return new dictionary
	return year_dict

year_dictionary = hurricane_by_year(hurricanes)

# write your count affected areas function here:
def count_affected_areas(hurricanes):
	# new dictionary
	count_affected_areas = {}
	# for every hurricane
	for value_dict in hurricanes.values():
		for value in value_dict["Areas affected"]:
			if (value not in count_affected_areas):
				count_affected_areas[value] = 1
			else:
				count_affected_areas[value] += 1
	return count_affected_areas

count_affected_areas_dict = count_affected_areas(hurricanes)

# write your find most affected area function here:
def most_affected_area(count_affected_areas_dict):
	most_affected_area = ""
	most_affected_area_num = 0
	for key, value in count_affected_areas_dict.items():
		if (value > most_affected_area_num):
			most_affected_area_num = value
			most_affected_area = key
	return most_affected_area

most_affected_area = most_affected_area(count_affected_areas_dict)

# write your greatest number of deaths function here:
def most_number_of_deaths(hurricanes):
	most_deaths_hurricane = ""
	most_deaths = 0
	for key, value in hurricanes.items():
		if (value["Deaths"] > 0):
			most_deaths = value["Deaths"]
			most_deaths_hurricane = key
	return most_deaths_hurricane

most_deaths_hurricane = most_number_of_deaths(hurricanes)

# write your catgeorize by mortality function here:
def mortality_categories(hurricanes):
	# new dictionary
	mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
	# loop over hurricanes
	for key, value in hurricanes.items():
		if (value["Deaths"] == 0):
			mortality_dict[0].append({key: value})
		elif (0 < value["Deaths"] <= 100):
			mortality_dict[1].append({key: value})
		elif (100 < value["Deaths"] <= 500):
			mortality_dict[2].append({key: value})
		elif (500 < value["Deaths"] <= 1000):
			mortality_dict[3].append({key: value})
		elif (1000 < value["Deaths"] <= 10000):
			mortality_dict[4].append({key: value})
	return mortality_dict

mortality_categories = mortality_categories(hurricanes)

# write your greatest damage function here:
def greatest_damage(hurricanes):
	greatest_damage_hurricane = ""
	greatest_damage_amount = 0
	for key, value in hurricanes.items():
		if (value["Damages"] == "Damages not recorded"):
			pass
		elif (value["Damages"] > greatest_damage_amount):
			greatest_damage_hurricane = key
			greatest_damage_amount = value["Damages"]
	return greatest_damage_hurricane, greatest_damage_amount

greatest_damage, greatest_amount = greatest_damage(hurricanes)
print("The hurricane with the most damage was {greatest_damage} costing {greatest_amount} dollars.".format(greatest_damage = greatest_damage, greatest_amount = greatest_amount))