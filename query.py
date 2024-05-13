from database import connect_to_mysql
import traceback



# REQ 1
def db_manager_login(username, password):
    connection = connect_to_mysql()
    print("Connection is successful")
    cursor = connection.cursor()
    query = """
        SELECT COUNT(*) FROM DatabaseManagers
        WHERE username = %s AND password = %s
    """
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    print("result", result)
    cursor.close()
    connection.close()
    
    if result[0] > 0: #Check for whether there is a match for username and password
        return True
    else:
        return False


# REQ 2
# Database managers shall be able to add new Users (Players/Juries/Coaches) to
# the system. (So no signup page is required.)
def add_new_user_query(user_type, username, password, name, surname, date_of_birth, height, weight, nationality):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    userQuery = "INSERT INTO Users (username, password, name, surname) VALUES (%s, %s, %s, %s)" # For all type of users we need to create user
    cursor.execute(userQuery, (username, password, name, surname))
    cursor.reset()

    if user_type == "Player": # Player case 
        query = """
            INSERT INTO Players (username, password, name, surname, date_of_birth, height, weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, name, surname, date_of_birth, height, weight))

    elif user_type == "Jury": # Jury Case
        query = """
            INSERT INTO Juries (username, password, name, surname, nationality)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, name, surname, nationality))

    elif user_type == "Coach": # Coach case
        query = """
            INSERT INTO Coaches (username, password, name, surname, nationality)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, name, surname, nationality))
    else:
        print("Invalid user type")
        return
    
    connection.commit()
    cursor.close()
    connection.close()


# REQ 3
# Database managers shall be able to update stadium name according to the wills
# of the politicians. When a stadium is updated, all the preexisting records with
# that name should be changed.
def update_stadium_name(old_name, new_name):
    print(old_name, new_name)
    try:
        connection = connect_to_mysql()
        cursor = connection.cursor()
        cursor.execute("SET SQL_SAFE_UPDATES = 0;") # In order to make name changes there is a need to disable safe updates
        query = """
            UPDATE Stadiums
            SET stadium_name = %s
            WHERE stadium_name = %s
        """
        cursor.execute(query, (new_name, old_name))
        rows_affected = cursor.rowcount
        connection.commit()
        cursor.execute("SET SQL_SAFE_UPDATES = 1;") # enable safe updates again
        return rows_affected > 0
    except Exception as e:
        print("Failed to update stadium name:", e)
        
        return False
    finally:
        cursor.close()
        connection.close()


# REQ 4 
# Coaches shall be able to delete match sessions by providing session ID. When a
# match session is deleted, all data regarding that match session must be deleted
# including the rating, date, stadium etc. Also, the squad info of that match
# session should be deleted.
def delete_match_session_query(session_id):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = """
        DELETE FROM MatchSessions
        WHERE session_id = %s;
    """
    cursor.execute(query, (session_id,))
    rows_affected = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return rows_affected



# REQ 5
# Coaches shall be able to add a new match session, he/she can only put his/her
# current team ID. Stadium info and date, time, timeslot info are up to the coach’s
# choice but they should not be conflicting. You should check for any type of conflict with triggers.
# Also coach can choose(assign) his/her own session’s assigned
# jury (by jury’s name and surname). The rating of the newly added session
# should be left blank or null at first, till a jury logs in and rates the match.

def add_match_session_query(coach_username, stadium_id, time_slot, date, jury_name, jury_surname): 
    #In order to prevent unread result found error we create different cursors for each operation 
    connection = connect_to_mysql()
    try:
        with connection.cursor() as cursor: #Getting team id by using coach username 
            team_id_query = "SELECT team_id FROM Teams WHERE coach_username = %s"
            cursor.execute(team_id_query, (coach_username,))
            team_id = cursor.fetchone()[0]


        with connection.cursor(buffered=True) as cursor: #Getting jury username by using name and surname of jury
            assigned_jury_username_query = "SELECT username FROM Juries WHERE name LIKE %s AND surname LIKE %s"
            cursor.execute(assigned_jury_username_query, (jury_name, jury_surname))
            assigned_jury_username = cursor.fetchone()[0]
            if cursor.with_rows and cursor.statement:  # Still unread result error so extra prevention, Check if there are unread results
                cursor.fetchall()  # Read all remaining data to clear the cursor

        with connection.cursor() as cursor: # Inserting new session
            insert_query = """
                INSERT INTO MatchSessions (team_id, stadium_id, time_slot, date, assigned_jury_username)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (team_id, stadium_id, time_slot, date, assigned_jury_username))
            connection.commit()
    except Exception as e:
        print("Error occurred while executing database query:")
        traceback.print_exc()
        connection.rollback()
    finally:
        connection.close()

# REQ 6
# Coaches shall be able to create a squad for his/her newly created session 
# (however a new session can exist without a declared squad.). All the players 
# that the coach chooses for his/her squad should be from the coach’s current team.
# Coach shall be able to create squad using player names.

