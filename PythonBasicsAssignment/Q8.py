import json
import csv

INPUT_FILE = "PythonBasicsAssignment/sales.json"
OUTPUT_FILE = "PythonBasicsAssignment/orders_output.csv"


def process_orders(data):

    rows = []
    customer_totals = {}

    for order in data.get("orders", []):

        order_id = order.get("order_id", "N/A")

        customer = order.get("customer", {})
        customer_name = customer.get("name", "Unknown")

        address = order.get("shipping_address", "Unknown")

        country_code = address.split(",")[-1].strip() if "," in address else "N/A"

        for item in order.get("items", []):

            product_name = item.get("name", "Unknown")
            price = float(item.get("price", 0))
            quantity = int(item.get("quantity", 0))

            total_value = price * quantity

            discount = 0
            if total_value > 100:
                discount = total_value * 0.10

            shipping_cost = quantity * 5

            final_total = total_value - discount + shipping_cost

            row = [
                order_id,
                customer_name,
                product_name,
                price,
                quantity,
                round(total_value,2),
                round(discount,2),
                shipping_cost,
                round(final_total,2),
                address,
                country_code
            ]

            rows.append(row)

            customer_totals[customer_name] = customer_totals.get(customer_name,0) + final_total

    return rows, customer_totals


def sort_by_customer_spending(rows, totals):

    return sorted(
        rows,
        key=lambda x: totals.get(x[1],0),
        reverse=True
    )


def save_to_csv(rows):

    headers = [
        "Order ID",
        "Customer Name",
        "Product Name",
        "Product Price",
        "Quantity Purchased",
        "Total Value",
        "Discount",
        "Shipping Cost",
        "Final Total",
        "Shipping Address",
        "Country Code"
    ]

    with open(OUTPUT_FILE, "w", newline="") as f:

        writer = csv.writer(f)
        writer.writerow(headers)

        for r in rows:
            writer.writerow(r)

    print("CSV file saved:", OUTPUT_FILE)


def main():

    try:
        with open(INPUT_FILE,"r") as f:
            data = json.load(f)
    except Exception as e:
        print("Error reading JSON:", e)
        return

    rows, totals = process_orders(data)

    sorted_rows = sort_by_customer_spending(rows, totals)

    save_to_csv(sorted_rows)


if __name__ == "__main__":
    main()