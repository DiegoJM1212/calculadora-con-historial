#strings#

my_string ="mi string"
my_0ther_string ="mi string"

print(len(my_string))
print(len(my_0ther_string))

print(my_string+ " " + my_0ther_string)

my_new_line_string = "este es un string\nconsalo de linea"
print(my_new_line_string)

my_tab_string ="\teste es un string con abulacion"
print(my_tab_string)

my_scape_string ="\teste es un string \n escapado"
print(my_scape_string)

#formateo

name, surname, edad = "Diego", "Jimenez", 29

print("mi nombre es {} {} y mi edad es {}".format(name, surname, edad) )
print("mi nombre es %s %s y mi edad es%d"  %(name, surname, edad))
print(f"mi nombre es {name} {surname} y mi edad es {edad}" )

#desempacateado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

#division 

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)


language_slice = language[0:6:2]
print(language_slice)

#reverse
reversed_lenguage = language[::-1]
print(reversed_lenguage)

#funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())

print(language.upper().isupper())
print(language.startswith("py"))
