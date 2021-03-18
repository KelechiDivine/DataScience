from matplotlib import  pyplot as plt

groups = ["Group1", "Group2", "Group3", "Group4",
          "Group5", "Group6", "Group7", "Group8"]
height = [5, 20, 30, 10, 25, 35, 15, 40]

plt.bar(range(len(groups)), height)

plt.ylabel("Height group graph!")
plt.xlabel("Group chat! ")
plt.title("Our gup number! ")

plt.xticks(range(len(groups)), groups)

plt.show()
