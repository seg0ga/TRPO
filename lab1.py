import matplotlib.pyplot as plt

threads = [1, 2, 4, 8, 16, 32, 64]
time_us = [36177369, 18057264, 8986848, 5469246, 4605549, 4350850, 4051821]

plt.plot(threads, time_us, 'o-')
plt.xlabel('Число потоков')
plt.ylabel('Время, мкс')
plt.title('Зависимость времени от числа потоков')
plt.grid(True)
plt.xscale('log', base=2)
plt.xticks(threads, [str(t) for t in threads])
plt.show()
