# Exercise 1: Student Grades Analysis
from threading import Event

students = {
 "Alice": [85, 78, 92],
 "Bob": [79, 74, 81],
 "Charlie": [91, 82, 85],
 "David": [76, 85, 83],
 "Eve": [88, 79, 92]
}

# Use max() and min() with a custome key to find a name with the average
max_name = max(students, key=lambda name: sum(students[name]) / len(students[name]))
min_name = min(students, key=lambda name: sum(students[name]) / len(students[name]))

# calculate the actual averages for output
max_avg = sum(students[max_name]) / len(students[max_name])
min_avg = sum(students[min_name]) / len(students[min_name])



# print results
print(f"The highest average is {max_avg} by {max_name}")
print(f"The lowest average is {min_avg} by {min_name}")
print()

# Add Frank
students["Frank"] = [80, 90, 85]
print(students)
print()

# Exercise 2
inventory = {
 "apple": (50, 0.5),
 "banana": (100, 0.2),
 "orange": (75, 0.3),
 "pear": (20, 0.4)
}

# table
print(f"{'Item': <7} {'Quantity': <10} {'Price (per unit)'}")
print("-"* 35)

#print
for item, (quantity, price) in inventory.items():
 print(f"{item:<10} {quantity:<10} {price:<10}")

# total value
total_value = 0
for item, (quantity, price) in inventory.items():
 total_value += quantity * price
print(f"The total value of the inventory is: ${total_value:.2f} ")
print()

# add Mango
inventory["mango"] = (20, 0.6)

for item, (quantity, price) in inventory.items():
 print(f"{item:<10} {quantity:<10} {price:<10}")
print()

# update banana
inventory["banana"] = (120, 0.2)
for item, (quantity, price) in inventory.items():
 print(f"{item:<10} {quantity:<10} {price:<10}")
print()

# remove pear
del inventory["pear"]
for item, (quantity, price) in inventory.items():
 print(f"{item:<10} {quantity:<10} {price:<10}")
print()

# Exerices 3
employees = [
 ("John Doe", "Accounting", "john.doe@example.com"),
 ("Jane Smith", "Marketing", "jane.smith@example.com"),
 ("Emily Davis", "HR", "emily.davis@example.com"),
 ("Michael Brown", "IT", "michael.brown@example.com") ]

# table
print(f"{'Name':<15} {'Department':<15}")
print("-"*27)

# print names & departments
for names, departments, emails in employees:
 print(f"{names:<15} {departments:<15}")
print()

# sort employees by last name
sorted_employees = sorted(employees, key=lambda x: x[0].split()[-1])

# print(sorted_employees)
print(f"{'Name':<15} {'Email':<15}")
print("-"*40)

for names, department, email in sorted_employees:
 print(f"{names:<15} {email:<15}")
print()

# add a new employee
new_employee = ("Davd Wilson","Sales","david.wilson@example.com")
employees.append(new_employee)

print(f"{'Name':<15} {'Department':<15} {'Email'}")
print("-"*55)

for names, departments, emails in employees:
 print(f"{names:<15} {departments:<15} {emails}")
print()

# find Jane Smith
for names, departments, emails in employees:
 if names == "Jane Smith":
  print(f"{names}'s department is {departments}")
  break
print()