def create_squad_query(session_id, coach_username, players):
    connection = connect_to_mysql()
    cursor = connection.cursor()

    # Ensuring the session is linked to the coach's team
    team_id_query = """
        SELECT t.team_id FROM Teams t
        JOIN MatchSessions ms ON t.team_id = ms.team_id
        WHERE ms.session_id = %s AND t.coach_username = %s
    """
    cursor.execute(team_id_query, (session_id, coach_username))
    team_id_result = cursor.fetchone()
    # print(f"Team id : {team_id_result}")
    
    if not team_id_result: #No match case 
        cursor.close()
        connection.close()
        print("Session does not belong to the coach's team or session does not exist.")
        return False
    # print(players)
    
    for player in players: # Insert each player into the new squad
        player_username = player.username
        position_id = player.position_id
        # print(f"player_username : {player_username} , position_id: {position_id}")        
        
        # Verify that the player is part of the coach's team
        player_check_query = """ 
            SELECT username FROM PlayerTeams WHERE username = %s AND team_id = %s
        """
        cursor.execute(player_check_query, (player_username, team_id_result[0])) 
        player_check = cursor.fetchone()
        print(f"player_check : {player_check}")

        if not player_check:#Player in different team case 
            continue  # Skip player

        # Insert player into the squad
        insert_query = """
            INSERT INTO SessionSquads (session_id, played_player_username, position_id)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (session_id, player_username, position_id))

    connection.commit()
    cursor.close()
    connection.close()
    return True



# REQ 7
# Coaches shall be able to see a list of all existing stadiums names and their
# countries.
def get_stadiums_query():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = """
        SELECT stadium_name, stadium_country FROM Stadiums
    """
    cursor.execute(query)
    stadiums = cursor.fetchall()
    print(stadiums)
    cursor.close()
    connection.close()
    return stadiums


# REQ 8
# Juries shall be able to view the average rating of all sessions that he/she rated
# also the count of total rated sessions by him/her
def get_jury_ratings_query(jury_username):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = """
        SELECT AVG(rating), COUNT(rating) FROM MatchSessions
        WHERE assigned_jury_username = %s
    """
    cursor.execute(query, (jury_username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


# REQ 9
# Juries shall be able to rate a session that are assigned to them
# only if they haven’t rated that session yet and if the current
# date (like the date of the Demo :) ) is after the date of the 
# specific match session.

def rate_match_query(session_id, jury_username, rating): # Check trigger for this query in datapase.py
    connection = connect_to_mysql()
    cursor = connection.cursor()
    try:
        update_query = """
            UPDATE MatchSessions
            SET rating = %s
            WHERE session_id = %s AND assigned_jury_username = %s AND rating IS NULL
        """
        cursor.execute(update_query, (rating, session_id, jury_username))
        if cursor.rowcount == 0:
            raise ValueError("Failed to update rating. Session may not exist, already be rated, or is in the future.")
        connection.commit()
    except Exception as e:
        connection.rollback() #If fail discard all changes.
        print("Error occurred:", str(e))
        return False, str(e)
    finally:
        cursor.close()
        connection.close()

    return True

# REQ 10
# Players shall be able to view all of the players’ names and surnames
# that he/she has played within a session at least once. Also a player
# should see the height of the player that he/she played with the most.
# If there are more than one players that he/she played the most, he/she 
# should see the average height of those players.

def view_played_players_query(player_username):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    try:
        #Getting all players that gave played together with given player
        cursor.execute("""
            SELECT DISTINCT p2.name, p2.surname
            FROM SessionSquads s1
            JOIN SessionSquads s2 ON s1.session_id = s2.session_id
            JOIN Players p1 ON s1.played_player_username = p1.username
            JOIN Players p2 ON s2.played_player_username = p2.username
            WHERE p1.username = %s AND p2.username != %s
        """, (player_username, player_username))
        players = cursor.fetchall()
        cursor.reset() 
        # Find player whom the given player has played the most sessions
        cursor.execute("""
            SELECT p2.name, p2.surname, COUNT(*) as session_count
            FROM SessionSquads s1
            JOIN SessionSquads s2 ON s1.session_id = s2.session_id
            JOIN Players p1 ON s1.played_player_username = p1.username
            JOIN Players p2 ON s2.played_player_username = p2.username
            WHERE p1.username = %s AND p2.username != %s
            GROUP BY p2.username
            ORDER BY session_count DESC
            LIMIT 1
        """, (player_username, player_username))
        most_frequent_player = cursor.fetchall()
        cursor.reset()

       
        if len(most_frequent_player) > 1: # If there are multiple players with the same max session count, calculate the average height
            names = tuple((player[0], player[1]) for player in most_frequent_player)

            cursor.execute("""
                SELECT AVG(height)
                FROM Players
                WHERE (name, surname) IN (%s)
            """, (names,))
            average_height = cursor.fetchone()[0]

        else:  # Case for single or none player from query , None player from query will be handled on ui (Check req10.html)
            cursor.execute("""
                SELECT p.height
                FROM Players p
                WHERE p.name = %s AND p.surname = %s
            """, (most_frequent_player[0][0],most_frequent_player[0][1]))
            average_height = cursor.fetchone()[0]
           
        return {"played_with": players, "most_frequent": most_frequent_player, "average_height": average_height}

    except Exception as e:
        print("An error occurred:", str(e))
        return {}
    finally:
        cursor.close()
        connection.close()
