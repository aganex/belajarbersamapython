# Defining the function
def print_info(nama, usia=17):
    """This function prints the entered information."""
    print("Nama: ", nama)
    print("Usia: ", usia)

# Calling the function print_info
print_info(usia=29, nama="Galih")

# Calling the function without providing the age argument
print_info(nama="Galih")