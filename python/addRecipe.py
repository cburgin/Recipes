#!/usr/bin/env python3

# Class that is capable of parsing a recipe file and addeding it to the webkit-justify-content

import configparser

class addRecipe:
    """Adds recipe to the site"""
    def __init__(self, filename):
        pass

    #Uses configparser to parse a recipe and store it in an intermediate format
    def parse_recipe(self):
        config = configparser.ConfigParser()
