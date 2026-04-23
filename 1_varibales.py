my_stryng_variables = "my sting variable"
print (my_stryng_variables)

my_int_variables = "5"
print (my_int_variables)

(my_int_to_str_variable)= str(my_int_variables)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variables = "false"
print (my_bool_variables)


#concatenacion de variables en un printS
(print (my_stryng_variables, my_int_to_str_variable , my_bool_variables))
print("este es el valor de:", my_bool_variables)

#funciones del sistema
print(len(my_stryng_variables))

#variables en una sola linea
name, surname, alias, age = "diego", "jimenez", "DiegoJM", 29
print("me llamo", name, surname,"mi edad es", age,"y mi alias es:", alias)

#forzamos tipo?
address: str = "mi direccion"
address = 30
print(type(address))