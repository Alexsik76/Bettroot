from matplotlib import pyplot as plt
from vehicles2 import classes_of_cars


def statistic(data):
    list_of_power = []
    for line in data:
        list_of_power.append(line[2])
        for item in stand_objects:
            if item.comparison(line):
                list_of_founded['IN ALL'] += 1
                list_of_founded[item.__class__.__name__] += 1
                break
    x = list(list_of_founded.values())[1:]
    s = list(list_of_founded.keys())[1:]
    fig, (ax1, ax2) = plt.subplots(
        nrows=1, ncols=2,
        figsize=(8, 4)
    )

    ax1.pie(x, labels=s, shadow=True, autopct='%1.1f%%')
    ax1.set_title('All vehicles2')
    ax2.scatter(x=range(1000), y=list_of_power, marker='o', c='g', edgecolor='b')
    ax2.set_title('Scatter: Powers of vehicles2')
    ax2.set_xlabel('vehicles2')
    ax2.set_ylabel('power')

    plt.show()
