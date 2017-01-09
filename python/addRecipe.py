#!/usr/bin/env python3

# Class that is capable of parsing a recipe file and addeding it to the webkit-justify-content

import os

class addRecipe:
    """Adds recipe to the site"""
    def __init__(self, filename):
        # Create recipe attributes
        self.recipe = None
        self.description = None
        self.image = None
        self.ingredients = None
        self.instructions = None
        self.nutrition = None

        self.parse_recipe(filename)

    # Parse the recipe file
    def parse_recipe(self, filename):
        # Open and read the entire file
        with open(filename, "r") as f:
            recipe = f.read()
            # Split the recipe into sections and parse each section
            for sections in recipe.split(os.linesep + os.linesep):
                lines = sections.split(os.linesep)
                if lines[0] == "[RECIPE]":
                    self.recipe = lines[1:]
                elif lines[0] == "[DESCRIPTION]":
                    self.description = lines[1:]
                elif lines[0] == "[IMAGE]":
                    self.image = lines[1:]
                elif lines[0] == "[INGREDIENTS]":
                    self.ingredients = lines[1:]
                elif lines[0] == "[INSTRUCTIONS]":
                    self.instructions = lines[1:]
                elif lines[0] == "[NUTRITION]":
                    self.nutrition = lines[1:]

    # Convert the recipe into an html file
    def write_recipe(self, filename):

def main():
    recipe = addRecipe("eggroll.txt")

if __name__ == "__main__":
    main()