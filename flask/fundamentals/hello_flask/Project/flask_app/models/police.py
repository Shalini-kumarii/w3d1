from flask import flash
from flask_bcrypt import Bcrypt   
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app.models import user
from flask_app import app
from flask_app.models import crimes
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Police:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password=data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def create(cls, data):
        query="INSERT INTO polices (first_name,last_name,email,password,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())";
        id = connectToMySQL('crime_schema').query_db(query,data)

        return id

    @classmethod
    def get_all(cls):
       
        query = "SELECT * FROM polices;"
        results = connectToMySQL('crime_schema').query_db(query)

        # Create an empty list to append our instances of friends
        police= []
        for row in results:
            police.append(Police(row))
        
        return police


    @classmethod
    def get_login_by_email(cls, data):
       
        query = "SELECT * FROM polices WHERE email = %(email)s;"
        results = connectToMySQL("crime_schema").query_db(query, data)

        if len(results) < 1:
            return False

        police = Police(results[0])
        return police

    @classmethod
    def get_login_by_id(cls, data):

        query="SELECT * FROM polices Where id = %(id)s"
        results = connectToMySQL("crime_schema").query_db(query, data)

        if len(results) < 1:
            return False

        police = Police(results[0])

        return police

    
     # update
    @classmethod
    def update_Crime(cls,data):
        query = "UPDATE crime SET status= %(status)s,description= %(description)s,updated_at= now() WHERE id=%(id)s";
        print(query)
        return connectToMySQL("crime_schema").query_db(query, data)




    
    @staticmethod
    def login_validator(post_data):
        police = Police.get_login_by_email({"email": post_data["email"]})
        print (police)
        if not police:
            flash("invalid credential")
            return False

        if not bcrypt.check_password_hash(police.password ,post_data["password"]):
            flash("invalid credential")
            return False

        return True

    @staticmethod
    def validate_register(post_data):
        is_valid = True

        if len(post_data['first_name']) < 2:
            flash(" First name must be at least 2 characters.")
            is_valid = False

        if len(post_data['last_name']) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        
        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!")
            is_valid = False

        else:
            police=Police.get_login_by_email({"email": post_data['email']})
            if police:
                flash("user email already exists")
                is_valid = False

    
        if len(post_data['password']) < 8:
            flash("password must be at least 8 characters")
            is_valid = False

        if (post_data['password']) != (post_data['confirm_password']):
            flash("Password and confirm password must be matched")
            is_valid = False

        return is_valid

