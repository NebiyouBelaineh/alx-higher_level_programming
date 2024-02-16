#!/usr/bin/python3

"""script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    name = sys.argv[4]
    query = """SELECT `cities`.`name` FROM `cities` INNER JOIN `states` ON
    `cities`.`state_id` = `states`.`id` WHERE `states`.`name` = %s ORDER BY
    `cities`.`id`"""
    cur.execute(query, (name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
