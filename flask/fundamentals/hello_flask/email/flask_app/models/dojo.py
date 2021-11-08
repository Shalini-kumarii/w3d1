from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def survey_create(cls, data):
        query="INSERT INTO emails (email,created_at,updated_at) VALUES(%(email)s,NOW(),NOW())";
        id = connectToMySQL('email__schema').query_db(query,data)

        return id

    # Now we use class methods to query our database
    @classmethod
    def get_suvery(cls, data):
       
        # return Dojo(results[0])
        query = "SELECT * FROM emails WHERE emails.id = %(id)s;"

        # results is a list of dictionaries
        # list is either empty or has a length of 1, a single dictionary
        results = connectToMySQL("email__schema").query_db(query, data)

        if len(results) == 0:
            return False

        dojo = Dojo(results[0])

        # cls()
        return dojo

    @staticmethod
    def validate_email(post_data):
        # this function receives the user input AKA the post data as a dictionary
        # is_valid is set to true, assuming the data is valid at the start
        is_valid = True
        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        query = "SELECT * FROM emails WHERE emails.email =%(email)s;"
        results = connectToMySQL("email__schema").query_db(query,post_data)
        if len(results) > 0:
            flash("email address exists!")
            is_valid = False
        print(results)
        
        return is_valid
        
