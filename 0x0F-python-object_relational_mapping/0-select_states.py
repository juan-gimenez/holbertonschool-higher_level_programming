#!/usr/bin/python3
"""
lists all states from the database
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
    curs.execute("SELECT * FROM states ORDER BY states.id;")
    for row in curs.fetchall():
        print(row)
        """
        print row
        """
    curs.close()
    datac.close()
