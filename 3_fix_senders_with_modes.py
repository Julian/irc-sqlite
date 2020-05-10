import sqlite3

with sqlite3.connect("/Users/Julian/Desktop/irc/irc.sqlite") as conn:
        senders = conn.execute(
            """
            SELECT DISTINCT sender
            FROM messages
            WHERE sender like '+%'
            OR sender like '@%'
            """
        )
        for each, in senders:
            sender = each.lstrip(" +@")
            messages = conn.execute(
                """
                UPDATE messages
                SET sender = ?
                WHERE sender = ?
                """, (sender, each),
            )
