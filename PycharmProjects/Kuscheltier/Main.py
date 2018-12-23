import psycopg2

class Main(object):
    hostname = 'localhost'
    username = 'vinc'
    password = 'vinc'
    database = 'teddy'

    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)


    curr = myConnection.cursor()
    print(curr.execute("""SELECT * FROM medikamente"""));

    myConnection.close()


if __name__ == '__main__'():
    Main();
