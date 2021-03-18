from matplotlib import  pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West side Story"]
num_oscar = [5, 11, 3, 8, 10]

xs = [i for i, _ in enumerate(movies)]

plt.bar(xs, num_oscar)

plt.ylabel("")
plt.title("My favorite movies")

plt.xticks([i for i, _ in enumerate(movies)], movies)

plt.show()
