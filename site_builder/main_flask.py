#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main_flask.py


from flask import Flask, render_template, url_for, redirect, g, session, request
from flask_wtf import FlaskForm
import jinja2
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from builder import build_module
from notifier import get_notifier, notify


__app__ = "Generatore Pagine HTML per PyMOTW-it 3"
__doc__ = """Interfaccia utente flask"""
__version__ = "0.2"
__date__ = "2017-08-23"
__changelog__ = """
2017-08-16: Prima stesura
2017-08-23: Compilazione di elenco di moduli
"""

nobj = get_notifier()
app = Flask(__name__)
app.config.from_object('config')
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('flask_templates')
])
app.jinja_loader = my_loader


@app.route('/')
@app.route('/index')
def index():
    session.clear()
    return render_template('index.html',
                           titolo=__app__)


@app.route('/generator', methods=['GET', 'POST'])
def generator():

    form = HTMLGeneratorForm()

    if form.validate_on_submit():
        module = form.modules.data.lower()
        log = '\n'.join(build_module(module.split()))
        session['log'] = log
        session['module'] = module
        return redirect(url_for('builder_log'))
    else:
        pass

    m = session.get('module', '')
    return render_template('generator.html',
                           titolo='Generatore Codice HTML',
                           form=form, defname=m)


@app.route('/builder_log', methods=['GET', 'POST'])
def builder_log():
    form = BuilderLog()
    lc = session.get('log', '')
    if form.validate_on_submit():
        return redirect(url_for('generator'))

    notify(nobj, 'Scritta pagina ' + session.get('module', ''))
    return render_template('builder_log.html',
                           titolo="Log elaborazione",
                           form=form, logcontent=lc)


class BuilderLog(FlaskForm):

    log = TextAreaField()


class HTMLGeneratorForm(FlaskForm):

    modules = StringField('modules', validators=[DataRequired()])
    rebuild_index = BooleanField('rebindex', default=False)
    rebuild_table = BooleanField('rebtbl', default=False)


app.run(debug=True)