# Exercise 4
library = {
 "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
 "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
 "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
 "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

#print
print(f"{'ISBN':<20} {'Title':<25} {'Author':<17} {'Year'}")
print("-"*70)

for isbn, details in library.items():
 title = details["title"]
 author = details["author"]
 year = details["year"]
 print(f"{isbn:<20}{title:<25}{author:<20}{year}")
print()

# isbn 978-0-14-028329-7
for isbn, details in library.items():
 title = details["title"]
 author = details["author"]
 year = details["year"]
 if isbn == "978-0-14-028329-7":
  print(f"{isbn:<20}{title:<25}{author:<20}{year}")
  break
print()

# add a new book
library["978-1-4028-9462-6"] = {"title":"The Great Gatsby", "author":"F. Scott Fitzgerald", "year":1925}
for isbn, details in library.items():
 title = details["title"]
 author = details["author"]
 year = details["year"]
 print(f"{isbn:<20}{title:<25}{author:<20}{year}")
print()

# update a year
# old_moc =  "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
# new_moc =  "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1961}
# library.replace(old_moc, new_moc)

for isbn, details in library.items():
 if details["title"] == "To Kill a Mockingbird":
  details["year"] = 1961
  print(f"{isbn:<20}{details["title"]:<25}{details["author"]:<20}{details["year"]}")
  break
print()


# remove a book
del library["978-0-452-28423-4"]
for isbn, details in library.items():
 title = details["title"]
 author = details["author"]
 year = details["year"]
 print(f"{isbn:<20}{title:<25}{author:<20}{year}")
print()

# Exercise 5
cities = {
 "New York": 8419000,
 "Los Angeles": 3980000,
 "Chicago": 2716000,
 "Houston": 2328000,
 "Phoenix": 1690000
}

# user-friendly format
print(f"{'City':<20}{'Population'}")
print("-"*30)

for city, population in cities.items():
 print(f"{city:<20}{population}")
print()

# city and the highest/lowest population
high_city = max(cities, key=cities.get)
# high_city = max(cities, key=lambda city: cities[city])
low_city = min(cities, key=cities.get)

high_pop = cities[high_city]
low_pop = cities[low_city]

# print results
print(f"The highest population is {high_pop} in {high_city}")
print(f"The lowest population is {low_pop} in {low_city}")
print()

# update the population of Phoenix
cities["Phoenix"] = 1700000
for city, population in cities.items():
 print(f"{city:<20}{population}")
print()

# add a new city
cities["San Francisco"] = 884000
for city, population in cities.items():
 print(f"{city:<20}{population}")
print()

# Exercise 6
movies = {
 "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci Fi"},
 "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
 "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
 "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "C rime"},
 "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "D rama"}
}

# user-friendly format
print(f"{'Title':<20}{'Year':<10}{'Rating':<10}{'Genre'}")
print("-"*50)

for titles, details in movies.items():
 year = details["year"]
 rating = details["rating"]
 genre = details["genre"]
 print(f"{titles:<20}{year:<10}{rating:<10}{genre}")
print()

# the highest-rated movie
high_name = max(movies, key=lambda title: movies[title]["rating"])

high_rate = movies[high_name]["rating"]

print(f"The highest-rated movie is {high_name} of {high_rate}")
print()

# add a new movie
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

# update the rating
movies["Inception"]["rating"] = 9.0

# remove pulp fiction
del movies["Pulp Fiction"]

for titles, details in movies.items():
 year = details["year"]
 rating = details["rating"]
 genre = details["genre"]
 print(f"{titles:<20}{year:<10}{rating:<10}{genre}")
print()

# Exercise 7
countries = {
 "USA": "Washington, D.C.",
 "Canada": "Ottawa",
 "France": "Paris",
 "Germany": "Berlin",
 "Japan": "Tokyo"
}

# print
print(f"{'Country':<15}{'Captial'}")
print("-"*30)

for countires, capitals in countries.items():
 print(f"{countires:<15}{capitals}")
print()

# print germany
ger_cap = countries["Germany"]
print(f"The capital of Germany is {ger_cap}.")
print()

#add a new country
countries["Austrailia"] = "Canberra"
for countires, capitals in countries.items():
 print(f"{countires:<15}{capitals}")
print()

# update USA
countries["USA"] = "New Washington"
for countires, capitals in countries.items():
 print(f"{countires:<15}{capitals}")
print()

# remove france
del countries["France"]
for countires, capitals in countries.items():
 print(f"{countires:<15}{capitals}")
print()

