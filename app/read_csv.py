import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data


def read_data_by_country(data, country):
  result = list(
      filter(lambda item: item['Country/Territory'].lower() == country.lower(),
             data))
  population_by_year = {
      key.split()[0]: value
      for key, value in result[0].items() if key in [
          '2022 Population', '2020 Population', '2015 Population',
          '2010 Population', '2000 Population', '1990 Population',
          '1980 Population', '1970 Population'
      ]
  }
  return population_by_year

  print(population_by_year)


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  #print(data[9])
  read_data_by_country(data, 'Colombia')
