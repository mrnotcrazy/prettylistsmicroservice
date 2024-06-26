import os
import time

# Set TEST_MODE to True or False
TEST_MODE = True

def process_list(content):
    if content.startswith("list:"):
        items = content[5:].strip().split(", ")
        return "\n".join(f"{i + 1}:{item.capitalize()}" for i, item in enumerate(items))
    elif content.startswith("list0:"):
        items = content[6:].strip().split(", ")
        return "\n".join(f"-------\n|{item.ljust(6)}|" for item in items) + "\n-------"
    elif content.startswith("list1:"):
        items = content[6:].strip().split(", ")
        return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
    elif content.startswith("list2:"):
        items = content[6:].strip().split(", ")
        # Example of another format, can be customized as needed
        return "\n".join(f"--> {item}" for item in items)
    else:
        return 0#do nothing

def read_and_process_file(filename):
    if not os.path.exists(filename):
        return

    with open(filename, 'r') as file:
        content = file.read().strip()

    if content:

        output = process_list(content)
        if output == 0:
            pass
        else:
            if TEST_MODE:
                print("Content read from file:")
                print(content)
            if TEST_MODE:
                print("Content after writing to file:")
                print(output)
            with open(filename, 'w') as file:
                file.write(output)

def main():
    filename = "list.txt"
    while True:
        read_and_process_file(filename)
        time.sleep(1)  # Adjust as needed

if __name__ == "__main__":
    main()
