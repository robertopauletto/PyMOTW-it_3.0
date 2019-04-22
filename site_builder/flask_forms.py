#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flask_forms.py

from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, StringField, TextAreaField, SubmitField,
    SelectField, DateField
)
from wtforms.validators import DataRequired, InputRequired
from flask_ckeditor import CKEditorField

__doc__ = """flask_forms.py.py"""
__version__ = "0.1"
__changelog__ = """

"""


class BuilderLog(FlaskForm):

    log = TextAreaField()


class NewArticleForm(FlaskForm):
    template = StringField('templatename')
    name = StringField('articlename')
    description = StringField('articledescr')
    purpose = StringField('articlenpurpos')
    categ = SelectField('categ')
    publish_date = DateField('publishdate', format='%d/%M/%Y')
    add_to_index = BooleanField('addtoindex', default=True)
    # editor = CKEditorField('test')


class CategorieForm(FlaskForm):
    nome = StringField('catname')


class HTMLGeneratorForm(FlaskForm):

    modules = StringField('modules', validators=[DataRequired()])
    rebuild_index = BooleanField('rebindex', default=False)
    rebuild_table = BooleanField('rebtbl', default=False)
    spellcheck = BooleanField('spcheck', default=False)
    fixed_sidebar = BooleanField('sbfixed', default=True)


class ConfigurationForm(FlaskForm):
    submit = SubmitField('Modifica configurazione')
