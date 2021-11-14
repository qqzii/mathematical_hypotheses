import matplotlib.pyplot as plt
import random


def color_generator():
    colors_tag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'F']
    color = '#'
    while True:
        color += str(random.choice(colors_tag))
        if len(color) == 7:
            break
    return color


def graph_add(x, y, color):
    plt.plot(x, y, c=color)
    plt.grid()
    plt.savefig('graph.png')


def collatz_hypothesis(x):
    iterations = []
    iteration_val = 0
    x_val = []
    while True:
        x_val.append(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = x * 3 + 1
        iterations.append(iteration_val)
        iteration_val += 1
        if x == 1:
            break

    graph_add(iterations, x_val, color_generator())


def main():

    quantity = 111

    for i in range(quantity):
        collatz_hypothesis(i+1)


if __name__ == "__main__":
    main()
