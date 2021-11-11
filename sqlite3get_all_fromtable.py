# %%
#######################################
def sqlite3get_all_fromtable(sql_conn: sqlite3.Connection, table_name: str):
    import sqlite3
    import pandas
    if isinstance(sql_conn, sqlite3.Connection):    
        cursor = sql_conn.execute(f"select * from {table_name}")
        column_headers = list(map(lambda x:x[0], cursor.description))
        row_contents = [e for e in cursor]
        results_df = pandas.DataFrame(row_contents, columns=column_headers)
        return results_df

