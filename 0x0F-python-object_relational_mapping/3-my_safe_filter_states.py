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
    arg = argv[4]
    curs.execute("SELECT * FROM states where name like %s ORDER BY id ASC;",
                 (arg,))
    fall = curs.fetchall()
    for n in fall:
        if (n[1] == arg):
            print("{}".format(n))
            """
            print if equal
            """
    curs.close()
    datac.close()
