import requests
import mysql.connector
import mysql
def insert_data(cursor,data,db):
    try:
        query = "insert into trending(\
            ticker,\
                ticker_name,\
                    latest_price,\
                        points_change,\
                            percentage_change,\
                                traded_of_mkt_cap)\
            values(%s,%s,%s,%s,%s,%s);"
        parsed_data =[]
        for company in data:
            parsed_data.append(
                (company["ticker"],
                company["ticker_name"],
                company["latest_price"],
                company["points_change"],
                company["percentage_change"],
                company["traded_of_mkt_cap"])
            )
        cursor.executemany(query,parsed_data)
        db.commit()
        return 0
       
    except mysql.connector.Error as e:
        raise(e)     
    
def fetch_data(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data
    except requests.exceptions.HTTPError as err:
        raise(f'error fetching data: {err} ')
        
db = None 
TRENDING_API_URL = "https://www.onlinekhabar.com/smtm/home/trending"
  
try:
    db = mysql.connector.connect(
        host= "localhost",
        port =3306,
        user ="root",
        password ="Nishan@2059",
        database = "nepsemock"
    )
    
    if db.is_connected:
        print("db connected....")

    trending_result= fetch_data(TRENDING_API_URL)
    trending_data =trending_result['response']

    # saving to database
    cursor =db.cursor()
    row = insert_data(cursor,trending_data,db)  
    if row == 0:
        print("data succesfully inserted to db!!!")
except mysql.connector.Error as e:
    print(f"error connecting db: {e.msg}")
except Exception as err:
    print(f'something went wrong: {err}')
finally:
    if db and db. is_connected:
        db.close()


    


