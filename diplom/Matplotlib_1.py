import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

apl_price = [123.32, 321.33, 188.3, 222.2, 545.3]
ms_price = [66.4, 44, 77, 88, 55]
msi_price = [661.4, 441, 771, 881, 689]
year = [2014, 2015, 2016, 2017, 2018]

# plt.plot(year, apl_price)
# plt.plot(year, msi_price)
# # По сути то же, но в строчку
plt.plot(year, apl_price, ':k',
         year, msi_price, '--b')
plt.scatter(year, ms_price)

plt.xlabel("Year")
plt.ylabel("Stock Price")

# Границы осей
plt.axis([2013, 2019, 40, 1000])

plt.show()

# Задаются размеры окна
fig_1 = plt.figure(1, figsize=(16, 8))
print(fig_1)

# 121 и 122 - это обозначение позиции фигуры
chart_1 = fig_1.add_subplot(224)
chart_2 = fig_1.add_subplot(221)

chart_1.plot(year, apl_price)
chart_2.scatter(year, ms_price)


plt.show()

