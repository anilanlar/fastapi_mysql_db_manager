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
VALUES ('player1', 'password1', 'Michael', 'Jordan', '1963-02-17', 198, 98),
       ('player2', 'password2', 'LeBron', 'James', '1984-12-30', 206, 113);

-- Insert data into Coaches table
INSERT INTO Coaches (username, password, nationality)
VALUES ('coach1', 'password1', 'USA'),
       ('coach2', 'password2', 'Spain');

-- Insert data into Juries table
INSERT INTO Juries (username, password,name,surname, nationality)
VALUES ('jury1', 'password1','a','b', 'France'),
       ('jury2', 'password2','a','b', 'Germany');

-- Insert data into Positions table
INSERT INTO Positions (position_id, position_name)
VALUES (1, 'Setter'),
       (2, 'Libero'),
       (3, 'Middle blocker');

-- Insert data into Teams table
INSERT INTO Teams (team_id, team_name, coach_username, contract_start, contract_finish, channel_id)
VALUES (1, 'Team A', 'coach1', '2024-01-01', '2024-12-31', 1),
       (2, 'Team B', 'coach2', '2024-01-01', '2024-12-31', 2);

-- Insert data into PlayerPositions table
INSERT INTO PlayerPositions (player_positions_id, username, position_id)
VALUES (1, 'player1', 1),
       (2, 'player2', 3);

-- Insert data into PlayerTeams table
INSERT INTO PlayerTeams (player_teams_id, username, team_id)
VALUES (1, 'player1', 1),
       (2, 'player2', 2);


   
INSERT INTO Stadiums (stadium_id, stadium_name, stadium_country)
VALUES (1, "Wembley", "UK"),
       (2, "Santiago", "SPAIN");

-- Insert data into MatchSessions table
INSERT INTO MatchSessions (session_id, team_id, stadium_id, time_slot, date, assigned_jury_username, rating)
VALUES (1, 1, 1, 1, '2024-05-10', 'jury1', 4),
       (2, 2, 2, 2, '2024-05-11', 'jury2', 3);



-- Insert data into SessionSquads table
INSERT INTO SessionSquads (squad_id, session_id, played_player_username, position_id)
VALUES (1, 1, 'player1', 1),
       (2, 1, 'player2', 3);
