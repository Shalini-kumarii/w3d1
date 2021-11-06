# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
# model the class after the dojos table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
       
        query = "SELECT * FROM dojos;"
        # results is a list of dictionaries
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)

        # Create an empty list to append our instances of friends
        dojos = []

        # Iterate over the db results and create instances of friends with cls.
        for row in results:
           # users.append( cls(user) )

            dojos.append(Dojo(row))
        
        return dojos

    # Now we use class methods to query our database
    @classmethod
    def get_one(cls, data):
       
        # return Dojo(results[0])
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        # results is a list of dictionaries
        # list is either empty or has a length of 1, a single dictionary
        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)

        if len(results) == 0:
            return False

        dojo = Dojo(results[0])

        if results[0]["ninjas.id"] != None:
            for row in results:
                ninjaData = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at'],
                    "dojo_id": row["dojo_id"]
                }
                print(ninjaData)
                dojo.ninjas.append(Ninja(ninjaData))

        # cls()
        return dojo

    @classmethod
    def create(cls,data):     # data is dictionary holds post info
        query="INSERT INTO dojos (name,created_at,updated_at) VALUES(%(name)s,NOW(),NOW())";
        results = connectToMySQL('dojos_ninjas_schema').query_db(query,data)

        return results

    # UPDATE
    @classmethod
    def update(cls, data):
        # data is a dictionary that holds the post information AND the id of the dog we are updating
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"

        # results from a insert query gives us the ID of the updated dog
        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)

        return results

        
    # DELETE
    @classmethod
    def delete(cls, data):
        # data is still a dictionary, but it only holds {"id": the_number}
        query = "DELETE FROM dojos WHERE id = %(id)s;"

        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)

        return results