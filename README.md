# Les règles du jeu

# La matrice
Elle comporte plusieurs points de référence<br>
La visualisation de la poursuite résultante sous une forme paritaire. <br>
Chaque nombre produit a un taux de représentation parmi la famille des nombres pairs, <br>
les nombres pairs se suivent à pas de deux de manière chronologique. <br>
Dont la base est le nombre 2, en le transformant en mantisse, on délivre l'exposant. <br><br>
`Définition section = Elle a comme valeur initiale le produit (2^exposant) en commençant à ((2^exposant)/2)+2` <br>

## La liste et le dictionnaire
`"""def graphes(tab2, guide):`<br>
`...."Mise en situation matricielle."`<br>
`....print(lineno(), '*** Multilignes :\n graphes.tab2:', tab2, '\n guide:', guide)"""`return☺
#### La liste [tab2]
Contient la série des multiples de deux, qui dès quand on y parvient, <br>
on sait qu'à partir de là, le nombre est divisible par deux jusqu'au nombre ("premier nombre impair"_1) un.<br>
#### Le dictionnaire {guide}
Il a la définition des nombres découverts via cet algorithme, <br>
ainsi que les valeurs exprimées parmi la série des nombres produits. (maximum et minimum)

## Qualité du recouvrement idéologique
#### Conjecture de Collatz & Problème de Syracuse
Cette application est un ensemble d'informations liées aux nombres pairs, son but est d'apporter<br><br>
`une aide visuelle * avec notamment, les trois axes torrentiels de l'ensemble {impair, tab2, pair}`,<br>
alignant les parités des nombres produits par le jeu (n/2, n*3+1)..<br>
D'autres lignées voient le jour, celles traçant les séquences réelles produites par le jeu.<br><br>
`Les informations textuelles apportent une aide cognitive apparemment visuelle dans le texte,`<br>
` en diffusant différents résumés de démonstration statistique.`<br>
Au-delà de ces axes sont cités les taux des couvertures et des sections..<br>
`'# Caractéristiques ; *nombre-original, *facteur-exposant, *terminal-maxi, *terminal-mini.`<br>
Pour un nombre n(28) : `'a,b=32,16 | x=100*(n-a)/(a-b)=25 % | moyenne |.`<br>
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

<br><br><br>top<br>
