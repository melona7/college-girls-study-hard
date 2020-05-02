CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	email VARCHAR(40) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(username)
);

CREATE TABLE trees (
    tree BIT NOT NULL,
    PRIMARY KEY(tree)
);
