def save_to_file(content, file):
    with open(file, 'a') as save_1:
        save_1.write(content)


def read_file(filename):
    with open(filename, 'r') as read_1:
        print(read_1.read())


file = input("en que archivo deseas guardar tu mensaje ")
content = input("que mensaje deseas guardar? ")
filename = file

save_to_file(content, file)
read_file((filename))