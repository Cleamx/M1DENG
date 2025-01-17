-- R1 : Nombre total d’étudiants par année de formation, par année 
-- et moyenne des notes finales pour les formations ayant accueilli plus de 5 étudiants depuis 2010 

-- R1.1 : Utilisation des jointures 
SELECT 
    af.id_annee_formation,
    aa.debut_annee,
    aa.fin_annee,
    COUNT(e.id_etudiant) AS nombre_etudiants,
    AVG(n.note) AS moyenne_notes
FROM 
    AnneeFormation af
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique
JOIN 
    Etudiant e ON af.id_annee_formation = e.id_annee_formation
JOIN 
    Notes n ON e.id_etudiant = n.id_etudiant
WHERE 
    aa.debut_annee >= 2010
GROUP BY 
    af.id_annee_formation, aa.debut_annee, aa.fin_annee
HAVING 
    COUNT(e.id_etudiant) > 5;

-- R1.2 : Utilisation de sous-requêtes 
SELECT  
    af.id_annee_formation, 
    aa.debut_annee, 
    aa.fin_annee, 
    COUNT(DISTINCT e.id_etudiant) AS total_etudiants, 
    (
        SELECT AVG(n.note)  
        FROM Notes n  
        WHERE n.id_etudiant IN ( 
            SELECT etu.id_etudiant  
            FROM Etudiant etu  
            WHERE etu.id_annee_formation = af.id_annee_formation 
        ) 
    ) AS moyenne_notes_finales 
FROM 
    AnneeFormation af 
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique 
JOIN 
    Etudiant e ON e.id_annee_formation = af.id_annee_formation 
WHERE 
    aa.debut_annee >= 2010 
GROUP BY 
    af.id_annee_formation, 
    aa.debut_annee, 
    aa.fin_annee 
HAVING 
    COUNT(DISTINCT e.id_etudiant) > 5;

-- Indexes : 
CREATE INDEX idx_notes_etudiant ON Notes(id_etudiant);
CREATE INDEX idx_etudiant_annee_formation ON Etudiant(id_annee_formation);
CREATE INDEX idx_annee_academique ON AnneeAcademique(debut_annee);

-- R2 : Intitulé des matières et nom de l’enseignant pour l'année de formation 1 du 
-- diplôme Licence en 2023-2024 sans notes en dessous de la moyenne générale 

-- R2.1 : Utilisation d’une sous-requête avec la moyenne générale 
WITH MoyenneGenerale AS (
    SELECT AVG(note) AS moyenne_generale 
    FROM Notes 
    JOIN AnneeFormation af ON Notes.id_element = af.id_annee_formation 
    JOIN AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique 
    WHERE aa.debut_annee = 2023 
      AND aa.fin_annee = 2024 
      AND af.niveau = 'L1'
)
SELECT  
    ec.nom_element,  
    ens.nom,  
    ens.prenom 
FROM 
    ElementConstitutif ec 
JOIN 
    Enseignant ens ON ec.id_enseignant = ens.id_enseignant 
JOIN 
    UniteEnseignement ue ON ec.id_ue = ue.id_ue 
JOIN 
    AnneeFormation af ON ue.id_annee_formation = af.id_annee_formation 
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique 
WHERE 
    af.niveau = 'L1'  
    AND aa.debut_annee = 2023  
    AND aa.fin_annee = 2024 
    AND ec.id_element NOT IN (
        SELECT n.id_element 
        FROM Notes n 
        JOIN Etudiant e ON n.id_etudiant = e.id_etudiant 
        WHERE n.note < (SELECT moyenne_generale FROM MoyenneGenerale)
    );

-- R2.2 : Utilisation d'une jointure avec filtrage 
WITH MoyenneParElement AS (
    SELECT 
        id_element, 
        AVG(note) AS moyenne_element 
    FROM 
        Notes 
    GROUP BY 
        id_element 
) 
SELECT  
    ec.nom_element, 
    ens.nom, 
    ens.prenom 
FROM 
    ElementConstitutif ec 
JOIN 
    Enseignant ens ON ec.id_enseignant = ens.id_enseignant 
JOIN 
    UniteEnseignement ue ON ec.id_ue = ue.id_ue 
JOIN 
    AnneeFormation af ON ue.id_annee_formation = af.id_annee_formation 
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique 
LEFT JOIN 
    MoyenneParElement mpe ON ec.id_element = mpe.id_element 
WHERE 
    af.niveau = 'L1'  
    AND aa.debut_annee = 2023  
    AND aa.fin_annee = 2024 
    AND (mpe.moyenne_element IS NULL OR mpe.moyenne_element >= 10);

-- Indexes :
CREATE INDEX idx_element_ue ON ElementConstitutif(id_ue);
CREATE INDEX idx_annee_formation_diplome ON AnneeFormation(id_diplome, niveau);

-- R3 : Filières sans étudiants ayant obtenu une moyenne générale inférieure à 4 en 2023-2024 
-- R3.1 : Utilisation d’une sous-requête avec exclusion 
SELECT DISTINCT 
    af.id_annee_formation 
FROM 
    AnneeFormation af 
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique 
JOIN 
    Etudiant e ON e.id_annee_formation = af.id_annee_formation 
WHERE 
    aa.debut_annee = 2023 
    AND aa.fin_annee = 2024 
    AND af.id_annee_formation NOT IN ( 
        SELECT 
            e.id_annee_formation 
        FROM 
            Notes n 
        JOIN 
            Etudiant e2 ON n.id_etudiant = e2.id_etudiant 
        WHERE 
            n.note < 4 
    );

-- R3.2 : Utilisation d'une jointure avec un GROUP BY et un HAVING 
SELECT 
    af.id_annee_formation 
FROM 
    Notes n 
JOIN 
    Etudiant e ON n.id_etudiant = e.id_etudiant 
JOIN 
    AnneeFormation af ON e.id_annee_formation = af.id_annee_formation 
JOIN 
    AnneeAcademique aa ON af.id_annee_academique = aa.id_annee_academique 
WHERE 
    aa.debut_annee = 2023 
    AND aa.fin_annee = 2024 
GROUP BY 
    af.id_annee_formation 
HAVING 
    MIN(n.note) >= 4;

-- Indexes :
CREATE INDEX idx_notes_etudiant ON Notes(id_etudiant, note);