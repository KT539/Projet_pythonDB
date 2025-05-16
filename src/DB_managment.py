import mysql.connector
from datetime import date

# connect to the database
def connect_to_DB():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="festival_PythonDB"
    )
    return connexion

def loginAdmin_request(email, password):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM visitors WHERE email=%s AND hash=%s AND email=\'kilian.testard@bluewin.ch\'', (email, password))
    visitor = cursor.fetchone()
    cursor.close()
    return visitor is not None # originally had an else structure, ChatGPT suggested the "is not" formulation

def login_request(email, password):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM visitors WHERE email=%s AND hash=%s AND email!=\'kilian.testard@bluewin.ch\'', (email, password))
    visitor = cursor.fetchone()
    cursor.close()
    return visitor is not None

# used ChatGPT as corrector for my code
def get_visitor_id(email):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM visitors WHERE email=%s', (email,))
    vis_id = cursor.fetchone()
    cursor.close()
    return vis_id[0] if vis_id else None

def reservations_requests(visitor_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT reservations.id, reservations.date_reservation, visitors.first_name, visitors.last_name, concerts.name AS concert_title, concerts.date FROM reservations INNER JOIN visitors ON reservations.visitor_id = visitors.id INNER JOIN concerts ON reservations.concert_id = concerts.id WHERE visitors.id = %s', (visitor_id,))
    return cursor.fetchall()

def reservationsAdmin_requests():
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT reservations.id, reservations.date_reservation, visitors.first_name, visitors.last_name, concerts.name AS concert_title, concerts.date FROM reservations INNER JOIN visitors ON reservations.visitor_id = visitors.id INNER JOIN concerts ON reservations.concert_id = concerts.id')
    return cursor.fetchall()

def newReservation(selected_concert_id, visitor_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reservations (date_reservation, concert_id, visitor_id) VALUES (%s, %s, %s)', (date.today(), selected_concert_id, visitor_id))
    conn.commit()

def deleteReservation(selected_reservation_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE reservations.id = %s', (selected_reservation_id,))
    conn.commit()


def visitors_requests():
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT visitors.id, visitors.first_name, visitors.last_name, visitors.birthdate, visitors.email FROM visitors')
    return cursor.fetchall()

def concerts_requests():
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT concerts.id, concerts.name, concerts.date, concerts.scene_number FROM concerts')
    return cursor.fetchall()

def bands_requests():
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT bands.id, bands.name,bands.genre, bands.description,bands.origin FROM bands')
    return cursor.fetchall()
