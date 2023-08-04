import numpy as np

class Material:
    def __init__(self, name, molecular_weight, quantity_grams):
        self.name = name
        self.molecular_weight = molecular_weight
        self.quantity_grams = quantity_grams

    def molar_quantity(self):
        return self.quantity_grams / self.molecular_weight

    def __str__(self):
        return f"{self.name} (Molecular Weight: {self.molecular_weight} g/mol, Quantity: {self.quantity_grams} g, Moles: {self.molar_quantity()} mol)"


class Reaction:
    def __init__(self, reactants, products, stoichiometry):
        self.reactants = reactants
        self.products = products
        self.stoichiometry = stoichiometry

    def perform_reaction(self):
        reactant_moles = [r.molar_quantity() for r in self.reactants]
        limiting_reactant_index = np.argmin(np.array(reactant_moles) / np.array(self.stoichiometry['reactants']))
        limiting_reactant = self.reactants[limiting_reactant_index]
        reaction_ratio = limiting_reactant.molar_quantity() / self.stoichiometry['reactants'][limiting_reactant_index]

        # Update quantities
        for i, reactant in enumerate(self.reactants):
            reactant.quantity_grams -= reaction_ratio * self.stoichiometry['reactants'][i] * reactant.molecular_weight

        for i, product in enumerate(self.products):
            product.quantity_grams += reaction_ratio * self.stoichiometry['products'][i] * product.molecular_weight


class RawMaterials:
    def __init__(self):
        self.materials = {}

    def add_material(self, material):
        self.materials[material.name] = material

    def get_material(self, name):
        return self.materials.get(name)

    def list_materials(self):
        for material in self.materials.values():
            print(material)