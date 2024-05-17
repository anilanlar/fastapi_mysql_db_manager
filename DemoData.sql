-- Insert data into DatabaseManagers table
INSERT INTO DatabaseManagers (username, password)
VALUES ('manager1', 'password1'),
       ('manager2', 'password2');

-- Insert data into Users table
INSERT INTO Users (username, password, name, surname)
VALUES ('user1', 'password1', 'John', 'Doe'),
       ('user2', 'password2', 'Alice', 'Smith');

-- Insert data into Players table
INSERT INTO Players (username, password, name, surname, date_of_birth, height, weight)
VALUES ('g_orge', 'Go.1993', 'Gizem', 'Örge', '1993-04-26', 170, 59),
('c_ozbay', 'Co.1996', 'Cansu', 'Özbay', '1996-10-17', 182, 78),
('m_vargas', 'Mv.1999', 'Melissa', 'Vargas', '1999-10-16', 194, 76),
('h_baladin', 'Hb.2007', 'Hande', 'Baladın', '2007-09-01', 190, 81),
('a_kalac', 'Ak.1995', 'Aslı', 'Kalaç', '1995-12-13', 185, 73),
('ee_dundar', 'Eed.2008', 'Eda Erdem', 'Dündar', '2008-06-22', 188, 74),
('z_gunes', 'Zg.2008', 'Zehra', 'Güneş', '2008-07-07', 197, 88),
('i_aydin', 'Ia.2007', 'İlkin', 'Aydın', '2007-01-05', 183, 67),
('e_sahin', 'Es.2001', 'Elif', 'Şahin', '2001-01-19', 190, 68),
('e_karakurt', 'Ek.2006', 'Ebrar', 'Karakurt', '2006-01-17', 196, 73),
('s_akoz', 'Sa.1991', 'Simge', 'Aköz', '1991-04-23', 168, 55),
('k_akman', 'Ka.2006', 'Kübra', 'Akman', '2006-10-13', 200, 88),
('d_cebecioglu', 'Dc.2007', 'Derya', 'Cebecioğlu', '2007-10-24', 187, 68),
('a_aykac', 'Aa.1996', 'Ayşe', 'Aykaç', '1996-02-27', 176, 57),
('user_2826', 'P.45825', 'Brenda', 'Schulz', '2002-12-13', 193, 80),
('user_9501', 'P.99695', 'Erika', 'Foley', '1995-12-21', 164, 62),
('user_3556', 'P.49595', 'Andrea', 'Campbell', '1996-04-26', 185, 100),
('user_7934', 'P.24374', 'Beatrice', 'Bradley', '1997-05-28', 150, 57),
('user_4163', 'P.31812', 'Betsey', 'Lenoir', '1993-05-07', 156, 48),
('user_2835', 'P.51875', 'Martha', 'Lazo', '2001-05-20', 173, 71),
('user_8142', 'P.58665', 'Wanda', 'Ramirez', '1994-01-03', 183, 94),
('user_2092', 'P.16070', 'Eileen', 'Ryen', '2004-06-21', 188, 60),
('user_3000', 'P.73005', 'Stephanie', 'White', '2002-05-19', 193, 74),
('user_8323', 'P.33562', 'Daenerys', 'Targaryen', '2006-09-16', 222, 74);

-- Insert data into Coaches table
INSERT INTO Coaches (username, password, nationality)
VALUES ('d_santarelli', 'santa.really1', 'ITA'),
('g_guidetti', 'guidgio.90', 'ITA'),
('f_akbas', 'a.fatih55', 'TR'),
('m_hebert', 'm.hebert45', 'US'),
('o_deriviere', 'oliviere_147', 'FR'),
('a_derune', 'aderune_147', 'FR');

-- Insert data into Juries table
INSERT INTO Juries (username, password,name,surname, nationality)
VALUES ('o_ozcelik', 'ozlem.0347', 'Özlem', 'Özçelik', 'TR'),
('m_sevinc', 'mehmet.0457', 'Mehmet', 'Sevinç', 'TR'),
('e_sener', 'ertem.4587', 'Ertem', 'Şener', 'TR'),
('s_engin', 'sinan.6893', 'Sinan', 'Engin', 'TR');

