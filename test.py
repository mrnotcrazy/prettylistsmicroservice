import time

def write_to_file(content):
    with open("list.txt", 'w') as file:
        file.write(content)

def test_microservice():
    # Test with "list:"
    write_to_file("list: apple, orange, limabeans")
    time.sleep(2)  # Wait for the microservice to process
    with open("list.txt", 'r') as file:
        print("list: output:\n", file.read())

    # Test with "list0:"
    write_to_file("list0: one, two, three")
    time.sleep(2)
    with open("list.txt", 'r') as file:
        print("list0: output:\n", file.read())

    # Test with "list1:"
    write_to_file("list1: one, two, three")
    time.sleep(2)
    with open("list.txt", 'r') as file:
        print("list1: output:\n", file.read())

    # Test with "list2:"
    write_to_file("list2: one, two, three")
    time.sleep(2)
    with open("list.txt", 'r') as file:
        print("list2: output:\n", file.read())

if __name__ == "__main__":
    test_microservice()
