# %%
#######################################
def sqlite3get_columnheaders_fromtable_alt(sql_conn: sqlite3.Connection, table_name: str):
    import sqlite3
    import re
    if isinstance(sql_conn, sqlite3.Connection):
        sql_syntax_with_header_names = list(sql_conn.execute(f"select sql from sqlite_master where name='{table_name}';"))
        column_names = re.findall(r'(?:[a-z_]+)', sql_syntax_with_header_names[0][0])
        column_names = column_names[1:]
        return column_names

