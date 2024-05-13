import mysql.connector

# Connect to MySQL
def connect_to_mysql():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alb761834925:",
    database="VolleyDB"
)


# Function to create Database Managers table
def create_database_managers_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DatabaseManagers (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create Users table
def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50),
            name VARCHAR(50),
            surname VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create Players table
def create_players_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Players (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50),
            name VARCHAR(50),
            surname VARCHAR(50),
            date_of_birth DATE,
            height FLOAT,
            weight FLOAT
        )
    """)
    connection.commit()
    cursor.close()

# Function to create Coaches table
def create_coaches_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Coaches (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50),
            name VARCHAR(50),
            surname VARCHAR(50),
            nationality VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create Juries table
def create_juries_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Juries (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50),
            name VARCHAR(50),
            surname VARCHAR(50),
            nationality VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create Positions table
def create_positions_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Positions (
            position_id INT PRIMARY KEY,
            position_name VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create Teams table
def create_teams_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teams (
            team_id INT AUTO_INCREMENT PRIMARY KEY,
            team_name VARCHAR(50),
            coach_username VARCHAR(50),
            contract_start DATE,
            contract_finish DATE,
            channel_id INT,
            FOREIGN KEY (coach_username) REFERENCES Coaches(username)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create PlayerPositions table
def create_player_positions_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PlayerPositions (
            player_positions_id INT PRIMARY KEY,
            username VARCHAR(50),
            position_id INT,
            FOREIGN KEY (username) REFERENCES Players(username),
            FOREIGN KEY (position_id) REFERENCES Positions(position_id)
        )
    """)
    connection.commit()
    cursor.close()

# Function to create PlayerTeams table
def create_player_teams_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PlayerTeams (
            player_teams_id INT PRIMARY KEY,
            username VARCHAR(50),
            team_id INT,
            FOREIGN KEY (username) REFERENCES Players(username),
            FOREIGN KEY (team_id) REFERENCES Teams(team_id)
        )
    """)
    connection.commit()
    cursor.close()



# Function to create MatchSessions table
def create_match_sessions_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MatchSessions (
            session_id INT AUTO_INCREMENT PRIMARY KEY,
            team_id INT,
            stadium_id INT,
            time_slot INT,
            date VARCHAR(512),
            assigned_jury_username VARCHAR(50),
            rating INT,
            FOREIGN KEY (stadium_id) REFERENCES Stadiums(stadium_id),
            FOREIGN KEY (team_id) REFERENCES Teams(team_id),
            FOREIGN KEY (assigned_jury_username) REFERENCES Juries(username)
        )
    """)
    connection.commit()
    cursor.close()


# Function to create Stadiums table
def create_stadium_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Stadiums (
            stadium_id INT PRIMARY KEY,
            stadium_name VARCHAR(50),
            stadium_country VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()


# Function to create SessionSquads table
def create_session_squads_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SessionSquads (
            squad_id INT PRIMARY KEY,
            session_id INT,
            played_player_username VARCHAR(50),
            position_id INT,
            FOREIGN KEY (session_id) REFERENCES MatchSessions(session_id) ON DELETE CASCADE,
            FOREIGN KEY (played_player_username) REFERENCES Players(username),
            FOREIGN KEY (position_id) REFERENCES Positions(position_id)
        )
    """)
    connection.commit()
    cursor.close()



#Trigger for REQ 9 rating
def rate_match_trigger(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TRIGGER BeforeUpdateRating
        BEFORE UPDATE ON MatchSessions
        FOR EACH ROW
        BEGIN
            IF OLD.rating IS NULL AND NEW.rating IS NOT NULL THEN
                IF CURDATE() > OLD.date THEN
                    SET NEW.rating = NEW.rating;
                ELSE
                    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot rate a future session.';
                END IF;
            ELSEIF OLD.rating IS NOT NULL THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Session already rated.';
            END IF;
        END;
    """)
    connection.commit()
    cursor.close()

# Call this function to create all tables
def create_tables():
    connection = connect_to_mysql()
    create_database_managers_table(connection)
    create_users_table(connection)
    create_players_table(connection)
    create_coaches_table(connection)
    create_juries_table(connection)
    create_positions_table(connection)
    create_teams_table(connection)
    create_player_positions_table(connection)
    create_player_teams_table(connection)
    create_stadium_table(connection)
    create_match_sessions_table(connection)
    create_session_squads_table(connection)

    rate_match_trigger(connection)

    connection.close()
    
# Call the function to drop all tables
def drop_tables():
    connection = connect_to_mysql()
    cursor = connection.cursor()

    # Disable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

    #  drop all tables
    cursor.execute("""
        SELECT CONCAT('DROP TABLE IF EXISTS ', table_name, ';') AS drop_statement
        FROM information_schema.tables
        WHERE table_schema = 'VolleyDB';
    """)
    drop_commands = cursor.fetchall()
    for command in drop_commands:
        cursor.execute(command[0])

    # enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

    connection.commit()
    cursor.close()
    connection.close()
    
# Add mock data
def add_data():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    with open('CreateMockData.sql', 'r') as file:
        sql_queries = file.read()

    queries = sql_queries.split(';')
    for query in queries:
        try:
            if query.strip() != '':
                cursor.execute(query)
                connection.commit()
                print("Query executed successfully!")
        except Exception as e:
            print("Error executing query:", str(e))

    cursor.close()
    connection.close()