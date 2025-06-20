def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


print("This is a calculator module.")
if __name__ == "__main__":
    print("Running the calculator module directly.")
else:
    print("Importing the calculator module.")
    print("Addition:", add(5, 3))
