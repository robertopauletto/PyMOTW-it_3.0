#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main_flask.py


from collections import OrderedDict
from flask import (
    Flask, render_template, url_for, redirect, g, session, request
)
from flask_ckeditor import CKEditor
from flask_forms import (
    BuilderLog, HTMLGeneratorForm, ConfigurationForm, NewArticleForm,
    CategorieForm
)
import jinja2
import json
from notifier import get_notifier, notify
import os.path
import webbrowser
import os
from builder import build_module, build_index, build_module_table, \
     set_builder_conf, get_categorie, crea_nuovo_articolo, save_categorie


__app__ = "Generatore Pagine HTML per PyMOTW-it 3"
__version__ = "0.2"
__date__ = "2017-08-23"
__changelog__ = """
2017-08-16: Prima stesura
2017-08-23: Compilazione di elenco di moduli
2019-03-24: Form di creazione articolo
"""

try:
    nobj = get_notifier()
except:
    nobj = None

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config.from_object('config')

# Dir template di flask diversa dal default
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('flask_templates')
])
app.jinja_loader = my_loader

builder_config = json.load(open('site_builder_config.json'))
set_builder_conf(
    OrderedDict(sorted(builder_config.items(), key=lambda t: t[0]))
)


@app.route('/')
@app.route('/index')
def index():
    session.clear()
    return render_template('index.html', titolo=__app__)


@app.route('/categorie', methods=['GET', 'POST'])
def categorie():
    file_categ = builder_config['file_categories']
    form = CategorieForm()
    listcat = [c[0] for c in get_categorie(file_categ)]
    if form.validate_on_submit():
        listcat.append(form.nome.data)
        save_categorie(file_categ, listcat)
        listcat = [c[0] for c in get_categorie(file_categ)]
        print()
    return render_template('categorie.html', form=form,
                           titolo='Categorie', listcat=listcat)


@app.route('/new_article', methods=['GET', 'POST'])
def new_article():
    """Creaazione file nuovo articolo"""
    form = NewArticleForm()
    tmpl = os.path.join(
        builder_config['new_article_folder'],
        builder_config['new_article_template']
    )
    form.categ.choices = get_categorie(builder_config['file_categories'])
    save_categorie(builder_config['file_categories'],
                   [c[0] for c in form.categ.choices])
    if form.validate_on_submit():
        template = form.template.data
        nome_modulo = form.name.data
        descrizione = form.description.data
        categ = form.categ.data
        purpose = form.purpose.data
        pubdate = form.publish_date.data
        ati = form.add_to_index.data
        outfile = os.path.join(builder_config['tran_dir'], nome_modulo + '.xml')

        crea_nuovo_articolo(
            outfile=outfile,
            filetemplate=template,
            categoria=categ,
            nome_modulo=nome_modulo,
            scopo=purpose,
            descrizione=descrizione,
            data_pubb=pubdate,
            aggiungi_a_indice=ati,
            filecron=builder_config['translated_modules']
        )
        session['log'] = "Creato file {}".format(os.path.abspath(outfile))
        return redirect(url_for('builder_log'))
    return render_template(
        'new_article.html', form=form, deftemplate=os.path.abspath(tmpl),
        titolo='Creazione file per nuovo articolo'
    )


@app.route('/generator', methods=['GET', 'POST'])
def generator():
    """Costruisce la pagina html per il modulo"""
    form = HTMLGeneratorForm()

    if form.validate_on_submit():
        module = form.modules.data.lower()
        is_sidebar_fixed = form.fixed_sidebar.data
        tmplog, check_sintassi = build_module(module.split(), is_sidebar_fixed)
        if form.spellcheck:
            pass
        log = '\n'.join(tmplog)
        if form.rebuild_index.data:
            log += '\n'.join(build_index())
            session['rebuild_index'] = True
        if form.rebuild_table.data:
            log += '\n'.join(build_module_table())
            session['rebuild_table'] = True

        session['log'] = log
        session['module'] = module
        session['check_sintassi'] = (check_sintassi if form.spellcheck.data
                                     else None)
        return redirect(url_for('builder_log'))
    else:
        pass

    m = session.get('module', '')
    return render_template('generator.html',
                           titolo='Generatore Codice HTML',
                           form=form, defname=m)


@app.route('/builder_log', methods=['GET', 'POST'])
def builder_log():
    """Mostra il risultato dell'elaborazione"""
    form = BuilderLog()
    lc = session.get('log', '')
    x = request
    if form.validate_on_submit():
        if 'apri' in request.form:
            fn, _ = os.path.splitext(session['module'])
            webbrowser.open('../html/' + fn + ".html" )
        else:
            return redirect(url_for('generator'))

    notify(nobj, 'Scritta pagina ' + session.get('module', ''))
    return render_template('builder_log.html',
                           titolo="Log elaborazione",
                           form=form, logcontent=lc)


@app.route('/config', methods=['GET', 'POST'])
def config():
    """Gestione dei parametri di configurazione"""
    titolo = 'Parametri di configurazione Configurazione'
    form = ConfigurationForm()
    if form.validate_on_submit():
        r = request
        _tmp(r.form)
    return render_template("config.html", myconf=builder_config,
                           titolo=titolo, form=form)


def _tmp(conf_flds):
    log = []
    for k, v in conf_flds:
        log.append(k)
    x = builder_config
    print()


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    """Gestione aggiornamenti sito online"""
    titolo = 'Gestione Aggiornamenti Sito'
    return render_template('uploader.html', titolo=titolo)


app.run(debug=True)
