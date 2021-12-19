#EXERCISE 3
"""
(ii) Write a Python programming to display a horizontal bar chart of the popularity of programming Languages(Give Red colour to the bar chart).
"""

import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.barh(x_pos, popularity,color='red')

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)

plt.show()
