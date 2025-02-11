import os
print("Current working directory:", os.getcwd())

def read_file(file):

    with open(file) as f:
        return f.read()


def main():
    file = "products.txt"
    result = read_file(file)
    print(result)


if __name__ == "__main__":
    main()
