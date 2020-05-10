CREATE TABLE IF NOT EXISTS messages (
    timestamp DATETIME,
    channel TEXT,
    sender TEXT,
    contents TEXT
);
CREATE INDEX IF NOT EXISTS message_senders ON messages (sender);
CREATE INDEX IF NOT EXISTS message_channels ON messages (channel);
