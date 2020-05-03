CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	PRIMARY KEY(username)
);

CREATE TABLE rooms (
    room VARCHAR(20) NOT NULL,
	numAlive INTEGER NOT NULL,
	numDead INTEGER NOT NULL,
    PRIMARY KEY(room)
);


