import sqlite3

with sqlite3.connect("/Users/Julian/Desktop/irc/irc.sqlite") as conn:
        channels = conn.execute(
            """
            SELECT DISTINCT channel from messages where channel like '%.__-__'
            """
        )
        for each, in channels:
            channel, _, date = each.rpartition(".")
            messages = conn.execute(
                """
                UPDATE messages
                SET channel = ?
                WHERE channel = ?
                """, (channel, each),
            )
