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
    arg = argv[4]
    curs = datac.cursor()
    curs.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
                = states.id WHERE states.name LIKE BINARY %s ORDER BY\
                cities.id;",
                 (arg, ))
    fall = curs.fetchall()
    emptylist = []
    for n in fall:
        emptylist.append(n[0])
    print(", ".join(emptylist))
    """
    print cities
    """
    curs.close()
    datac.close()
