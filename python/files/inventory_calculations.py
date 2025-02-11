import os

print("Current working directory:", os.getcwd())


def read_file(file):
    list_of_products = []
    with open(file) as f:
        for line in f.readlines():
            list_of_products.append(line)
    return list_of_products


def calculations(list_of_products: list):
    products_dict = {}
    for product in list_of_products:
        name, quantity, price = product.split(",")
        products_dict[name] = products_dict.get(name, 0) + (
            int(quantity) * float(price)
        )
    return products_dict


def main():
    file = "products.txt"
    result = read_file(file)
    print(calculations(result))


if __name__ == "__main__":
    main()
