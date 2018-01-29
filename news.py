import psycopg2

query1 = """select articles.slug, count(*) as views from log join articles
            on log.path like '%'||articles.slug where log.status = '200 OK'
            group by articles.slug order by views desc limit 3;"""

query2 = """select authors.name, count(*) as views from authors join articles
            on articles.author = authors.id join log
            on log.path like '%'||articles.slug where log.status = '200 OK'
            group by authors.name order by views desc;"""

query3 = """select date, errorperc
            from
            (select date,  (
                sum(views)/(select count(*)
                from log where to_char( log.time,'MON,DD,YYYY' ) = date
                ) * 100
            ) as errorperc
            from
            (select to_char(log.time,'MON,DD,YYYY') as date, count(*) as views
            from log where status != '200 OK' group by date ) as percentage
            group by date order by errorperc desc )
                    as result
            where errorperc >= 1
 """


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=news")
        return db
    except expression as e:
        print e


def command(query):
    results = []
    # Connect to the Database
    DB = connect()
    # Open a cursor to perform an operation
    cursor = DB.cursor()
    # Execute the Query
    cursor.execute(query)
    # Fecthing the results
    data = cursor.fetchall()

    for row in data:
        results.append(row)

    DB.commit()

    # Close the cursor and the connection
    cursor.close()
    DB.close()

    return results

for result in command(query1):
    print "{} -- {} views".format(result[0], result[1])

print "---------------------------------------"

for result in command(query2):
    print "{} -- {} views".format(result[0], result[1])

print "---------------------------------------"

for result in command(query3):
    print "{} -- {} % of errors".format(result[0], result[1])
