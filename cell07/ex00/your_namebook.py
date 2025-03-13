

def array_of_names(name_dict):
    full_names = [f"{first.capitalize()} {last.capitalize()}" for first, last in name_dict.items()]
    return full_names


names = {
    "john": "doe",
    "jane": "smith",
    "alice": "johnson"
}

full_names_list = array_of_names(names)
print(full_names_list)