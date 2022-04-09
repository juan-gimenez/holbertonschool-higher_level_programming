#!/usr/bin/python3
"""
lists all states starting w N
"""
"""
not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    datac = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3])
    curs = datac.cursor()
    curs.execute("SELECT * FROM states where name like 'N%' ORDER BY id ASC;")
    fall = curs.fetchall()
    for n in fall:
        if (n[1][0] == 'N'):
            print(n)
            """
            print if N
            """
    curs.close()
    datac.close()
