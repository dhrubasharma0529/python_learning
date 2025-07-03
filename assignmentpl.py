import mysql.connector
import requests
# fetching the data from api

url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/players?competition=8&season=2025&_limit=100"
r = requests.get(url=url)

#Database connection
connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    database = "Student"
)

mydb = connection.cursor()
try:
    if(connection):
        print("Database is connected successfully.")
        if(r.status_code == 200):
            data=(r.json()['data'])
            # data_0 = data[0]
            # print(data_0)
            #
            # Values = [(0,'Leeds United', 2 ,'leeds', 'Us', ' United States','American', 'Brenden', 'Aaronson', 'Brenden Aaronson', 11, 8, 2025, 427637, 'Midfielder','Right')]
            # mydb.executemany(sql, Values)
            # connection.commit() 

            sql_key= [] # To store the columns from the data.
            sql_value2= [] # to store the respective values.

            for i in data:

                single_player_list = {} # why not list to replace the empty columns with None values for parameter matchmaking.
                for key,value in i.items():
                
                    if type(value) == dict:
                          
                        for key1,value1 in value.items():   

                            single_player_list[key1] = value1
                            if key1 not in sql_key:
                                sql_key.append(key1)
        
                    else:
                        single_player_list[key]= value
                        if key not in sql_key:
                            sql_key.append(key)
                        
                row = tuple(single_player_list.get(col, None) for col in sql_key) # to match the column with sql_key and replace with none if not found.
                sql_value2.append(row)
        sql_key = tuple(sql_key)
        columns = ','.join(sql_key)
        placeholder = ','.join(['%s'] * len(sql_key))
        sql = f"Insert into player ({columns}) Values({placeholder})"
        mydb.executemany(sql,sql_value2)
        connection.commit()
except Exception as e:
    print(e)
finally:
    print("The Database is closed.")
    connection.close()