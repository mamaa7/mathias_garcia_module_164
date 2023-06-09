"""Gestion des formulaires avec WTF pour les films
Fichier : gestion_films_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddFilm(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    reference_produits_regexp = "^\d{1,10}$"
    reference_produits_add_wtf = StringField("Référence du produit ", validators=[Length(min=1, max=10, message="min 1 max 10"),
                                                               Regexp(reference_produits_regexp,
                                                                      message="Pas de lettres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])
    couleur_produits_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    couleur_produits_add_wtf = StringField("Couleur du produit ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(couleur_produits_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])
    type_produits_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    type_produits_add_wtf = StringField("Type de produit ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(type_produits_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer produit")


class FormWTFUpdateFilm(FlaskForm):
    """
        Dans le formulaire "film_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    reference_produits_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    reference_produits_update_wtf = StringField("Clavioter la référence du produit ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(reference_produits_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    couleur_produits_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    couleur_produits_update_wtf = StringField("Clavioter la couleur du produit ",
                                            validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(couleur_produits_update_regexp,
                                                               message="Pas de chiffres, de "
                                                                       "caractères "
                                                                       "spéciaux, "
                                                                       "d'espace à double, de double "
                                                                       "apostrophe, de double trait "
                                                                       "union")
                                                        ])

    type_produits_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Zaf-zÀ-ÖØ-öø-ÿ]+$"
    type_produits_update_wtf = StringField("Clavioter le type de produit ",
                                         validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                     Regexp(type_produits_update_regexp,
                                                            message="Pas de chiffres, de "
                                                                    "caractères "
                                                                    "spéciaux, "
                                                                    "d'espace à double, de double "
                                                                    "apostrophe, de double trait "
                                                                    "union")
                                                     ])

    reference_produits_update_wtf = StringField("Référence du produit ", widget=TextArea())
    couleur_produits_update_wtf = StringField("Couleur du produit", widget=TextArea())
    type_produits_update_wtf = StringField("Type de produit", widget=TextArea())
    submit = SubmitField("Update produit")


class FormWTFDeleteFilm(FlaskForm):
    """
        Dans le formulaire "film_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_film_delete_wtf = StringField("Effacer ce produit")
    submit_btn_del_film = SubmitField("Effacer produit")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
