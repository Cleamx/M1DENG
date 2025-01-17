CREATE ROLE etudiant;
CREATE ROLE enseignant;
CREATE ROLE directeur_des_etudes;

-- 1. Vue qui permet aux étudiants de consulter les informations 
--    sur les formations disponibles
CREATE VIEW vue_etudiant_formations AS
SELECT 
    af.id_annee_formation,
    d.nom_diplome,
    af.niveau,
    af.nb_etudiants_max,
    aa.debut_annee,
    aa.fin_annee
FROM 
    AnneeFormation af
JOIN 
    Diplome d ON af.id_diplome = d.id_diplome
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique;

-- 2. Vue qui permet aux enseignants de consulter et de mettre à jour 
--    les notes des étudiants
CREATE VIEW vue_enseignant_notes AS
SELECT 
    e.nom AS nom_etudiant,
    e.prenom AS prenom_etudiant,
    ec.nom_element AS nom_element_constitutif,
    n.note
FROM 
    Notes n
JOIN 
    Etudiant e ON n.id_etudiant = e.id_etudiant
JOIN 
    ElementConstitutif ec ON n.id_element = ec.id_element;

-- 3. Vue qui permet au directeur des études de consulter 
--    les informations sur les formations disponibles
CREATE VIEW vue_directeur_formations AS
SELECT 
    af.id_annee_formation,
    d.nom_diplome,
    af.niveau,
    af.nb_etudiants_max,
    aa.debut_annee,
    aa.fin_annee
FROM 
    AnneeFormation af
JOIN 
    Diplome d ON af.id_diplome = d.id_diplome
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique;

-- 4. Vue qui permet aux étudiants de consulter les avis 
--    déposés par d’autres étudiants sur les formations
CREATE VIEW vue_etudiant_avis AS
SELECT 
    e.nom AS nom_etudiant,
    e.prenom AS prenom_etudiant,
    af.niveau AS niveau_formation,
    a.commentaire
FROM 
    Avis a
JOIN 
    Etudiant e ON a.id_etudiant = e.id_etudiant
JOIN 
    AnneeFormation af ON a.id_annee_formation = af.id_annee_formation;

-- 5. Vue qui permet aux enseignants de consulter les détails des unités d'enseignement 
--    et des éléments constitutifs qu'ils enseignent
CREATE VIEW vue_enseignant_details AS
SELECT 
    ens.nom AS nom_enseignant,
    ens.prenom AS prenom_enseignant,
    ens.specialite,
    ec.nom_element AS nom_element_constitutif,
    ue.nom_ue AS nom_unite_enseignement,
    ue.semestre,
    ue.coefficient
FROM 
    Enseignant ens
JOIN 
    ElementConstitutif ec ON ens.id_enseignant = ec.id_enseignant
JOIN 
    UniteEnseignement ue ON ec.id_ue = ue.id_ue;

-- Privilèges pour les étudiants, avoir accès aux informations des diplômes
-- pouvoir insérer des avis dans la table Avis, avoir accès aux avis déposés par tous les étudiants
GRANT SELECT ON vue_etudiant_formations TO etudiant;
GRANT SELECT, INSERT ON Avis TO etudiant;
GRANT SELECT ON vue_etudiant_avis TO etudiant;

-- Privilèges pour les enseignants, avoir accès aux notes des étudiants,
-- pouvoir insérer et mettre à jour les notes des étudiants,
-- avoir accès à aux détails des unités d'enseignement et des éléments constitutifs qu'ils enseignent
GRANT SELECT ON vue_enseignant_notes TO enseignant;
GRANT INSERT, UPDATE ON Notes TO enseignant;
GRANT SELECT ON vue_enseignant_details TO enseignant;

-- Privilèges pour le directeur des études, avoir accès aux informations des formations,
-- pouvoir insérer, mettre à jour et supprimer des formations,
-- avoir accès aux informations des diplômes et des années académiques
GRANT SELECT, INSERT, UPDATE, DELETE ON Diplome TO directeur_des_etudes;
GRANT SELECT, INSERT, UPDATE, DELETE ON AnneeAcademique TO directeur_des_etudes;
GRANT SELECT, INSERT, UPDATE, DELETE ON AnneeFormation TO directeur_des_etudes;
GRANT SELECT ON vue_directeur_formations TO directeur_etudes;