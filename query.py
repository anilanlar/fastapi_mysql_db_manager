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