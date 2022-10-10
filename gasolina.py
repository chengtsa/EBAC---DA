import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

gasolina_grafico = sns.barplot(data=gasolina_df, x="dia", y="venda", ci=None, palette="pastel")
gasolina_grafico.set(title='Preço médio da gasolina em São Paulo', xlabel='Dia do mês de julho', ylabel='Preço médio (R$)');
plt.savefig('gasolina.png')