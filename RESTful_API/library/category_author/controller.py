from flask import Blueprint
from .services import (add_author_service, get_author_by_id_service, get_all_authors_service, update_author_by_id_service,
                        delete_author_by_id_service,
                       add_category_service, get_category_by_id_service, get_all_categories_service, update_category_by_id_service,
                        delete_category_by_id_service)

author = Blueprint("author", __name__)
category = Blueprint("category", __name__)


# add new author
@author.route("/author-management/author", methods = ['POST'])
def add_author():
    return add_author_service()


# get author by id
@author.route("/author-management/author/<int:id>", methods = ['GET'])
def get_author_by_id(id):
    return get_author_by_id_service(id)


# get all authors
@author.route("/author-management/authors", methods = ['GET'])
def get_all_authors():
    return get_all_authors_service()


# update author by id
@author.route("/author-management/author/<int:id>", methods = ['PUT'])
def update_author_by_id(id):
    return update_author_by_id_service(id)


# delete author by id
@author.route("/author-management/author/<int:id>", methods = ['DELETE'])
def delete_author_by_id(id):
    return delete_author_by_id_service(id)


# add new category
@category.route("/category-management/category", methods = ['POST'])
def add_category():
    return add_category_service()


# get category by id
@category.route("/category-management/category/<int:id>", methods = ['GET'])
def get_category_by_id(id):
    return get_category_by_id_service(id)


# get all categories
@category.route("/category-management/categories", methods = ['GET'])
def get_all_categories():
    return get_all_categories_service()


# update category by id
@category.route("/category-management/category/<int:id>", methods = ['PUT'])
def update_category_by_id(id):
    return update_category_by_id_service(id)


# delete category by id
@category.route("/category-management/category/<int:id>", methods = ['DELETE'])
def delete_category_by_id(id):
    return delete_category_by_id_service(id)