from flask import flash
from flask_bcrypt import Bcrypt   
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app.models import user

from flask_app import app
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Crimes:
    def __init__( self , data ):
        self.id = data['id'] 
        self.nature_of_crime = data['nature_of_crime']
        self.address1 = data['address1']
        self.address2 = data['address2']
        self.county = data['county']
        self.neighborhood = data['neighborhood']
        self.pin = data['pin']
        self.description = data['description']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.longitude = data['longitude']
        self.latitude = data['latitude']
     
        if "user" in data:                                       # for one display by id
            self.user = data['user']
        else:
            self.user= user.User.get_login_by_id({"id":data['user_id']})

    # create
    @classmethod
    def create(cls,data):
        print("inside create")
        query="INSERT INTO crime(nature_of_crime,address1,address2,county,neighborhood,pin,description,status,created_at,updated_at,longitude,latitude,user_id) VALUES(%(nature_of_crime)s,%(address1)s,%(address2)s,%(county)s,%(neighborhood)s,%(pin)s,%(description)s,%(status)s,NOW(),NOW(),%(longitude)s,%(latitude)s,%(user_id)s)";
        results = connectToMySQL('crime_schema').query_db(query,data)

        return results


    #read many
    @classmethod
    def get_all(cls):
        
        query = "SELECT * FROM crime;"
       
        results = connectToMySQL('crime_schema').query_db(query)
        users = []

        # Iterate over the db results and create instances of friends with cls.
        for row in results:
        # users.append( cls(user) )

            users.append(Crimes(row))
        return users


    #read one
    @classmethod
    def get_one(cls,data): 
        query = "SELECT * FROM crime WHERE id = %(id)s;"
        results = connectToMySQL("crime_schema").query_db(query, data)

        if len(results) < 1:
            return False

        crime= Crimes(results[0])
        return crime

    @classmethod
    def get_crime_data_with_userid(cls,data): 
        query = "SELECT * FROM crime WHERE user_id = %(user_id)s;"
        results = connectToMySQL("crime_schema").query_db(query, data)
        crimes= []
        for row in results:
            crimes.append(Crimes(row))
        
        return crimes

#read one
    @classmethod
    def get_crime_data(cls,data): 
        query = "SELECT * FROM crime WHERE neighborhood = %(neighborhood)s;"
        results = connectToMySQL("crime_schema").query_db(query, data)

        # if len(results) < 1:
        #     return False

        crimes= []
        for row in results:
            crimes.append(Crimes(row))
        
        return crimes

    # update
    @classmethod
    def update(cls,data):
        query = "UPDATE crime SET nature_of_crime= %(nature_of_crime)s,address1=%(address1)s,address2=%(address2)s,county=%(county)s,neighborhood=%(neighborhood)s,pin=%(pin)s,description=%(description)s,updated_at= now() WHERE id=%(id)s";
        print(query)
        return connectToMySQL("crime_schema").query_db(query, data)


    # delete
    @classmethod
    def delete(cls,data):
        query = "DELETE from crime where id = %(id)s"
        connectToMySQL("crime_schema").query_db(query, data)


    # validate create
    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['address1'])< 2:
            flash("address must be two characters")
            is_valid = False
        
        if len(post_data['address2'])< 4:
            flash("address must be four characters")
            is_valid = False
        if len(post_data['pin'])< 5:
            flash("pin must be 5 digit")
            is_valid = False

        if len(post_data['description'])< 4:
            flash("description must be four characters")
            is_valid = False

        print (post_data)
        if len(post_data['longitude'])< 4:
            flash("Location access denied can't file the report. please click on allow")
            is_valid = False

        return is_valid


# valide update
    @staticmethod
    def validate_update(post_data):
        is_valid = True

        if len(post_data['address1'])< 2:
            flash("address must be two characters")
            is_valid = False
        
        if len(post_data['address2'])< 4:
            flash("address must be four characters")
            is_valid = False
        if len(post_data['pin'])< 5:
            flash("pin must be 5 digit")
            is_valid = False

        if len(post_data['description'])< 4:
            flash("description must be four characters")
            is_valid = False

        return is_valid

