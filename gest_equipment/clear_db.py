import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Liste des tables pour vérifier si 'django_admin_log' existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables dans la base de données:", tables)

# Si vous voulez supprimer une table spécifique (par exemple 'django_admin_log')
cursor.execute('DROP TABLE IF EXISTS django_admin_log')

# Validation des changements et fermeture de la connexion
conn.commit()
conn.close()

print("La table 'django_admin_log' a été supprimée si elle existait.")
