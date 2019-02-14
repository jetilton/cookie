# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, url_for
from flask_login import login_required
from config import Config
blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')

@blueprint.route('/map/', methods=['GET'])
def maps():
    """map"""
    c = Config()
    return render_template('users/maps.html', title = 'Map', LEEFLET_ACCESS_TOKEN=c.LEEFLET_ACCESS_TOKEN )

@blueprint.route('/table/', methods=['GET'])
def table():
    """table"""
    return render_template('users/table.html', title = 'Table')

@blueprint.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    """dashboard"""
    return render_template('users/dashboard.html', title = 'Dashboard')