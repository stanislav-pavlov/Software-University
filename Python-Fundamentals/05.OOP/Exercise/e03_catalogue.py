class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        self.first_letter = first_letter
        sorted_by_first_letter = []
        for element in Catalogue.products:
            if element[0] == first_letter:
                sorted_by_first_letter.append(element)
        return sorted_by_first_letter

    def __repr__(self):
        asc_sorted_list = sorted(Catalogue.products)
        joined_list = "\n".join(asc_sorted_list)
        return f"Items in the {self.name}:\n{joined_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
