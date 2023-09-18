import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


print(df[(df['population'] >= 0) & (df['population'] <= 500)]['median_house_value'])  # вывод стоимости домов при
                                                                                      # population от 0 до 500


print(df[(df['population'] >= 0) & (df['population'] <= 500)]['median_house_value'].mean())  # вывод средней стоимости
                                                                                             # дома при population
                                                                                             # от 0 до 500

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

print(df[df['population'] == df['population'].min()]['households'].max())