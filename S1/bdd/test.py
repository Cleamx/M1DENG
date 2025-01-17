from faker import Faker
import random

# Initialiser Faker
fake = Faker()

# Fichier où les requêtes SQL seront sauvegardées
output_file = "populate_data_with_constraints.sql"

# Fonction pour générer les requêtes SQL
def generate_sql():
    queries = []

    # 1. Table Diplome
    niveaux = ["Licence", "Master"]
    diplome_ids = []
    for i in range(5):
        niveau = random.choice(niveaux)
        nom_diplome = f"{niveau} en {fake.word().capitalize()}"
        queries.append(f"INSERT INTO Diplome (niveau, nom_diplome) VALUES ('{niveau}', '{nom_diplome}');")
        diplome_ids.append(i + 1)  

    # 2. Table AnneeAcademique
    annee_academique_ids = []
    for annee in range(2005, 2024):
        debut_annee = annee
        fin_annee = annee + 1
        queries.append(f"INSERT INTO AnneeAcademique (debut_annee, fin_annee) VALUES ({debut_annee}, {fin_annee});")
        annee_academique_ids.append(annee - 2004) 

    # 3. Table AnneeFormation
    annee_formation_ids = []
    for i in range(20):
        id_diplome = random.choice(diplome_ids)
        id_annee_academique = random.choice(annee_academique_ids)
        niveau = random.choice(["L1", "L2", "L3", "M1", "M2"])
        nb_etudiants_max = random.randint(20, 200)
        queries.append(
            f"INSERT INTO AnneeFormation (id_diplome, id_annee_academique, niveau, nb_etudiants_max) "
            f"VALUES ({id_diplome}, {id_annee_academique}, '{niveau}', {nb_etudiants_max});"
        )
        annee_formation_ids.append(i + 1)

    # 4. Table Enseignant
    enseignant_ids = []
    for i in range(10):
        nom = fake.last_name().replace("'", "''")
        prenom = fake.first_name().replace("'", "''")
        specialite = fake.job().replace("'", "''")
        queries.append(f"INSERT INTO Enseignant (nom, prenom, specialite) VALUES ('{nom}', '{prenom}', '{specialite}');")
        enseignant_ids.append(i + 1)

    # 5. Table UniteEnseignement
    ue_ids = []
    for i in range(30):
        id_annee_formation = random.choice(annee_formation_ids)
        nom_ue = f"UE {fake.word().capitalize()}".replace("'", "''")
        semestre = random.randint(1, 2)
        coefficient = round(random.uniform(1.0, 5.0), 1)
        queries.append(
            f"INSERT INTO UniteEnseignement (id_annee_formation, nom_ue, semestre, coefficient) "
            f"VALUES ({id_annee_formation}, '{nom_ue}', {semestre}, {coefficient});"
        )
        ue_ids.append(i + 1)

    # 6. Table ElementConstitutif
    element_ids = []
    for i in range(50):
        id_ue = random.choice(ue_ids)
        nom_element = f"EC {fake.word().capitalize()}".replace("'", "''")
        heures_cours = random.randint(5, 50)
        heures_td = random.randint(5, 50)
        heures_tp = random.randint(5, 50)
        id_enseignant = random.choice(enseignant_ids)
        queries.append(
            f"INSERT INTO ElementConstitutif (id_ue, nom_element, heures_cours, heures_td, heures_tp, id_enseignant) "
            f"VALUES ({id_ue}, '{nom_element}', {heures_cours}, {heures_td}, {heures_tp}, {id_enseignant});"
        )
        element_ids.append(i + 1)

    # 7. Table Etudiant (1,000 étudiants)
    etudiant_ids = []
    for i in range(1000):  # Générer 1,000 étudiants
        nom = fake.last_name().replace("'", "''")
        prenom = fake.first_name().replace("'", "''")
        id_annee_formation = random.choice(annee_formation_ids)
        queries.append(
            f"INSERT INTO Etudiant (nom, prenom, id_annee_formation) "
            f"VALUES ('{nom}', '{prenom}', {id_annee_formation});"
        )
        etudiant_ids.append(i + 1)

    # 8. Table Notes
    for i in range(200):
        id_etudiant = random.choice(etudiant_ids)
        id_element = random.choice(element_ids)
        note = round(random.uniform(0, 20), 1)
        queries.append(
            f"INSERT INTO Notes (id_etudiant, id_element, note) "
            f"VALUES ({id_etudiant}, {id_element}, {note});"
        )

    # 9. Table Avis
    for i in range(50):
        id_etudiant = random.choice(etudiant_ids)
        id_annee_formation = random.choice(annee_formation_ids)
        commentaire = fake.text(max_nb_chars=200).replace("'", "''")
        queries.append(
            f"INSERT INTO Avis (id_etudiant, id_annee_formation, commentaire) "
            f"VALUES ({id_etudiant}, {id_annee_formation}, '{commentaire}');"
        )

    with open(output_file, "w") as f:
        for query in queries:
            f.write(query + "\n")

    print(f"Les requêtes SQL ont été générées et sauvegardées dans {output_file}.")

generate_sql()
