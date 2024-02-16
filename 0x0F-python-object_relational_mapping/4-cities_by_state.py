#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM `cities`"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
