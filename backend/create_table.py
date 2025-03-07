import mysql.connector
import bcrypt

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="120312"
)

cursor = conn.cursor()

# Création de la base de données et sélection
cursor.execute("CREATE DATABASE IF NOT EXISTS Forum;")
cursor.execute("USE Forum;")

# Création des tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cours (
        id_cours INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        nb_topics INT DEFAULT 0,
        nb_post INT DEFAULT 0,
        dernier_msg_date DATETIME DEFAULT CURRENT_TIMESTAMP
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id_user INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        mdp VARCHAR(255) NOT NULL,
        username VARCHAR(100) NOT NULL,
        id_cours INT,
        FOREIGN KEY (id_cours) REFERENCES cours(id_cours) ON DELETE SET NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS post (
        id_post INT AUTO_INCREMENT PRIMARY KEY,
        dernier_msg_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        corps TEXT NOT NULL,
        title VARCHAR(255) NOT NULL,
        id_user INT NOT NULL,
        FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id_topic INT AUTO_INCREMENT PRIMARY KEY,
        nb_posts INT DEFAULT 0,
        dernier_msg_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        id_post INT,
        FOREIGN KEY (id_post) REFERENCES post(id_post) ON DELETE CASCADE
    );
""")


try:
    cursor.execute("INSERT INTO users (email, mdp, username) VALUES (%s, %s, %s)",
                   ("ilyes@gmail.com", "ILYESdu12?", "ilyesB"))
    conn.commit()
except mysql.connector.Error as err:
    print(f"Erreur : {err}")

cursor.close()
conn.close()
