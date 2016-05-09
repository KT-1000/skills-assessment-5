"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""
from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.startswith("Cor")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued != 1).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter(Brand.discontinued == 1 or Brand.founded < 1950).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()


# Fill in the following functions. (See directions for more info.)
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    # avoid collision between param year and model field year
    cur_year = year

    models_by_year = (db.session(Model.name, Model.brand_name, Brand.headquarters)
                        .join(Brand).filter_by(Model.year == cur_year)).all()

    for model in models_by_year:
        print "Model: %s Brand: %s HQ: %s" % (model[0], model[1], model[2])


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
    using only ONE database query.'''
    brands = db.session(Brand.name, Model.name).join(Model).all()
    #some kind of backref thing?

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)
# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# Datatype is a query object with returned value:
# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, braneadquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
# FROM brands
# WHERE brands.name = :name_1


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table provides a way to connect two tables that would otherwise
# have a many-to-many relationship. Its constituent parts are typically
# its own primary key, one foreign key from one table, and a second foreign
# key from the other table.
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands = []
    result = Brand.query.filter(Brand.name == mystr)

    for brand in result:
        brands_by_name = brands.append(brand)

    return brands_by_name


def get_models_between(start_year, end_year):
    # get years between start and end year
    # query db for all models in that list
    # return list of model names
    pass
