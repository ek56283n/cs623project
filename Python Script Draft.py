
import psycopg2
from tabulate import tabulate

print("Beginning")

# Change the credentials and the name of the database
# create table student(id integer, name varchar(10), primary key(id))

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="@lphaSapphire2018!")

print(con)

#For isolation: SERIALIZABLE
con.set_isolation_level(3)

#For atomicity
con.autocommit = False

try:
    cur = con.cursor()
    # QUERY
    cur.execute("DELETE FROM depot WHERE depid = 'd1' ")

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")

print("End")
