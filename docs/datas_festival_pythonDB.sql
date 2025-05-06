USE `festival_pythondb`;

-- BANDS --------------------------


INSERT INTO bands (id, name, genre, origin, description) VALUES
(1, 'Alpine Echoes', 'Folk', 'Lausanne', 'Traditional Swiss folk band with alpine roots.'),
(2, 'Geneva Lights', 'Pop', 'Geneva', 'Upbeat pop group known across Romandy.'),
(3, 'Rhône Flow', 'Hip-hop', 'Lausanne', 'Urban hip-hop with French lyrics.'),
(4, 'Swiss Metal', 'Metal', 'Zurich', 'Hardcore metal band touring Europe.'),
(5, 'Jazz du Léman', 'Jazz', 'Vevey', 'Smooth jazz group with saxophone lead.'),
(6, 'Yodel Beat', 'Electronic', 'Bern', 'Electro with yodel-inspired samples.'),
(7, 'Château Rock', 'Rock', 'Neuchâtel', 'Garage rockers from the lake region.'),
(8, 'Montreux Moods', 'Soul', 'Montreux', 'Soul band playing Montreux Jazz Fest.'),
(9, 'AlpenFire', 'Electronic', 'Lucerne', 'EDM group with fire shows.'),
(10, 'Lausanne Strings', 'Classical', 'Lausanne', 'Chamber ensemble from conservatory.'),
(11, 'Lac Noir', 'Alternative', 'Fribourg', 'Moody indie rock band.'),
(12, 'Romand Rebels', 'Punk', 'Lausanne', 'DIY punk from Romandy scene.'),
(13, 'Funky Gruyère', 'Funk', 'Gruyère', 'Cheesy name, funky vibes.'),
(14, 'The Glacier Notes', 'Indie Pop', 'Zermatt', 'Melodic indie pop with nature themes.'),
(15, 'Snowdrift', 'Ambient', 'Sion', 'Instrumental ambient project.'),
(16, 'Matterhorn Monks', 'Experimental', 'Brig', 'Avant-garde musical collective.'),
(17, 'Echo Alpina', 'World', 'Appenzell', 'Mix of Swiss & global folk music.'),
(18, 'Les Échos de la Nuit', 'Electronic', 'Lausanne', 'Underground techno from Lausanne.'),
(19, 'Suisse Symphonique', 'Classical', 'Bern', 'National level symphonic orchestra.'),
(20, 'Voix du Lac', 'Vocal', 'Lausanne', 'A capella group with lake-inspired themes.');



--    CONCERTS    --------------------------
 

INSERT INTO concerts (id, name, date, price, scene_number, max_capacity, band_id) VALUES
(1, 'Sunset Sessions', '2025-07-12 19:00:00', 25.00, 1, 300, 1),
(2, 'Synth Night', '2025-07-13 20:00:00', 30.00, 2, 250, 2),
(3, 'Jazz by the Lake', '2025-07-14 18:30:00', 35.00, 1, 200, 3),
(4, 'Beats & Alps', '2025-07-15 21:00:00', 40.00, 3, 500, 4),
(5, 'Indie Night Lausanne', '2025-07-16 19:30:00', 20.00, 1, 150, 5),
(6, 'Metal Storm', '2025-07-17 22:00:00', 45.00, 2, 400, 6),
(7, 'Pop Lake Fest', '2025-07-18 20:00:00', 22.00, 1, 350, 7),
(8, 'Alternative Echoes', '2025-07-19 21:00:00', 28.00, 3, 280, 8),
(9, 'Jazz Morning Jam', '2025-07-20 11:00:00', 15.00, 2, 100, 9),
(10, 'Snow & Sound', '2025-07-21 20:30:00', 32.00, 3, 270, 10),
(11, 'Rap Up Lausanne', '2025-07-22 20:00:00', 18.00, 1, 300, 11),
(12, 'Tradition Meets Tech', '2025-07-23 19:30:00', 25.00, 2, 220, 12),
(13, 'Rhine Rhythms', '2025-07-24 22:00:00', 35.00, 3, 500, 13),
(14, 'Folk Fest', '2025-07-25 18:00:00', 20.00, 1, 180, 14),
(15, 'Lugano Rock Night', '2025-07-26 21:00:00', 30.00, 2, 260, 15),
(16, 'Pop Tock', '2025-07-27 20:00:00', 25.00, 1, 220, 16),
(17, 'Collider Beats', '2025-07-28 21:30:00', 33.00, 3, 300, 17),
(18, 'Soul at Sunset', '2025-07-29 19:00:00', 28.00, 2, 240, 18),
(19, 'Mountain Reggae', '2025-07-30 20:00:00', 26.00, 1, 270, 19),
(20, 'Post-Rock Nights', '2025-07-31 21:00:00', 29.00, 2, 250, 20);


