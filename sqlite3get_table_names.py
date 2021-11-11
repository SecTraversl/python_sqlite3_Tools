# %%
#######################################
def sqlite3get_table_names(sql_conn: sqlite3.Connection):
    """For a given sqlite3 database connection object, returns the table names within that database.

    Examples:
        >>> db_conn = sqlite3.connect('places.sqlite')\n
        >>> sqlite3get_table_names(db_conn)\n
        ['moz_origins', 'moz_places', 'moz_historyvisits', 'moz_inputhistory', 'moz_bookmarks', 'moz_bookmarks_deleted', 'moz_keywords', 'moz_anno_attributes', 'moz_annos', 'moz_items_annos', 'moz_meta', 'sqlite_stat1']

    References:
        # How to list tables for a given database:\n
        https://techoverflow.net/2019/10/14/how-to-list-tables-in-sqlite3-database-in-python/\n
        
        # Firefox forensics - what sqlite databases store which artifacts\n
        https://www.foxtonforensics.com/browser-history-examiner/firefox-history-location\n

    Args:
        sql_conn (sqlite3.Connection): Reference an existing slite3 Connection object.

    Returns:
        list: Returns a list of the table names in the database.
    """
    import sqlite3
    cursor = sql_conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [
        name[0] for name in cursor.fetchall() if name[0] != 'sqlite_sequence'
    ]
    cursor.close()
    return table_names

