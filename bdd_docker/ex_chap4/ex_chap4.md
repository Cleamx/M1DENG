# Exercices chapitre 4

## Exercice 1

```SQL
explain analyse select * from banque
-- Seq Scan on banque  (cost=0.00..11.00 rows=100 width=778) (actual time=0.037..0.042 rows=50 loops=1) 

explain analyse select * from client
-- Seq Scan on client  (cost=0.00..4317.00 rows=200000 width=60) (actual time=0.012..18.459 rows=200000 loops=1)

select relname as table_name, relpages as nb_blocks
from pg_class
where relname in ('client', 'banque')
 
-- "banque"	0
-- "client"	2317
```

---

## Exercice 2

```SQL
SELECT id_client, nom_client, date_naissance 
FROM client 
WHERE date_naissance > '1965-01-01';
-- Execution Time: 34.089 ms

create index id_naissance on client(date_naissance)
-- Execution Time: 25.186 ms

```
Avec un index ça ne change rien il n'est pas utiliser donc le coup ne change pas (il entrainerait un coup supérieur)

---

## Exercice 3

```SQL
select nom_bnk, id_client 
from banque 
natural join client 
where banque.id_bnk = client.id_bnk
```

En créant l'index cela ne change rien à l'exécution, l'index n'est pas utiliser
