# Project: PythonDB: HarmoniK Festival
# Title: DB_managment.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 1.0, last modified:  10.06.2025


import mysql.connector
from datetime import date


# connect to the database
def connect_to_DB():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="festival_pythondb"
    )
    return connexion

# def loginAdmin_request(email, password_hash):
#     conn = connect_to_DB()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM visitors WHERE email=%s AND hash=%s AND is_admin=True', (email, password_hash))
#     visitor = cursor.fetchone()
#     cursor.close()
#     return visitor is not None # originally had an else structure, ChatGPT suggested the "is not" formulation

def login_request(email, password_hash):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM visitors WHERE email=%s AND hash=%s', (email, password_hash))
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

def get_username(email):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT first_name FROM visitors WHERE email=%s', (email,))
    username = cursor.fetchone()
    cursor.close()
    return username[0] if username else None

def get_admin_status(email):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('SELECT is_admin FROM visitors WHERE email=%s', (email,))
    admin_status = cursor.fetchone()
    cursor.close()
    return admin_status[0] if admin_status else None

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
    # control pour déja resérvé
    cursor.execute(
        "SELECT * FROM reservations WHERE concert_id = %s AND visitor_id = %s",
        (selected_concert_id, visitor_id)
    )
    existing = cursor.fetchone()
    if existing:
        success=False
    else:
        cursor.execute('INSERT INTO reservations (date_reservation, concert_id, visitor_id) VALUES (%s, %s, %s)', (date.today(), selected_concert_id, visitor_id))
        conn.commit()
        success=True
    return success


def deleteReservation(selected_reservation_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE reservations.id = %s', (selected_reservation_id,))
    conn.commit()

def newConcert(concert_name, concert_date, concert_price, scene_number, max_capacity, band_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO concerts (name, date, price, scene_number, max_capacity, band_id) VALUES (%s, %s, %s, %s, %s, %s)', (concert_name, concert_date, concert_price, scene_number, max_capacity, band_id))
    conn.commit()

def deleteConcert(selected_concert_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM concerts WHERE concerts.id = %s', (selected_concert_id,))
    conn.commit()

def newBand(band_name, band_genre, band_origin, band_description):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bands (name, genre, origin, description) VALUES (%s, %s, %s, %s)', (band_name, band_genre, band_origin, band_description))
    conn.commit()

def deleteBand(selected_band_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM bands WHERE bands.id = %s', (selected_band_id,))
    conn.commit()

def updateBand(selected_band_id, new_name, new_genre, new_origin, new_desc):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('UPDATE bands SET name = %s, genre = %s, origin = %s, description = %s WHERE bands.id = %s', (new_name, new_genre, new_origin, new_desc, selected_band_id))
    conn.commit()

def updateVisitor(selected_visitor_id, new_fname, new_lname, new_bdate, new_email):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('UPDATE visitors SET first_name= %s, last_name = %s, birthdate = %s, email = %s WHERE visitors.id = %s', (new_fname, new_lname, new_bdate, new_email, selected_visitor_id))
    conn.commit()

def updateConcert(selected_concert_id,new_name,new_date,new_price,new_snmbr,new_capacity,new_band):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('UPDATE concerts SET name=%s,date=%s,price=%s,scene_number=%s,max_capacity=%s,band_id=%s WHERE concerts.id=%s' , (new_name,new_date,new_price,new_snmbr,new_capacity,new_band,selected_concert_id))
    conn.commit()

def deleteVisReservation(selected_visitor_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE reservations.visitor_id = %s', (selected_visitor_id,))
    conn.commit()

def deleteVisitor(selected_visitor_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM visitors WHERE visitors.id = %s', (selected_visitor_id,))
    conn.commit()

def updatePassword(new_pswd_hash, visitor_id):
    conn = connect_to_DB()
    cursor = conn.cursor()
    cursor.execute('UPDATE visitors SET hash = %s WHERE visitors.id = %s', (new_pswd_hash, visitor_id))
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


def newVisitor(vis_fname, vis_lname, vis_birthdate, vis_email, vis_password_hash):
    conn = connect_to_DB()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM visitors WHERE email = %s", (vis_email,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        raise ValueError("This email is already registered.")
    cursor.execute('INSERT INTO visitors (first_name, last_name, birthdate, email, hash, is_admin) values (%s, %s, %s, %s,%s, %s)' ,
                   (vis_fname, vis_lname, vis_birthdate, vis_email, vis_password_hash, 0))
    conn.commit()

