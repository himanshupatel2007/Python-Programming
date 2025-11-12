name = "Himanshu"
age = 18
cgpa = 7.9
student = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(student))

#Explicit Typecasting
print("Explicit Type Casting")

new_name = bool(name)
print(type(new_name))

new_age = bool(age)
print(type(new_age))

new_age = str(age)
print(type(new_age))

new_age = float(age)
print(type(new_age))

new_cgpa = int(cgpa)
print(type(new_cgpa))

new_cgpa = str(cgpa)
print(type(new_cgpa))

new_cgpa = bool(cgpa)
print(type(new_cgpa))

new_student = str(student)
print(type(new_student))

new_student = int(student)
print(type(new_student))

new_student = float(student)
print(type(new_student))

#Implicit Typecasting
print("Implicit Type Casting")

x = 10
y = 23.4

z= y/x

print(z)