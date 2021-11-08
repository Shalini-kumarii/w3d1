from flask import flash
from flask_bcrypt import Bcrypt   
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import app
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
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
        query="INSERT INTO registers (first_name,last_name,email,password,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())";
        id = connectToMySQL('login_schema').query_db(query,data)

        return id


    @classmethod
    def get_all(cls):
       
        query = "SELECT * FROM registers;"
        # results is a list of dictionaries
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_schema').query_db(query)

        # Create an empty list to append our instances of friends
        users= []

        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            users.append(User(row))
        
        return users


    # Now we use class methods to query our database
    @classmethod
    def get_login_by_email(cls, data):
       
        # return Dojo(results[0])
        query = "SELECT * FROM registers WHERE email = %(email)s;"

        # results is a list of dictionaries
        # list is either empty or has a length of 1, a single dictionary
        results = connectToMySQL("login_schema").query_db(query, data)

        if len(results) < 1:
            return False

        user = User(results[0])

        # cls()
        return user

    @classmethod
    def get_login_by_id(cls, data):
        query = "SELECT * FROM registers WHERE id = %(id)s;"
        results = connectToMySQL("login_schema").query_db(query, data)

        if len(results) < 1:
            return False

        user = User(results[0])

        # cls()
        return user

   

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
            user=User.get_login_by_email({"email": post_data['email']})
            if user:
                flash("user email already exists")
                is_valid = False

    
        if len(post_data['password']) < 8:
            flash("password must be at least 8 characters")
            is_valid = False

        if (post_data['password']) != (post_data['confirm_password']):
            flash("Password and confirm password must be matched")
            is_valid = False

        return is_valid

    @staticmethod
    def login_validator(post_data):
        user = User.get_login_by_email({"email": post_data["email"]})
        print (user)
        if not user:
            flash("invalid credential")
            return False

        if not bcrypt.check_password_hash(user.password ,post_data["password"]):
            flash("invalid credential")
            return False

        return True
        