# Exercise 8
cart = [
 {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
 {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
 {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
 {"item": "pear", "quantity": 2, "price_per_unit": 0.4} ]

print(f"{'Item':<10}{'Quantity':<10}{'Price Per Unit'}")
print("-"*35)
for details in cart:
 item = details["item"]
 quantity = details["quantity"]
 price_per_unit = details["price_per_unit"]
 print(f"{item:<10}{quantity:<10}{price_per_unit}")
print()

# total cost
total_cost = sum(item["quantity"] * item["price_per_unit"] for item in cart)
print(f"Total cost is {total_cost}.")
print()

# add a new item
cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})
for details in cart:
 item = details["item"]
 quantity = details["quantity"]
 price_per_unit = details["price_per_unit"]
 print(f"{item:<10}{quantity:<10}{price_per_unit}")
print()

# update the quantity
for details in cart:
 if details["item"] == "banana":
  details["quantity"] = 10
  print(f"{details["item"]:<10}{details["quantity"]:<10}{details["price_per_unit"]}")
print()

# remove pear
for item in cart:
 if item["item"] == "pear":
  cart.remove(item)
  break

for details in cart:
 item = details["item"]
 quantity = details["quantity"]
 price_per_unit = details["price_per_unit"]
 print(f"{item:<10}{quantity:<10}{price_per_unit}")
print()

# Exercise 9
weather = {
 "Monday": {"temperature": 20, "humidity": 60},
 "Tuesday": {"temperature": 22, "humidity": 55},
 "Wednesday": {"temperature": 19, "humidity": 65},
 "Thursday": {"temperature": 23, "humidity": 50},
 "Friday": {"temperature": 21, "humidity": 70} }

# print
print(f"{'Day':<10}{'Temperature':<15}{'Humidity'}")
print("-"*35)

for day, details in weather.items():
 temperature = details["temperature"]
 humidity = details["humidity"]
 print(f"{day:<10}{temperature:<15}{humidity}")
print()

# highest temp

high_day = max(weather, key=lambda day:weather[day]["temperature"])
high_temp = weather[high_day]["temperature"]
print(f"{high_day} has the highest temperature of {high_temp}C.")

# lowest humidity

low_day = min(weather, key=lambda day:weather[day]["humidity"])
low_hum = weather[low_day]["humidity"]
print(f"{low_day} has the lowest humidity of {low_hum:.2f}%")
print()

# update temp of wed
weather["Wednesday"]["temperature"] = 25
for day, details in weather.items():
 temperature = details["temperature"]
 humidity = details["humidity"]
 print(f"{day:<10}{temperature:<15}{humidity}")
print()

# add weather
weather["Saturday"] = {"temperature" : 24, "humidity" : 60}
for day, details in weather.items():
 temperature = details["temperature"]
 humidity = details["humidity"]
 print(f"{day:<10}{temperature:<15}{humidity}")
print()

# Exercise 10
members = [
 {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
 {"name": "Bob", "age": 30, "books_borrowed": ["The Catche r in the Rye"]},
 {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
 {"name": "David", "age": 35, "books_borrowed": ["The Grea t Gatsby"]}
]

print(f"{'Name':<10}{'Age':<10}{'Books borrowed'}")
print("-"*55)

for details in members:
 name = details["name"]
 age = details["age"]
 books_borrowed = details["books_borrowed"]
 print(f"{name:<10}{age:<10}{books_borrowed}")
print()

# find Charlie
for details in members:
 name = details["name"]
 age = details["age"]
 books_borrowed = details["books_borrowed"]
 if name == "Charlie":
  print(f"Charlie borrowed {books_borrowed}.")
print()

# add a new member
new_member = {"name":"Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]}
members.append(new_member)

# update the age of bob
for details in members:
 if details["name"] == "Bob":
    details["age"] = 31
    print(f"{details["name"]:<10}{details["age"]:<10}{details["books_borrowed"]}")
print()

# remove david
for member in members:
 if member["name"] == "David":
  members.remove(member)
  break

for details in members:
 name = details["name"]
 age = details["age"]
 books_borrowed = details["books_borrowed"]
 print(f"{name:<10}{age:<10}{books_borrowed}")
print()
