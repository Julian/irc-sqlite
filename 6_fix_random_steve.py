import sqlite3

with sqlite3.connect("/Users/Julian/Desktop/irc/irc.sqlite") as conn:
        messages = conn.execute(
            """
            SELECT contents
            FROM messages
            WHERE sender = ' '
            """
        )
        for each, in messages:
            assert each.startswith("Steve|> "), each
            _, space, contents = each.partition("> ")
            conn.execute(
                """
                UPDATE messages
                SET sender = '|Steve|',
                    contents = ?
                WHERE sender = ' ' AND contents = ?
                """, (contents, each),
            ).fetchall()
