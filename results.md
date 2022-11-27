
# Résultats
TME alignementfree Partie 2   
Lara Wahbi & Vitushanie Yogaranjan

## Fonction `minhash`:

Nous avons d'abord testé en créant une liste de k-mers de taille 100 (taille du sketch = 100). On utilise ici seulement la méthode des listes car elle s'est avérée être plus rapide que celle du dictionnaire de comptage.  
Nous avons obtenu les résultats suivants :  

 - `GCF_000008865.2_ASM886v2_genomic.fna GCF_008244785.1_ASM824478v1_genomic.fna 0.0 (0.0, 0.0)`
 - `GCF_000008865.2_ASM886v2_genomic.fna GCF_000005845.2_ASM584v2_genomic.fna 0.5873015873015873 (0.74, 0.74)`
 - `GCF_000008865.2_ASM886v2_genomic.fna GCF_000006945.2_ASM694v2_genomic.fna 0.0 (0.0, 0.0)`
 - `GCF_000008865.2_ASM886v2_genomic.fna GCF_000022165.1_ASM2216v1_genomic.fna 0.0 (0.0, 0.0)`
 - `GCF_008244785.1_ASM824478v1_genomic.fna GCF_000005845.2_ASM584v2_genomic.fna 0.0 (0.0, 0.0)`
 - `GCF_008244785.1_ASM824478v1_genomic.fna GCF_000006945.2_ASM694v2_genomic.fna 1.0 (1.0, 1.0)`
 - `GCF_008244785.1_ASM824478v1_genomic.fna GCF_000022165.1_ASM2216v1_genomic.fna 1.0 (1.0, 1.0)`
 - `GCF_000005845.2_ASM584v2_genomic.fna GCF_000006945.2_ASM694v2_genomic.fna 0.0 (0.0, 0.0)`
 - `GCF_000005845.2_ASM584v2_genomic.fna GCF_000022165.1_ASM2216v1_genomic.fna 0.0 (0.0, 0.0)`
 - `GCF_000006945.2_ASM694v2_genomic.fna GCF_000022165.1_ASM2216v1_genomic.fna 1.0 (1.0, 1.0)`

Pour la première comparaison, on compare deux espèces différentes, *Salmonella enterica* et *Escherichia coli*. On voit alors qu'aucun kmers en commun n'est trouvé.  
Pour la sixième comparaison, on compare deux souches de la même espèce, *Salmonella enterica*, les souches 14028S et LT2. On voit que tous les kmers sont communs.  
Pour la deuxième comparaison, on compare deux souches de la même espèce également, cette fois *Escherichia coli*, les souches Sakai et Sakai. Et ici on peut voir que la moitié des k-mers sont communs.  
On peut conclure que selon la taille du sketch qu'on décide d'obtenir, on peut arriver à visualiser la variabilité entre les génomes selon le rang taxonomique des organismes. Avec une taille de 100, cela n'est pas suffisant pour pouvoir différencier deux organimes qui sont de la même espèce et qui ne sont pas très différents. Inversement, cela n'est pas suffisant pour trouver des similarités entre organismes d'espèces différentes.  

  
On a donc retenté une nouvelle comparaison entre les deux souches de *Salmonella enterica* avec cette fois une liste de kmers de taille 1000, et on obtient le résultat suivant :
 - `GCF_008244785.1_ASM824478v1_genomic.fna GCF_000006945.2_ASM694v2_genomic.fna 0.9607843137254902 (0.98, 0.98)`
  
On arrive bien à détecter une différence entre ces souches, mais cependant cela prend environ 10 min (pour une seule comparaison), cette méthode est donc efficace lorsqu'on essaie de différencier deux souches de la même espèce, mais cela peut dépendre d'à quel point ils ont évolué indépendamment l'un de l'autre, comme on a pu le voir pour la comparaison n°2 et 6.
