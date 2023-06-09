"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    prenom_clients_regexp = "^[A-Za-zÀ-ÖØ-öø-ÿ\s]{1,50}$"
    prenom_clients_wtf = StringField("Ecrivez votre prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(prenom_clients_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    nom_genre_regexp = "^[A-Za-zÀ-ÖØ-öø-ÿ\s]{1,50}$"
    nom_genre_wtf = StringField("Ecrivez votre nom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                     Regexp(nom_genre_regexp,
                                                                            message="Pas de chiffres, de caractères "
                                                                                    "spéciaux, "
                                                                                    "d'espace à double, de double "
                                                                                    "apostrophe, de double trait union")
                                                                     ])

    tel_clients_regexp = "^0[0-9]{9}$"
    tel_clients_wtf = StringField("Ecrivez votre tel", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                     Regexp(tel_clients_regexp,
                                                                            message="Pas de chiffres, de caractères "
                                                                                    "spéciaux, "
                                                                                    "d'espace à double, de double "
                                                                                    "apostrophe, de double trait union")
                                                                     ])

    mail_clients_regexp = "^[^\s@]+@[^\s@]+\.[^\s@]+$"
    mail_clients_wtf = StringField("Ecrivez votre email ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                     Regexp(mail_clients_regexp,
                                                                            message="Pas de chiffres, de caractères "
                                                                                    "spéciaux, "
                                                                                    "d'espace à double, de double "
                                                                                    "apostrophe, de double trait union")
                                                                     ])

    rue_clients_regexp = "^[A-Za-z0-9À-ÖØ-öø-ÿ\s]{1,255}$"
    rue_clients_wtf = StringField("Ecrivez la rue ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                     Regexp(rue_clients_regexp,
                                                                            message="Pas de chiffres, de caractères "
                                                                                    "spéciaux, "
                                                                                    "d'espace à double, de double "
                                                                                    "apostrophe, de double trait union")
                                                                     ])

    npa_clients_regexp = "^\d{1,4}$"
    npa_clients_wtf = StringField("Ecrivez le NPA ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(npa_clients_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])

    ville_clients_regexp = "^[A-Za-zÀ-ÖØ-öø-ÿ\s]{1,50}$"
    ville_clients_wtf = StringField("Ecrivez le ville ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(ville_clients_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])
    submit = SubmitField("Enregistrer clients")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    nom_clients_update_wtf = StringField("Clavioter le Nom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_clients_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    prenom_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    prenom_clients_update_wtf = StringField("Clavioter le Prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(prenom_clients_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    tel_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    tel_clients_update_wtf = StringField("Clavioter le Numéro de téléphone ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(tel_clients_update_regexp,
                                                                                 message=" Uniquement des chiffres ")
                                                                          ])

    mail_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    mail_clients_update_wtf = StringField("Clavioter L'adresse e-mail ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(mail_clients_update_regexp,
                                                                                 message=" Une adresse e-mail valide avec un @ ")
                                                                          ])

    rue_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    rue_clients_update_wtf = StringField("Clavioter la Rue ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(rue_clients_update_regexp,
                                                                                 message="Pas de caractères spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    npa_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    npa_clients_update_wtf = StringField("Clavioter le Npa ", validators=[Length(min=2, max=4, message="min 2 max 4"),
                                                                          Regexp(npa_clients_update_regexp,
                                                                                 message="Uniquement des chiffres")
                                                                          ])

    ville_clients_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    ville_clients_update_wtf = StringField("Clavioter la Ville ", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                          Regexp(ville_clients_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    date_genre_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Update clients")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Nom")
    prenom_clients_delete_wtf = StringField("Prénom")
    tel_clients_delete_wtf = StringField("Numéro de téléphone")
    mail_clients_wtf = StringField("Adresse e-mail")
    rue_clients_delete_wtf = StringField("Rue")
    npa_clients_delete_wtf = StringField("Npa")
    ville_clients_delete_wtf = StringField("Ville")

    submit_btn_del = SubmitField("Effacer clients")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