-- VISITORS ----------------------


INSERT INTO visitors (id, first_name, last_name, birthdate, email, hash) VALUES
(1, 'Léa', 'Dupont', '1995-03-12', 'lea.dupont@gmail.com', 'hash1'),
(2, 'Marc', 'Schneider', '1988-11-25', 'marc.schneider@bluewin.ch', 'hash2'),
(3, 'Chloé', 'Baumann', '2000-07-04', 'chloe.baumann@epfl.ch', 'hash3'),
(4, 'Julien', 'Moret', '1992-01-17', 'julien.moret@gmail.com', 'hash4'),
(5, 'Nina', 'Müller', '1998-09-09', 'nina.mueller@unil.ch', 'hash5'),
(6, 'David', 'Rossi', '1990-06-30', 'david.rossi@lausanne.ch', 'hash6'),
(7, 'Emma', 'Keller', '1997-12-05', 'emma.keller@protonmail.com', 'hash7'),
(8, 'Sophie', 'Hug', '1993-08-21', 'sophie.hug@epfl.ch', 'hash8'),
(9, 'Lucas', 'Weber', '1985-04-14', 'lucas.weber@bluewin.ch', 'hash9'),
(10, 'Laura', 'Fischer', '2001-10-10', 'laura.fischer@unil.ch', 'hash10'),
(11, 'Thomas', 'Gérard', '1994-03-22', 'thomas.gerard@gmail.com', 'hash11'),
(12, 'Anna', 'Bovet', '1996-05-18', 'anna.bovet@lausanne.ch', 'hash12'),
(13, 'Sébastien', 'Joly', '1991-02-28', 'seb.joly@gmail.com', 'hash13'),
(14, 'Claire', 'Perret', '1999-07-07', 'claire.perret@epfl.ch', 'hash14'),
(15, 'Noah', 'Imhof', '1993-12-03', 'noah.imhof@bluewin.ch', 'hash15'),
(16, 'Julie', 'Vogel', '1990-06-11', 'julie.vogel@protonmail.com', 'hash16'),
(17, 'Mélanie', 'Favre', '1997-08-19', 'melanie.favre@gmail.com', 'hash17'),
(18, 'Hugo', 'Marti', '1992-04-08', 'hugo.marti@lausanne.ch', 'hash18'),
(19, 'Émilie', 'Renaud', '1995-01-30', 'emilie.renaud@unil.ch', 'hash19'),
(20, 'Alex', 'Berthoud', '1989-10-26', 'alex.berthoud@bluewin.ch', 'hash20'),
(21, 'Kilian', 'Testard', '1999-10-26', 'kilian.testard@bluewin.ch', 'hash21');


-- RESERVATIONS ------------------------------


INSERT INTO reservations (id, date_reservation, concert_id, visitor_id) VALUES
(1, '2025-07-12', 1, 1),
(2, '2025-07-13', 2, 2),
(3, '2025-07-14', 3, 3),
(4, '2025-07-15', 4, 4),
(5, '2025-07-16', 5, 5),
(6, '2025-07-17', 6, 6),
(7, '2025-07-18', 7, 7),
(8, '2025-07-19', 8, 8),
(9, '2025-07-20', 9, 9),
(10, '2025-07-21', 10, 10),
(11, '2025-07-22', 11, 11),
(12, '2025-07-23', 12, 12),
(13, '2025-07-24', 13, 13),
(14, '2025-07-25', 14, 14),
(15, '2025-07-26', 15, 15),
(16, '2025-07-27', 16, 16),
(17, '2025-07-28', 17, 17),
(18, '2025-07-29', 18, 18),
(19, '2025-07-30', 19, 19),
(20, '2025-07-31', 20, 20);


