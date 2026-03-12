
sizes = [
    "nano","micro","small","medium","large",
    "xlarge","2xlarge","4xlarge","8xlarge",
    "16xlarge","32xlarge"
]

def print_table(headers, rows):

    col_widths = []

    for i in range(len(headers)):
        max_len = len(headers[i])

        for row in rows:
            max_len = max(max_len, len(str(row[i])))

        col_widths.append(max_len)

    def border():
        print("+", end="")
        for w in col_widths:
            print("-"*(w+2) + "+", end="")
        print()

    border()

    print("|", end="")
    for i,h in enumerate(headers):
        print(" " + h.ljust(col_widths[i]) + " |", end="")
    print()

    border()

    for row in rows:
        print("|", end="")
        for i,val in enumerate(row):
            print(" " + str(val).ljust(col_widths[i]) + " |", end="")
        print()
        border()

def recommend_ec2(instance, cpu):

    inst_type, size = instance.split(".")
    index = sizes.index(size)

    if cpu < 20:
        status = "Underutilized"

        if index == 0:
            recommended = instance
        else:
            recommended = f"{inst_type}.{sizes[index-1]}"

    elif cpu > 80:
        status = "Overutilized"

        if index == len(sizes)-1:
            recommended = instance
        else:
            recommended = f"{inst_type}.{sizes[index+1]}"

    else:
        status = "Optimized"

        latest_generation = "t3"
        recommended = f"{latest_generation}.{size}"

    return status, recommended


current_ec2 = input("Enter current EC2 instance (example: t2.large): ")
cpu_input = input("Enter CPU utilization (%): ")

cpu = int(cpu_input.replace("%",""))

status, recommended = recommend_ec2(current_ec2, cpu)

headers = [
    "Serial No.",
    "Current EC2",
    "Current CPU",
    "Status",
    "Recommended EC2"
]

rows = [
    [1, current_ec2, str(cpu)+"%", status, recommended]
]

print_table(headers, rows)