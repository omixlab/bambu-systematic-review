CREATE DATABASE IF NOT EXISTS bambu;

USE bambu;

CREATE TABLE IF NOT EXISTS users (
	id	INTEGER (50) NOT NULL AUTO_INCREMENT,
	name	VARCHAR(40) NOT NULL,
	email	VARCHAR(40) NOT NULL,
	password VARCHAR(300) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(name),
	UNIQUE(password),
	UNIQUE(email)
);

CREATE TABLE IF NOT EXISTS keys_tokens (
	id INTEGER (50) NOT NULL AUTO_INCREMENT,
	NCBI_API_KEY VARCHAR(36) NOT NULL,
	X_ELS_APIKey VARCHAR(32) NOT NULL,
	X_ELS_Insttoken	VARCHAR(32) NOT NULL,
	user_id	INTEGER,
	UNIQUE(X_ELS_Insttoken),
	PRIMARY KEY(id),
	FOREIGN KEY(user_id) REFERENCES users(id),
	UNIQUE(X_ELS_APIKey),
	UNIQUE(NCBI_API_KEY)
);

CREATE TABLE IF NOT EXISTS results (
	id INTEGER(50) NOT NULL AUTO_INCREMENT,
	user_id	INTEGER,
	status VARCHAR(20),
	celery_id VARCHAR(100) NOT NULL,
	pubmed_query VARCHAR(1024),
	elsevier_query VARCHAR(1024),
	result_json json,
	created_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id),
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS flashtext_models (
	id INTEGER(50) NOT NULL AUTO_INCREMENT,
	user_id	INTEGER,
	name VARCHAR(64) NOT NULL,
	type VARCHAR(24),
	path VARCHAR(255),
	created_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id),
	PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS tokens_password (
	id INTEGER (50) NOT NULL AUTO_INCREMENT,
	user_id	INTEGER,
	token VARCHAR(64) NOT NULL,
	link VARCHAR(90) NOT NULL,
	created_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(token),
	PRIMARY KEY(id),
	FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO flashtext_models (id, user_id, name, type, path)
VALUES (1, 1, 'Human', 'GENE_OR_GENE_PRODUCT', 'data/flashtext_models/genes_human.pickle'); 

INSERT INTO flashtext_models (id, user_id, name, type, path)
VALUES (2, 1, 'Danio rerio', 'GENE_OR_GENE_PRODUCT', 'data/flashtext_models/genes_dario_rerio.pickle'); 