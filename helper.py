from math import ceil

if __name__.endswith("__main__"):
    base_y = 200

    with open("order.txt", "r") as file:
        lines = file.readlines()
        rows = ceil((len(lines)-9)/9) + 1
        print(f"image height: {base_y*2 + (rows)*(128 + 47) - 47}")

    input()