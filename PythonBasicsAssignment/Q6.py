import csv

def visualize_csv_table(filename):

    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            rows.append(row)

    col_widths = []

    num_cols = len(rows[0])

    for col in range(num_cols):

        max_len = 0

        for row in rows:

            if len(row[col]) > max_len:
                max_len = len(row[col])

        col_widths.append(max_len)

    def print_border():

        print("+", end="")

        for width in col_widths:
            print("-" * (width + 2) + "+", end="")

        print()

    
    print_border()

    for row in rows:

        print("|", end="")

        for i, cell in enumerate(row):

            print(" " + cell.ljust(col_widths[i]) + " |", end="")

        print()

        print_border()


filename = input("Enter CSV file name: ")

visualize_csv_table(filename)