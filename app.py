#!bin/bash
import csv
import MySQLdb

#Connection string should use docker environment variables

#Create database connection object

flightschedule = MySQLdb.connect(host='emiratesdb.cyxwewehppyf.eu-west-1.rds.amazonaws.com',
    user='admin',
    passwd='matango1',
    db='flightschedule')
    
#Use a cursor object to sequentially insert rows.

cursor = flightschedule.cursor()

csv_flights = csv.reader(file('flights.csv'))
for row in csv_flights:

    cursor.execute('INSERT INTO flights( Airport_ID, FName, City, Country ,IATA ,ICAO ,Destination,sheduled) '
    'VALUES("%s", "%s", "%s","%s","%s","%s","%s","%s")', 
          row)
          
#close the connection to the RDS database.
flightschedule.commit()
cursor.close()
print ("Inserts into database is done! Bye")


