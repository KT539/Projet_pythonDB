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


INSERT INTO visitors (id, first_name, last_name, birthdate, email, hash, is_admin) VALUES
(1, 'Léa', 'Dupont', '1995-03-12', 'lea.dupont@gmail.com', '3f6dd106af75dfa189dd8a39e55eda7205663207584fc0088f948a3b067356da', 0),
(2, 'Marc', 'Schneider', '1988-11-25', 'marc.schneider@bluewin.ch', '04f9bef355fee602a8845af17203c1cc1f241129e883676d7effb17ecb2bbb99', 0),
(3, 'Chloé', 'Baumann', '2000-07-04', 'chloe.baumann@epfl.ch', '59930792158886a1f6950696975637c66c5448400e5a77ac66ba32a73b1ee107', 0),
(4, 'Julien', 'Moret', '1992-01-17', 'julien.moret@gmail.com', '979078f1453a8de65703df2a35ea819a39c7d5b29dce668ce6a35f8c2ce28e16', 0),
(5, 'Nina', 'Müller', '1998-09-09', 'nina.mueller@unil.ch', 'cb46de32930c8cb70264554acf1a5f6ab750d50d6560e32d4ff2cf3c9396b660', 0),
(6, 'David', 'Rossi', '1990-06-30', 'david.rossi@lausanne.ch', '6af731c9adacb8d0a1445818945a18a9d2566258693706be0e19e7741e57ff71', 0),
(7, 'Emma', 'Keller', '1997-12-05', 'emma.keller@protonmail.com', 'f0a4334f3c06ac16dacdf3af2cddca17c3b56457829ceb2e716c8900c8b66d7c', 0),
(8, 'Sophie', 'Hug', '1993-08-21', 'sophie.hug@epfl.ch', '3069a8041facf5f158ac0f8be4b48c3bfe91f089667e47f2137f92f017725f2d', 0),
(9, 'Lucas', 'Weber', '1985-04-14', 'lucas.weber@bluewin.ch', 'd95f2cb64d33973a54bc2254b75de21793f683d6508a26065632c4cbd3cfed44', 0),
(10, 'Laura', 'Fischer', '2001-10-10', 'laura.fischer@unil.ch', '08defe58a642e3bf77e38f96c865eeecd8849a8cd60850fe1c039670eff4ac96', 0),
(11, 'Thomas', 'Gérard', '1994-03-22', 'thomas.gerard@gmail.com', '940745caf3a47d93c76bdf164375a13076b36402463f7b286a44cfc4b0f8e536', 0),
(12, 'Anna', 'Bovet', '1996-05-18', 'anna.bovet@lausanne.ch', 'c169ccf79b9f52aaa5d552dd122edbe076ed7a7fe158c4b31c8b410cdfc77d43', 0),
(13, 'Sébastien', 'Joly', '1991-02-28', 'seb.joly@gmail.com', '2dd2b742fd6ee7f598b80705b15e2b7f0a53d0ff3a339de3998f90b5569660cb', 0),
(14, 'Claire', 'Perret', '1999-07-07', 'claire.perret@epfl.ch', 'e3c9a8939960c90ca3fc739c2a1ddc7400c10b004d46d1e2cf40b050a41839a8', 0),
(15, 'Noah', 'Imhof', '1993-12-03', 'noah.imhof@bluewin.ch', 'ee972a89e6972190463d1dcb963d01b02be7ce6f8e72038c5a6b7ab1c8379214', 0),
(16, 'Julie', 'Vogel', '1990-06-11', 'julie.vogel@protonmail.com', 'fcb52ab409d9b0f9b1e304b4f185a1b3440d6ef5285dacc326bc0bc47260226a', 0),
(17, 'Mélanie', 'Favre', '1997-08-19', 'melanie.favre@gmail.com', '33b2efd6f70bd7a7de8aba3d8320a34edbab7c4d7d37332f4fdc0b23ce4c6245', 0),
(18, 'Hugo', 'Marti', '1992-04-08', 'hugo.marti@lausanne.ch', '33bc441c36d75cc1f1c0fc7a582fc9c259b6df483adfb6a41faadba424e5f488', 0),
(19, 'Émilie', 'Renaud', '1995-01-30', 'emilie.renaud@unil.ch', '5fd2da1086cdb0f43377cd296288e5bfb1b11c819788421f08f5f2ed178f1525', 0),
(20, 'Alex', 'Berthoud', '1989-10-26', 'alex.berthoud@bluewin.ch', '1686993f6edb8f5d119761eabb4d3d2b529a8faef08814f3088827b44f56d9a1', 0),
(21, 'Kilian', 'Testard', '1999-10-26', 'kilian.testard@bluewin.ch', '4f2e99b3fd0d318d07944f4dd9867cf950de204d0cac1161c0d95c86ad0cfc65', 1),
(22, 'Ahmet', 'Karabulut', '1992-06-24', 'ahmet.karabulut@bluewin.ch', '3938ab342698aa7c5a135df65918ffbd56eb1226a8c463ff566b4e897c87ba73', 1);


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




