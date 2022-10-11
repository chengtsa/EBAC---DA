import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

gasolina_grafico = sns.barplot(data=gasolina_df, x="dia", y="venda", ci=None, palette="bright")
gasolina_grafico.set(title='Preço médio da gasolina em SP', xlabel='Dia do mês julho/2021', ylabel='Preço médio (em reais)');
plt.savefig('gasolina.png')