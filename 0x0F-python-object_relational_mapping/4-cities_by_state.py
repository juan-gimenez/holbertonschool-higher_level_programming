#!/usr/bin/python3
"""
list if name equal to arg
"""
"""
not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    import sys

    datac = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3])
    curs = datac.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id;")
    fall = curs.fetchall()
    for n in fall:
        print(n)
        """
        print city,state
        """
    curs.close()
    datac.close()
