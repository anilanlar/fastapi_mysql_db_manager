from database import connect_to_mysql


def add_new_user(username, password):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = """
        INSERT INTO Users (username, password)
        VALUES (%s, %s)
    """
    cursor.execute(query, (username, password))
    connection.commit()
    cursor.close()
    connection.close()




# REQ 1
def db_manager_login(username, password):
    connection = connect_to_mysql()
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
    
    if result[0] > 0:
        return True
    else:
        return False


# REQ 2
# Database managers shall be able to add new Users (Players/Juries/Coaches) to
# the system. (So no signup page is required.)
def add_new_user_query(user_type, username, password, name, surname, date_of_birth, height, weight, nationality):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    userQuery = "INSERT INTO Users (username, password, name, surname) VALUES (%s, %s, %s, %s)"
    cursor.execute(userQuery, (username, password, name, surname))
    cursor.reset()

    if user_type == "Player":
        query = """
            INSERT INTO Players (username, password, name, surname, date_of_birth, height, weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, name, surname, date_of_birth, height, weight))

    elif user_type == "Jury":
        query = """
            INSERT INTO Juries (username, password, name, surname, nationality)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, name, surname, nationality))

    elif user_type == "Coach":
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
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = """
        UPDATE MatchSessions
        SET stadium_name = %s
        WHERE stadium_name = %s
    """
    cursor.execute(query, (new_name, old_name))
    rows_affected = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return rows_affected > 0


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
        WHERE session_id = %s
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
# choice but they should not be conflicting. You should check for any type of conflict with triggers. Also coach can choose(assign) his/her own session’s assigned
# jury (by jury’s name and surname). The rating of the newly added session
# should be left blank or null at first, till a jury logs in and rates the match.

def add_match_session_query(coach_username, stadium_id, time_slot, date, jury_name, jury_surname):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    team_id_query = "SELECT team_id FROM Teams WHERE coach_username = %s"
    cursor.execute(team_id_query, (coach_username,))
    team_id = cursor.fetchone()[0]
    cursor.reset()
    
    
    assigned_jury_username_query = "SELECT username FROM Juries WHERE name LIKE %s AND surname LIKE %s"
    cursor.execute(assigned_jury_username_query, (jury_name, jury_surname))
    assigned_jury_username = cursor.fetchone()[0]
    # stadium_name, stadium_country
    cursor.reset()
    
    query = """
        INSERT INTO MatchSessions (team_id, stadium_id, time_slot, date, assigned_jury_username)
        VALUES (%s, %s, %s, %s, %s)
    """
    
    try:
        cursor.execute(query, (team_id, stadium_id, time_slot, date, assigned_jury_username))
    except Exception as e:
        print("Error occurred while executing database query:", str(e))

    
    
    connection.commit()
    cursor.close()
    connection.close()


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