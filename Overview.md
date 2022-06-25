# FetchBot: Rover martien intelligent 

Construis un rover martien avec une carte Raspberry Pi et programme-le avec des techniques d'intelligence artificielle de reconnaissance d'images pour aller rechercher de précieux tubes sur Mars en 2026!

<div align="center">
<h4>Le rover martien Fetch en 2026 à la recherche des tubes laissés sur mars en 2022 par le rover Perseverance - <a href="https://mars.nasa.gov/resources/24761/fetch-rover-approaching-sample-tubes-artists-concept/">Vue d'artiste</a>:</h4> 
</div>

<img src="images/fetch-rover.jpg" alt="drawing" width="600"></img>

## Public ciblé

* A partir de **10 ans** pour les activités de reconnaissance d'images, construction du robot, et **programmation en Scratch**.
* A partir de **14 ans** pour les activités de reconnaissance d'images, construction du robot, et **programmation en Python**.


## Motivations des activités

En 2026, l'Agence Spatiale Européenne (ESA) et la National Aeronautics and Space Administration (NASA) enverront [un rover sur Mars avec pour mission de récuperer des tubes contenant des échantillons de sol martien](https://fr.wikipedia.org/wiki/Mars_Sample_Return#Mission_Sample_Retrieval_Lander_(SRL)). Le rover, qui s'appelle Fetch (qui signifie 'récupérer' en anglais), devra être capable de se déplacer, de retrouver les tubes, et de les récupérer de la façon la plus autonome possible. Pour cela, Fetch utilisera des techniques d'intelligence artificielle, notamment de reconnaissance d'images pour trouver de façon autonome les tubes déposés sur le sol par le rover [Perseverance](https://fr.wikipedia.org/wiki/Exploration_de_Mars_par_Perseverance) en 2022. 

Les activités proposées ici visent à faire découvrir comment concevoir un système d'intelligence artificielle pour de la reconnaissance d'images, et comment permettre à un rover martien de l'utiliser. 

## Aperçu

Les activités se décomposent en trois parties: Reconnaissance d'images, construction du rover, et contrôle intelligent du rover.

### 1. Reconnaissance d'images

Tout d'abord, nous expliquons comment créer **un modèle prédictif pour la reconnaissance d'image**. On utilisera pour cela la *[Teachable Machine](https://teachablemachine.withgoogle.com/)*. On montrera ensuite comment le modèle peut être **utilisé dans un programme de façon simple avec Scratch ou en Python** pour retrouver des tubes sur un sol martien. 

Ce sont les activités 1 à 3:


Numéro activité | Activité | Age | Temps estimé
 :--- | :--- | :--- | :--- 
1 | Reconnaissance d'images avec la Teachable Machine | 10-18| 2-4h
2 | Reconnaissance d'images avec Scratch | 10-14  | 2-4h
3 | Reconnaissance d'images avec Python | 14-18  | 2-4h

Exemple de l'interface Teachable Machine que vous utiliserez pour apprendre à une IA à reconnaître des images (par exemple retrouver des tubes sur un sol martien):


<img src="./images/TM_5_tube_other_fr.jpg"  width="600"/> 

</div>

```{note}
Les activités 2 et 3 sont indépendantes, mais nécessitent d'avoir fait l'activité 1 pour créer un modèle de reconnaissance d'images.
```

### 2. Construction du FetchBot

La deuxième partie consistera à **construire un rover**, appelé 'FetchBot', et à programmer des déplacements. Une carte programmable [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) et le [CamJam EduKit](https://camjam.me/?page_id=1035) seront utilisés (Le CamJam EduKit fournit toutes les pièces nécessaires à la construction du rover: Les roues, les moteurs, et la connectique). L'activité est prévue pour être **simple, relativement abordable financièrement** (Environ 80 euros en tout pour un CamJam EduKit, une carte programmable Raspberry Pi, et une caméra), et offrant une **large liberté dans la 'personnalisation' de l'apparence du rover**.  

Ce sont les activités 4 à 6:

Numéro activité | Activité | Age | Temps estimé
 :--- | :--- | :--- | :--- 
4 | Construction du FetchBot | 10-18 | 2-4h
5 | Contrôle du FetchBot avec Scratch | 10-14 | 2-4h
6 | Contrôle du FetchBot avec Python | 14-18 | 2-4h

Exemples de rovers FetchBot construits un chassis en carton, en impression 3D, ou en bois:

||||
:--- | --- | ---: |
|<img src="./images/CamJam_Box.jpg" width="230"/>  |<img src="./images/CamJam_3DPrint.jpg" width="300"/> | <img src="./images/CamJam_Wood.png" width="350"/>|
|<a href="https://www.youtube.com/watch?v=LJDEV7rGwaM">Chassis en carton (avec la boîte du CamJam EduKit)</a>|<a href="https://camjam.me/?page_id=1035">Chassis en impression 3D</a>|<a href="https://www.youtube.com/watch?v=LKTpj8QHWEc">Chassis en bois</a>|

```{note}
Les activités 5 et 6 sont indépendantes, mais nécessitent d'avoir fait l'activité 4 de construction du rover.
```

### 3. Contrôle intelligent du rover

La troisième partie consistera à **utiliser le modèle de reconnaissance d'image sur le rover**, pour permettre à celui-ci de retrouver de façon autonome des tubes dans son environnement. Nous proposons un sol martien à imprimer, de façon à rendre l'activité proche de ce qu'un rover martien pourra voir une fois à destination! 

Ce sont les activités 7 à 9:

Numéro activité | Activité | Age | Temps estimé
 :--- | :--- | :--- | :--- 
7 | FetchBot avec Caméra | 10-18 | 2-4h
8 | Contrôle du FetchBot et reconnaissance d'images avec Scratch (Adacraft) | 10-14 | 2-4h
9 | Contrôle du FetchBot et reconnaissance d'images avec Python | 14-18 | 2-4h

```{note}
Les activités 8 et 9 sont indépendantes, mais nécessitent d'avoir fait les activités précédentes (reconnaissance d'images, construction du rover, et d'avoir monté la caméra).
```

## Objectifs pédagogiques 

Les activités permettent d'appréhender et s'approprier les notions d'algorithmes, de logigrammes, et les concepts de bases 

* de la programmation (conditions, boucles, variables, objets),
* de robotique (construction d'un rover, câblage d'une carte programmable avec des moteurs et une batterie),
* de l'intelligence artificielle (entrainer un modèle de prédiction avec des exemples, utiliser le modèle dans un programme).


### 1. Référentiel FMTTN

Création de contenus:

* Savoir: Programmation et logigrammes.
* Savoir-Faire: Lire un algorithme simple, Écrire un algorithme simple, Lire un programme simple, Écrire un programme simple, Identifier des éléments relatifs à la programmation et aux logigrammes.
* Compétences: Concevoir un algorithme pour résoudre un problème simple, Concevoir un programme pour résoudre un problème, Porter un regard critique sur les raisons d’être et les conséquences induites par un algorithme.

### 2. Référentiel MIT AI Ethics

[Un programme d'études sur l'éthique de l'intelligence artificielle pour les élèves de collège](https://docs.google.com/document/d/1pQ8D4iDnwKoiveJOZZgy6SLvgDD1nYQOPFUwyuBpEic/edit#) (Page 7)

* 1 - Comprendre les mécanismes de base des systèmes d'intelligence artificielle. 
* 1.a. Connaître trois parties d'un algorithme : entrée, étapes pour changer l'entrée, sortie. 
* 1.b. Savoir que l'intelligence artificielle est un type d'algorithme spécifique et comporte trois parties spécifiques : ensemble de données, algorithme d'apprentissage et prédiction. 
* 1.c Comprendre le problème de la classification dans le contexte de l'apprentissage automatique supervisé. Comprendre comment la quantité de données d'entraînement affecte la précision et la robustesse d'un modèle d'apprentissage automatique supervisé. 
* 2.c. Connaître le terme « biais algorithmique » dans le contexte de la classification.
	* Comprendre l'effet des données d'entraînement sur la précision d'un système d'apprentissage automatique.
	* Reconnaître que les humains ont le pouvoir de conserver des ensembles de données de formation.
	* Comprendre comment la composition des données d'entraînement affecte “le résultat”  d'un système d'apprentissage automatique supervisé.
* 4.b. Identifier les ensembles de données nécessaires pour former un système d'IA pour atteindre cet objectif.
 




