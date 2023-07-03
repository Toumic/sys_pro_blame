# Les règles du jeu

# La matrice
Elle comporte plusieurs points de référence :<br>
## La liste et le dictionnaire
`def graphes(tab2, guide):`<br>
`...."""Mise en situation matricielle."""`<br>
`....print(lineno(), '*** Multilignes :\n graphes.tab2:', tab2, '\n guide:', guide)`
### La liste [tab2]
Elle contient la série des multiples de deux, qui dès quand on y parvient, <br>
on sait qu'à partir de cet élément on divise par deux en suivant les quotients pairs.<br>
### Le dictionnaire {guide}
Il a des clés qui définissent le nombre d'éléments découverts dans cet algorithme, <br>
ainsi que des valeurs exprimant la série des nombres de cet algorithme. (maximum et minimum)
## Qualité du recouvrement idéologique
### Conjecture de Collatz & Problème de Syracuse
Cette application est un ensemble d'informations liées aux nombres pairs, son but est d'apporter<br><br>
`une aide visuelle * avec notamment, les trois axes torrentiels de l'ensemble {impair, tab2, pair}`,<br>
alignant les parités des nombres produits par le jeu (n/2, n*3+1)..<br>
D'autres lignées pourront voir le jour, celle traçant la séquence réelle produite par le jeu.<br><br>
`Les informations textuelles apportent une aide cognitive apparemment visuelle dans le texte`<br>
Au-delà des axes sont cités les taux des couvertures des sections..<br>
`'# Caractéristiques ; *nombre-original, *facteur-exposant, *terminal-maxi, *terminal-mini.'`<br>
`a,b=32,18 | c=a/b=1.77 | n(32)/c=18 | n(16)/c=9`<br>
<br>
##### **Solutions :**
* ###### Nombre de descentes et montées
  * ###### _Quantité de division_ :  # (Cas. Cumul. Cran)
    * **_Pour un nombre pair (40) divisé par deux (2)_**
      * `(40/2=20), puis (20/2=10) et (10/2=5)`. Le nombre de divisions est égal à deux (avant l'impair)
    * #### `_Quotients soustraits_` :  # (Cas. Cumul. Cran)
      * Pour ce même nombre divisé par deux.
        * `(40/2=20), puis (20/2=10) et (10/2=5)`. La soustraction (max/min) fait l'intervalle (30), `(40-10=30)`
  *  ###### _Quantité multipliée_ :  # (Cas. Cumul. Cran)
    * Pour un nombre impair (41) multiplié par trois (3). Donne toujours un résultat impair.
      * Car, _" Un nombre impair multiplié par deux, produit toujours un nombre pair."_
      * `(1*2=2), (3*2=6), (5*2=10), (7*2=14), (9*2=18)`. Traité unitaire universel.
      * Pour, un nombre pair divisé par deux, ayant un multiplicateur inversé de deux. `(4/2=4*2)`
      * (impair multiplié par impair = impair), (impair multiplié par pair = pair). 
      * `(41*3=123), (123+1=124)`. Donne toujours un nombre pair, l'opération se réalise une fois.
      * #### `_Quantité additionnée_` :  # (Cas. Cumul. Cran)
        * Pour mesurer le multiple minus (3). Le 83 est un axial suivant les graduations produites.
        * `(41*3=123), (123+1=124)`. À valeur d'intervalle (83) `(41+83=124)`
        * `(124-1=123), (123/3=41)`. À même valeur d'intervalle `(83)`
#### _
#### * . Problème de mémoire rencontré..
Différence en pourcentage = (Différence absolue / Moyenne) x 100<br>
Pour deux valeurs X et Y, la différence en pourcentage est la suivante :<br>
Différence absolue = |x - y|<br>
Moyenne = (x - y) / 2<br>
Différence en pourcentage = (|x - y|) / ((x - y) / 2)) * 100<br>

<br><br><br>top<br>