-- Insert data into Positions table
INSERT INTO Positions (position_id, position_name)
VALUES (0, 'Libero'),
       (1, 'Setter'),
       (2, 'Opposite hitter'),
       (3, 'Outside hitter'),
       (4, 'Middle blocker');
-- Insert data into Teams table
INSERT INTO Teams (team_id, team_name, coach_username, contract_start, contract_finish, channel_id)
VALUES (0, 'Women A', 'd_santarelli', '2021-12-25', '2025-12-12', 0),
(1, 'Women B', 'g_guidetti', '2021-09-11', '2026-09-11', 1),
(2, 'U19', 'f_akbas', '2021-08-10', '2026-08-10', 0),
(3, 'Women B', 'f_akbas', '2000-08-10', '2015-08-10', 1),
(4, 'Women C', 'm_hebert', '2024-04-01', '2026-07-21', 1),
(5, 'U19', 'o_deriviere', '2015-08-10', '2020-08-09', 2),
(6, 'U19', 'a_derune', '2005-08-10', '2010-08-10', 2);

-- Insert data into PlayerPositions table
INSERT INTO PlayerPositions (player_positions_id, username, position_id)
VALUES (1, 'g_orge', 0),
(2, 'g_orge', 3),
(3, 'c_ozbay', 1),
(4, 'm_vargas', 2),
(5, 'h_baladin', 3),
(6, 'a_kalac', 4),
(7, 'ee_dundar', 4),
(8, 'z_gunes', 4),
(9, 'i_aydin', 1),
(10, 'i_aydin', 3),
(11, 'e_sahin', 1),
(12, 'e_sahin', 3),
(13, 'e_karakurt', 2),
(14, 'e_karakurt', 3),
(15, 's_akoz', 0),
(16, 'k_akman', 0),
(17, 'k_akman', 4),
(18, 'd_cebecioglu', 3),
(19, 'd_cebecioglu', 4),
(20, 'a_aykac', 0),
(21, 'user_2826', 2),
(22, 'user_2826', 1),
(23, 'user_9501', 0),
(24, 'user_9501', 4),
(25, 'user_3556', 1),
(26, 'user_3556', 0),
(27, 'user_7934', 4),
(28, 'user_7934', 2),
(29, 'user_4163', 3),
(30, 'user_4163', 0),
(31, 'user_2835', 2),
(32, 'user_2835', 3),
(33, 'user_8142', 1),
(34, 'user_8142', 3),
(35, 'user_2092', 4),
(36, 'user_2092', 2),
(37, 'user_3000', 1),
(38, 'user_3000', 4),
(39, 'user_8323', 3),
(40, 'user_8323', 2);

-- Insert data into PlayerTeams table
INSERT INTO PlayerTeams (player_teams_id, username, team_id)
VALUES (1, 'g_orge', 0),
(2, 'c_ozbay', 0),
(3, 'c_ozbay', 1),
(4, 'm_vargas', 0),
(5, 'm_vargas', 1),
(6, 'h_baladin', 0),
(7, 'h_baladin', 2),
(8, 'a_kalac', 0),
(9, 'a_kalac', 1),
(10, 'ee_dundar', 0),
(11, 'ee_dundar', 2),
(12, 'z_gunes', 0),
(13, 'z_gunes', 2),
(14, 'i_aydin', 1),
(15, 'i_aydin', 2),
(16, 'e_sahin', 0),
(17, 'e_karakurt', 0),
(18, 'e_karakurt', 2),
(19, 's_akoz', 0),
(20, 's_akoz', 1),
(21, 'k_akman', 0),
(22, 'k_akman', 2),
(23, 'd_cebecioglu', 0),
(24, 'd_cebecioglu', 1),
(25, 'a_aykac', 0),
(26, 'user_2826', 2),
(27, 'user_2826', 3),
(28, 'user_9501', 0),
(29, 'user_9501', 3),
(30, 'user_3556', 2),
(31, 'user_3556', 3),
(32, 'user_7934', 0),
(33, 'user_7934', 3),
(34, 'user_4163', 1),
(35, 'user_4163', 3),
(36, 'user_2835', 2),
(37, 'user_2835', 3),
(38, 'user_8142', 0),
(39, 'user_8142', 3),
(40, 'user_2092', 2),
(41, 'user_2092', 3),
(42, 'user_3000', 2),
(43, 'user_3000', 3),
(44, 'user_8323', 0),
(45, 'user_8323', 3);


   
INSERT INTO Stadiums (stadium_id, stadium_name, stadium_country)
VALUES (0, "Burhan Felek Voleybol Salonu", "TR"),
       (1, "GD Voleybol Arena", "TR"),
       (2, "Copper Box Arena", "UK"),
       (3, "Kuzey","TR");

