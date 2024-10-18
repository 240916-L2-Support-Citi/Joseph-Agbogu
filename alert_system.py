import psycopg

try:
    with psycopg.connect( # Using "with" simplifies the disposal of objects after we finish our "try"
       "dbname=log_entries user=agb host=/tmp port=5432"
    ) as connection: # returns a connection object
        with connection.cursor() as my_cursor:
            my_cursor.execute("SELECT COUNT (error_levels) FROM log_entries WHERE error_levels like '%FATAL%'") # Initializing my cursor to get the count of all rows in colmn error_levels that contaims "FATAL"
            fatal_count = my_cursor.fetchone()[0]

            print (fatal_count) # Print out fatal count

            my_cursor.execute("SELECT COUNT (error_levels) FROM log_entries WHERE error_levels like '%ERROR%'") # Initializing my cursor to get the count of all rows in colmn error_levels that contaims "ERROR"
            error_count = my_cursor.fetchone()[0]

            print (error_count) # print out error_count.
            
            #: Passsing both counts through an iteration to pront alert messages
            if fatal_count >=1 and error_count >=5:
                print ("ALERT!!!!!!!!! THRESHOLD PASSED")
            
except Exception as e:
    print("Error connecting to my db: " + e)