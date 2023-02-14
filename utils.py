def get_info_country(data,country):
    dataCountry = list(filter(lambda item: item['CCA3']==country,data))
    return dataCountry

def get_population(data):
    population_dict = {
        '2022' : int(data['2022 Population']),
        '2020' : int(data['2020 Population']),
        '2015' : int(data['2015 Population']),
        '2010' : int(data['2010 Population']),
        '2000' : int(data['2000 Population']),
        '1990' : int(data['1990 Population']),
        '1980' : int(data['1980 Population']),
        '1970' : int(data['1970 Population'])
    }
    return population_dict

def get_column (data):
    dataCountryValues = []
    dataCountryLabels = []

    country = list(map(lambda i : i['CCA3'],data))
    percentage = list(map(lambda i : i['World Population Percentage'],data))
    """for i in data: 
        dataCountryValues.append(i['World Population Percentage'])
        dataCountryLabels.append(i['CCA3'])"""
    print(country)
    print(percentage)

    return country,percentage


