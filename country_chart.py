import csv

def reader_csv(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile,delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key:value for key,value in iterable}
            data.append(country_dict)
    return data
            
def selectCountry(data,country):
    res = list(filter(lambda item: item['CCA3']==country,data))
    return res

def getPopulation(data):

    new_Dict = {
        '2022': data['2022 Population'],
        '2020': data['2020 Population'],
        '2015': data['2015 Population'],
        '2010': data['2010 Population'],
        '2000': data['2000 Population'],
        '1990': data['1990 Population'],
        '1980': data['1980 Population'],
        '1970': data['1970 Population']
    }

    print(new_Dict)

    return new_Dict


if __name__ == '__main__':
    data = reader_csv('./data.csv')
    res = selectCountry(data,'ARG')
    print(res)
    res = getPopulation(res)
    print(res)


