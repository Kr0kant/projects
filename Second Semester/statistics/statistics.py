import pandas
import pathlib
from pathlib import Path
import matplotlib.pyplot as plt
from scipy import stats


#work_path = pathlib.Path.cwd()
#data_path = Path(work_path, 'datasets', 'masses.csv')


masses = pandas.read_csv(r'statistics\datasets\masses.csv') #Данные с эксперимента по измерению масс номинально одинаковых грузиков
masses['experiments'].plot(kind='bar')

df = pandas.DataFrame(data={
    'Mass': masses['experiments'],
})

df.plot.kde()

plt.show()

d = df['Mass']

print(stats.kstest(d, 'norm', (d.mean(), d.std()), N=5000))
