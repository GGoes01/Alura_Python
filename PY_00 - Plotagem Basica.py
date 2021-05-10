# # 1 - Primeiro plot

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 2.5, 4, 5.5, 3]
# plt.plot(x, y)
# plt.show()

# # 2 - Labels

# plt.title("Plot de Desempenho")
# plt.xlabel("Tempo")
# plt.ylabel("Desempenho")
# plt.legend("Desempenho")
# plt.plot(x, y)
# plt.show()

# # 3 - Ajustando a estética do plot

plt.figure(figsize=(8, 6))
plt.title("Plot de Desempenho", loc="left", fontsize=20)
plt.xlabel("Tempo", fontsize="16")
plt.ylabel("Desempenho", fontsize="16")
plt.plot(x, y, linewidth=3, c="gray")
plt.show()
