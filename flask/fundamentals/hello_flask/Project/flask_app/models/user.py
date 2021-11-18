from flask import flash
from flask_bcrypt import Bcrypt   
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app.models import user
from flask_app import app
from flask_app.models import crimes
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
        self.crimes = []

    # Now we use class methods to query our database
    @classmethod
    def create(cls, data):
        query="INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())";
        id = connectToMySQL('crime_schema').query_db(query,data)

        return id


    @classmethod
    def get_all(cls):
       
        query = "SELECT * FROM users;"
        results = connectToMySQL('crime_schema').query_db(query)

        # Create an empty list to append our instances of friends
        users= []
        for row in results:
            users.append(User(row))
        
        return users


    # Now we use class methods to query our database
    @classmethod
    def get_login_by_email(cls, data):
       
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("crime_schema").query_db(query, data)

        if len(results) < 1:
            return False

        user = User(results[0])
        return user

    @classmethod
    def get_login_by_id(cls, data):

        query="SELECT * FROM users LEFT JOIN crime ON users.id = crime.user_id WHERE users.id = %(id)s"
        results = connectToMySQL("crime_schema").query_db(query, data)

        if len(results) < 1:
            return False

        user = cls(results[0])
        for row_from_db in results:
            row_data = {
                "id": row_from_db["crime.id"],
                "nature_of_crime":row_from_db["nature_of_crime"],
                "address1":row_from_db["address1"],
                "address2":row_from_db["address2"],
                "county": row_from_db["county"],
                "neighborhood":row_from_db["neighborhood"],
                "pin":row_from_db["pin"],
                "description":row_from_db["description"],
                "status": row_from_db["status"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"],
                "longitude": row_from_db["longitude"],
                "latitude": row_from_db["latitude"],
                "user":user,
            }

            user.crimes.append(crimes.Crimes(row_data))

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
        
