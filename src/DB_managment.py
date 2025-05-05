import mysql.connector

# connect to the database
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="festival_PythonDB"
)

def reservations_requests():
    cursor = connexion.cursor()
    cursor.execute('''
            SELECT reservations.id, reservations.date_reservation, visitors.first_name, visitors.last_name, concerts.name AS concert_title, concerts.date
            FROM reservations
            INNER JOIN visitors ON reservations.visitor_id = visitors.id
            INNER JOIN concerts ON reservations.concert_id = concerts.id'''
                   )
    return cursor.fetchall()

def concerts_requests():
    cursor = connexion.cursor()
    cursor.execute('''
          SELECT concerts.id, concerts.date, concerts.scene_number
          FROM concerts
         '''
                   )
    return cursor.fetchall()

def bands_requests():
    cursor = connexion.cursor()
    cursor.execute('''
        SELECT bands.id, bands.name,bands.genre, bands.description,bands.origin
        FROM bands
       '''
    )
    return cursor.fetchall()