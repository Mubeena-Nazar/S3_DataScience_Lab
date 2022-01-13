#EXERCISE 3
"""
(iii) Write a Python programming to display a bar chart of the popularity of programming Languages.
Use different color for each bar.
"""

import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
c=['blue','red','orange','purple','green','brown']
x_pos = [i for i, _ in enumerate(x)]

plt.barh(x_pos, popularity,color=c)

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)

plt.show()
