import sqlite3

with sqlite3.connect("/Users/Julian/Desktop/irc/irc.sqlite") as conn:
        messages = conn.execute(
            """
            SELECT sender, contents
            FROM messages
            WHERE sender = ''
            """
        )
        for _, action in messages:
            sender, space, contents = action.lstrip(" ").partition(" ")
            assert space, repr(action)
            print(sender, contents)
            conn.execute(
                """
                UPDATE messages
                SET sender = ?,
                    contents = ?
                WHERE sender = '' AND contents = ?
                """, (sender, contents, action),
            ).fetchall()
