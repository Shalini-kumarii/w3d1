from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojos table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def survey_create(cls, data):
        query="INSERT INTO dojos (name,location,language,comment,created_at,updated_at) VALUES(%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW())";
        id = connectToMySQL('dojo_survey_schema').query_db(query,data)

        return id

    # Now we use class methods to query our database
    @classmethod
    def get_suvery(cls, data):
       
        # return Dojo(results[0])
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"

        # results is a list of dictionaries
        # list is either empty or has a length of 1, a single dictionary
        results = connectToMySQL("dojo_survey_schema").query_db(query, data)

        if len(results) == 0:
            return False

        dojo = Dojo(results[0])

        # cls()
        return dojo
    @staticmethod
    def validate_dojo(post_data):
        # this function receives the user input AKA the post data as a dictionary
        # is_valid is set to true, assuming the data is valid at the start
        is_valid = True

        if len(post_data['name']) < 2:
            flash(" Name must be at least 2 characters.")
            is_valid = False

        # if not post_data['age'].isdigit():
        #     flash("Dog Age must be a number.")
        #     is_valid = False

        if len(post_data['comment']) < 2:
            flash("comment must be at least 2 characters")
            is_valid = False

        return is_valid