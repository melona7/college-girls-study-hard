CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	email VARCHAR(40) NOT NULL,
	filename VARCHAR(64) NOT NULL,
	password VARCHAR(256) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(username)
);

CREATE TABLE table_name (
    tree BIT NOT NULL,
    PRIMARY KEY(tree)
);
