import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=news")
        return db    
    except expression as e:
        print e
     

def most_views():
    results = []
    # Connect to the Database
    DB = connect()
    # Open a cursor to perform an operation
    cursor = DB.cursor()
    # Execute the Query
    query = """ select articles.slug, count(log.path) as views from log join articles
                on log.path like '%'||articles.slug group by articles.slug order by views desc limit 3
            """
    cursor.execute(query)
    # Fecthing the results
    data = cursor.fetchall()

    for row in data:
        results.append(row)
    
    DB.commit()
    
    # Close the cursor and the connection
    cursor.close()
    DB.close()
    
    #Output
    for result in results:
        print "{}-- {} views".format(result[0], result[1]) 


def most_popular():
    results = []
    # Connect to the Database
    DB = connect()
    # Open a cursor to perform an operation
    cursor = DB.cursor()
    # Execute the Query
    query = """ select authors.name, count(log.path) from authors join articles
                on articles.author = authors.id join log 
                on log.path like '%'||articles.slug group by authors.name order by count(log.path) desc 
            """
    cursor.execute(query)
    # Fecthing the results
    data = cursor.fetchall()

    for row in data:
        results.append(row)

    DB.commit()
    
    # Close the cursor and the connection
    cursor.close()
    DB.close()

    for result in results:
        print "{}-- {} views".format(result[0], result[1]) 


def errors():
    results = []
    # Connect to the Database
    DB = connect()
    # Open a cursor to perform an operation
    cursor = DB.cursor()
    # Execute the Query
    query = """
            select time from log where status != '200 OK' limit 10
            """
    cursor.execute(query)
    # Fecthing the results
    data = cursor.fetchall()

    for row in data:
        results.append(row)

    DB.commit()
    
    # Close the cursor and the connection
    cursor.close()
    DB.close()


    for result in results:
        print "{} -- {}% errors".format(result[0], 0) 




# most_views() 
# print "---------------------------------------"
# most_popular() 
# print "---------------------------------------"
errors()
