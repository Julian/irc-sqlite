import sqlite3

with sqlite3.connect("/Users/Julian/Desktop/irc/irc.sqlite") as conn:
        channels = conn.execute(
            """
            SELECT distinct(channel) from messages
            """
        )
        for channel, in channels:
            if channel.startswith(("freenode_", "oftc_")):
                _, _, real_channel = channel.partition("_")
                print(
                    """
                    UPDATE messages
                    SET channel=?
                    WHERE channel=?
                    """, (real_channel, channel)
)
                conn.execute(
                    """
                    UPDATE messages
                    SET channel=?
                    WHERE channel=?
                    """, (real_channel, channel)
                )
