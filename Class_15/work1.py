import matplotlib.pyplot as plt
import numpy as np

heroes = ['Prabhas', 'Pawan', 'Chiranjeevi', 'Sharukh', 'Amitabh'] #x-axis values



movies = [100,300,200,600,1000] #height of bars, valuesfor y-axis

c = ['r', 'b','k','g', 'orange']

plt.bar (heroes, movies, color=c)

plt.xlabel('Hero Name', color='b', fontsize=15)

plt.ylabel('Number of Movies', color='b', fontsize=15)

plt.title('Hero wise number of movies',color='r', fontsize=15)

plt.show()
