
import numpy as np
import matplotlib.pyplot as plt

# Визначаємо діапазон x
x = np.linspace(-2, 5, 400)
# Обчислюємо Y(x)
y = x * np.sin(5 * x)

# Створюємо графік
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$Y(x) = x \sin(5x)$', color='blue')
plt.title('Графік функції Y(x) = x * sin(5x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()

# Зберігаємо графік у файл .png
plt.savefig('function_graph.png')

# Відображаємо графік
plt.show()
