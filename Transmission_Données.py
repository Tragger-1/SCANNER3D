
import mariadb
import sys
def Transmission_Donnee(x,y,z,r,g,b):
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="appscan",
            password="Scanner3D",
            host="192.168.1.62",
            port=3306,
            database="DATAPOINT"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()

    # cur.execute(
    #     "DELETE FROM `POINT` WHERE `POINT`.`NUM_OBJET` = 1"
    # )

    cur.execute(
        "INSERT INTO POINT(NUM_OBJET, X, Y, Z, R, G, B) VALUES (1," + str(x) + "," + str(y) + "," + str(z) + "," + str(r) + "," + str(g) + "," + str(b) + ")"
    )

    conn.commit()

   # print("INSERT INTO POINT(NUM_OBJET, X, Y, Z, R, G, B) VALUES (1," + str(x) + "," + str(y) + "," + str(z) + "," + str(r) + "," + str(g) + "," + str(b) + ")")

    cur.close()
    conn.close()
    #row= cur.fetchone()
    #print(*row, sep=' ')



    #print("Transmission de donnees | Ok" )
#mon but est d'effacer tout ce qui a comme numéro d'objet le 1 
#puis remplacer avec ce qui vient d'etre scanner (pointcloud)
