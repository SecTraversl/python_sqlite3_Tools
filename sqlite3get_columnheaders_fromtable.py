# %%
#######################################
def sqlite3get_columnheaders_fromtable(sql_conn: sqlite3.Connection, table_name: str):
    import sqlite3
    if isinstance(sql_conn, sqlite3.Connection):
        cursor = sql_conn.execute(f"select * from '{table_name}';")
        column_headers = list(map(lambda x:x[0], cursor.description))
        return column_headers

