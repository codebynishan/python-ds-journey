import requests
import mysql.connector
import mysql
from datetime import datetime
# inserting data 
def insert_data(cursor,data,db):
    print(f"this mf is runned, {data}")
    try:
        query = "insert into tickers(\
            ticker,\
                ticker_name,\
                    icon,\
                        sector,\
                            point_change,\
                                percentage_change)\
            values(%s,%s,%s,%s,%s,%s);"
        parsed_data =[]
        for company in data:
            parsed_data.append(
                (
                company["ticker"],
                company["ticker_name"],
                company["icon"],
                company["sector"],
                company["point_change"],
                company["percentage_change"])
            )
        cursor.executemany(query,parsed_data)
        db.commit()
        return 0
       
    except mysql.connector.Error as e:
       
        raise(e)  
   

# fetching data 
def fetch_data(url):
    
    try:
        r = requests.get(url)
        today =datetime.today().date()
        print(today)
        if r.status_code == 200:
            data = r.json()
            return data["response"]
    except requests.exceptions.HTTPError as err:
        
        raise(f'error fetching data: {err} ')
    

        
    

def connect_db():
        db = mysql.connector.connect(
            host= "localhost",
            port =3306,
            user ="root",
            password ="Nishan@2059",
            database = "nepsemock"
        )
        
        return db

db = None 
TICKERS_API_URL ="https://www.onlinekhabar.com/smtm/search-list/tickers"

def main():
    
    try:
        db = connect_db()
        if db.is_connected:
            print("connected to database!")

        tickers_data = fetch_data(TICKERS_API_URL)
       

        # saving to database
        cursor =db.cursor()
        row = insert_data(cursor,tickers_data,db)  
        if row == 0:
            print("data succesfully inserted to db!!!")
            
    except mysql.connector.Error as e:
        print(f"error connecting db: {e.msg}")
    except Exception as err:
        print(f'something went wrong: {err}')
    finally:
        if db and db. is_connected:
            db.close()
            

# entry point 

main()

    


