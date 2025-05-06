import mysql.connector

# connect to the database
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="festival_PythonDB"
)

def loginAdmin_request(email, password):
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM visitors WHERE email=%s AND hash=%s AND email='kilian.testard@bluewin.ch'", (email, password))
    visitor = cursor.fetchone()
    cursor.close()
    return visitor is not None

def login_request(email, password):
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM visitors WHERE email=%s AND hash=%s AND email!='kilian.testard@bluewin.ch'", (email, password))
    visitor = cursor.fetchone()
    cursor.close()
    return visitor is not None

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