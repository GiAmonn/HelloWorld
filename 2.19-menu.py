try:
    menu = {
    "Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50,
    "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50,
    "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00
}
    itemcost = 0
    while True:
        item = float(menu[input("choose item: ")])
        itemcost = itemcost + item

except EOFError:
    print(f"Total cost is: {itemcost:.2f}$")