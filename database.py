import mysql.connector

# Connect to MySQL
def connect_to_mysql():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="anil",
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
    # Wait for 2 seconds
    
    # create_data(connection)
    connection.close()
    
    # connection = connect_to_mysql()
    # create_data(connection)
    # connection.close()

# Call the function to create all tables
