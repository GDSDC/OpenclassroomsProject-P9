<h3 align="center">
    <img alt="Logo" title="#logo" width="250px" src="/assets/16004297044411_P7.png">
    <br>
</h3>


# OpenClassrooms Projet P9

- [Objectif](#obj)
- [Compétences](#competences)
- [Technologies](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)
- [Tests](#tests)
- [Présentation](#presentation)

<a id="obj"></a>
## Objectif

La jeune startup LITReview a pour objectif de commercialiser un produit permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.
L'objectif du projet est de développer cette application Web en utilisant Django.

<a id="competences"></a>
## Compétences acquises
- Développer une application web en utilisant Django
- Utiliser le rendu côté serveur dans Django

<a id="techs"></a>
## Technologies Utilisées
- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [HTML](https://developer.mozilla.org/fr/docs/Web/HTML)
- [JavaScrip](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [CSS](https://developer.mozilla.org/fr/docs/Web/CSS)

<a id="reqs"></a>
## Requirements
- django
- pillow
- python-dotenv
- whitenoise

<a id="architecture"></a>
## Architecture et répertoires
```
Project
├── litreview_project
│   ├── authentication          \
│   ├── feed                     \
│   ├── follows                   \__ applications django
│   ├── posts                     /
│   ├── review                   /
│   ├── ticket                  /
│   ├── litreview_project : répertoire du projet django
│   │    ├── settings.py : fichier de réglages django
│   │    ├── urls.py : fichier principal des endpoints
│   │    ├── ..
│   ├── media : répertoire de fichiers image
│   ├── db.sqlite3 : base de données
│   ├── manage.py : fichier principal de gestion django
│
|── requirements.txt
|── documentation
```

<a id="localconfig"></a>
## Configuration locale
## Installation

### 1. Récupération du projet sur votre machine locale

Clonez le repository sur votre machine.

```bash
git clone https://github.com/GDSDC/OpenclassroomsProject-P9.git
```

Accédez au répertoire cloné.
```bash
cd OpenclassroomsProject-P9
```

### 2. Création d'un environnement virtuel 
Créez l'environnement virtuel env.
```bash
python3 -m venv env
```

### 3. Activation et installation de votre environnement virtuel 

Activez votre environnement virtuel env nouvellement créé.
```bash
source env/bin/activate
```

Installez les paquets présents dans la liste requirements.txt.
```bash
pip install -r requirements.txt
```

### 4. Initialisation de la base de données

Accédez au dossier de travail.
```bash
cd litreview_project
```

Procédez à une recherche de migrations.
```bash
python manage.py makemigrations
```

Lancer les migrations nécessaires.
```bash
python manage.py migrate
```

## Utilisation

### 1. Démarrage du serveur local

Accédez au dossier de travail.
```bash
cd litreview_project
```

Démarrez le serveur local.
```bash
python manage.py runserver
```

### 2. Navigation

Accédez au site sur votre navigateur depuis l'url http://127.0.0.1:8000/

<a id="tests"></a>
### Tests

Utilisez les identifiants de connexion suivant pour tester l'application.

| Utilisateur           | Identifiant   | Mot de passe |
|-----------------------|---------------|--------------|
| Utilisateur Principal | `u_principal` | `up`         |
| Utilisateur Suivi n°1 | `u_suivi_1`   | `us1`        |
| Utilisateur Suivi n°2 | `u_suivi_2`   | `us1`        |
| Utilisateur Suiveur   | `u_suiveur`   | `us`         |

Voir la présentation pour en savoir plus sur les liens entre les utilisateurs de test.


<a id="presentation"></a>
### Présentation

[<img alt="presentation" width="480px" src="/assets/presentation.png">](https://docs.google.com/presentation/d/e/2PACX-1vQ0P70x7hJJTLe-yN9KdE04QLPV73KHRE3bU-ndA8SotkTT28NFNRux3MmXkiRAhSfYZsUIsSGK7iQe/pub?start=true&loop=false&delayms=5000)



