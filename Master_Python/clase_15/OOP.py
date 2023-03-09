# class Circle:
#     def __init__(self, radius):    # instance attribute
#         self.radius = radius
#
#     def __str__(self):
#         return str(self.radius)
#
#
# moon = Circle(1737)
#
#
# print(moon)

# num = str(2 ** 128)
#
# print(len(num))

# phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
#
# phone['OS'], phone['Color'] = ('Android'), ('Black')
#
# print(phone)

# phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
#
# vat = round((phone['Price']*.19),2)
#
# print(vat)

# my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]
#
# my_var = str(my_list[1]) + my_list[2][0] + my_list[3][3]

# languages = ['English', 'Python', 'Java', 'Golang', 'German']
#
# languages = languages[1:4]
#
# print(languages)

# my_list = list(range(-20, 8, 3))
#
# print(my_list)

# days = [10, 11, 13, 14, 15]
#
# days.insert(2, 12)
#
# print(days)

# message = 'Wow! Python is great'
# vowels = 'aeio'
#
# no_vowels = [x for x in message if x not in vowels and x != ' ']
#
# print(no_vowels)

# names1 = {'John', 'Marry', 'Lena', 'Pollux'}
# names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}
#
# names = list(names1.intersection(names2))
#
# print(names)

# phone1 = ['1111', '2222', '2222', '1111']
# phone2 = ['1111', '3333', '3333', '1111']
#
# phone_numbers = set(phone1 + phone2)
#
# print(phone_numbers)

# my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
# stringe1 = my_str.split()
# interface_mac = stringe1[0] + '!' + stringe1[4]
#
# print(interface_mac)

# def my_function(n):
#     number = n + ' + ' + n*2 + ' + ' + n*3 + ' = '
#     suma = int(n) + int(n*2) + int(n*3)
#     return number + 'wich is ' + str(suma)

# def my_function(n):
#     suma = int(n) + int(n*2) + int(n*3)
#     return suma
#
# print(my_function('5'))

# mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
#
# mac_unique = [x for x in set(mac)]
#
# print(mac_unique)

# mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
# mac_unique = []
# for x in mac:
#     if x not in mac_unique:
#         mac_unique.append(x)
#
# print(mac_unique)

# years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]
#
# years_unique = [x for x in set(years)]
#
# print(years_unique)

# words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']
#
# palindromes = [x for x in words if x.lower() == x[::-1].lower()]
#
# print(palindromes)

# list2 = [1, 2, 1, 1, 3]
# list3 = ['a', 'b', 'a', 'a', 'c', 'a', 'a', 'a', 'd']
#
# def remove_from_list(my_list, item):
#     """
#     Function that removes all accurrances of item from my_list
#     """
#     return [x for x in my_list if x != item]
#
# print(remove_from_list(list2, 1))
# print(remove_from_list(list3, 'a'))
# print(list3)

# def remove_from_list(my_list, item):
#     while (item in my_list):
#         my_list.remove(item)
#
# print(remove_from_list(list2, 1))
# print(remove_from_list(list3, 'a'))
# print(list3)

# countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']
#
# countries = [x for x in set(countries)]
# countries.sort()
#
# print(countries)

# with open('show_arp.txt') as file:
#     ip_mac = [tuple(x.split()[1:4:2]) for x in file.readlines()][1::]
# 
# print(ip_mac)

# with open('show_arp.txt', 'r', newline='') as f:
#     ## Reading file in list (each line is list element)
#     contents = f.read().splitlines()
#     print(contents)
#     ## The argument newline='' is necessary only in Windows
#
#     ## Eliminating the first item from the list (files header)
#     contents = contents[1:]
#
#     # Empty list that stores tuples like (ip, mac)
#     ip_mac = list()
#
#     # Iterating over the list(file contents) line by line
#     for line in contents:
#         ip = line.split()[1]  ## Getting the IP
#         mac = line.split()[3]  ## Getting the MAC
#
#         ## Adding the tuple to the ip_mac list
#         ip_mac.append((ip, mac))
#
#     print(contents)

# area = lambda x: x**2
# print(area(2))
# PI = 3.141592653589793
# PI = float('{0:.5f}'.format(PI))
#
# PI = float(format(PI, '.5f'))
#
# print(PI)

# countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}
#
# print({x: v for x, v in sorted(countries.items(), key=lambda x: x[0])})

# keys = sorted(countries.keys())
#
# for k in keys:
#     print(countries[k])

# salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}
#
# tax ={x: (v*.1) for x, v in salaries.items()}
#
# print(tax)



    