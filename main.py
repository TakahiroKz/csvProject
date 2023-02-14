import utils as ut
import readCSV as rcsv
import chart as ct

def run(path, country): #Si desde otro modulo llamo esta funcion se ejecutara
    labels = []
    values = []
    labels1 = []
    values1 = []
    print("Generando informacion correspondiente al pais seleccionado: ")
    dictCsv = rcsv.read_csv(path)
    countryInfo = ut.get_info_country(dictCsv, country)
    if len(countryInfo[0]) > 0:
        countryInfo = countryInfo[0]
        countryPopulation = ut.get_population(countryInfo)
        for key, value in countryPopulation.items():
            labels.append(key)
            values.append(value)
        print(countryPopulation)
        ct.generate_pi_chart(values, labels,country)
        ct.generate_bar_chart(labels,values,country)

    print("Generando informacion correspondiente a la columna: ")
    country,percentage = ut.get_column(dictCsv)
    ct.generate_pi_chart(country,percentage)
    ct.generate_bar_chart(country, percentage)
    

if __name__ == '__main__': #Desde aqui si ejecuto el modulo main ejecutara la funcion
    country = input("Buscar pais por codigo CCA3: ")
    country = country.upper()
    run('./data.csv', country)



    