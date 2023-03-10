# Pide al usuario una lista de países separados por comas
input_countries = input("Ingrese una lista de países separados por comas: ")

# Separa los países en una lista y elimina posibles los espacios en blanco
country_list = [country.strip() for country in input_countries.split(',')]

# Elimina paises duplicados usando un set y convierte el resultado a lista
country_list = list(set(country_list))

# Ordena la lista de países alfabeticamente
country_list.sort()

# Muestra la lista de países ordenada y separada por comas
print("Lista de países ordenada alfabeticamente: ", end="")
print(", ".join(country_list))