-- Insert data into MatchSessions table
INSERT INTO MatchSessions (session_id, team_id, stadium_id, time_slot, date, assigned_jury_username, rating)
VALUES (0, 0, 0, 1, '2024-03-10', 'o_ozcelik', 4.5),
(1, 1, 1, 1, '2024-04-03', 'o_ozcelik', 4.9),
(2, 0, 1, 3, '2024-04-03', 'o_ozcelik', 4.4),
(3, 2, 2, 2, '2024-04-03', 'm_sevinc', 4.9),
(4, 3, 2, 2, '2023-04-03', 'e_sener', 4.5),
(5, 3, 1, 1, '2023-05-27', 's_engin', 4.4),
(6, 0, 1, 1, '2022-09-01', 'm_sevinc', 4.6),
(7, 0, 2, 3, '2023-05-02', 'o_ozcelik', 4.7),
(8, 1, 0, 1, '2024-02-10', 'o_ozcelik', 4.5);



-- Insert data into SessionSquads table
INSERT INTO SessionSquads (squad_id, session_id, played_player_username, position_id)
VALUES (1, 0, 'g_orge', 0),
(2, 0, 'c_ozbay', 1),
(3, 0, 'm_vargas', 2),
(4, 0, 'h_baladin', 3),
(5, 0, 'a_kalac', 4),
(6, 0, 'ee_dundar', 4),
(7, 1, 'c_ozbay', 1),
(8, 1, 'm_vargas', 2),
(9, 1, 'i_aydin', 1),
(10, 1, 'a_kalac', 4),
(11, 1, 's_akoz', 0),
(12, 1, 'd_cebecioglu', 3),
(13, 2, 'g_orge', 3),
(14, 2, 'm_vargas', 2),
(15, 2, 'c_ozbay', 1),
(16, 2, 'a_kalac', 4),
(17, 2, 's_akoz', 0),
(18, 2, 'a_aykac', 0),
(19, 3, 'ee_dundar', 4),
(20, 3, 'h_baladin', 3),
(21, 3, 'z_gunes', 4),
(22, 3, 'i_aydin', 3),
(23, 3, 'e_karakurt', 2),
(24, 3, 'k_akman', 0),
(25, 4, 'user_2826', 2),
(26, 4, 'user_9501', 0),
(27, 4, 'user_3556', 1),
(28, 4, 'user_7934', 4),
(29, 4, 'user_4163', 3),
(30, 4, 'user_2835', 2),
(31, 5, 'user_2826', 1),
(32, 5, 'user_9501', 4),
(33, 5, 'user_3556', 0),
(34, 5, 'user_7934', 2),
(35, 5, 'user_4163', 0),
(36, 5, 'user_2835', 3),
(37, 6, 'g_orge', 0),
(38, 6, 'm_vargas', 2),
(39, 6, 'c_ozbay', 1),
(40, 6, 'a_kalac', 4),
(41, 6, 'e_karakurt', 3),
(42, 6, 'a_aykac', 0),
(43, 7, 'g_orge', 3),
(44, 7, 'm_vargas', 2),
(45, 7, 'c_ozbay', 1),
(46, 7, 'a_kalac', 4),
(47, 7, 'e_karakurt', 2),
(48, 7, 'a_aykac', 0);
