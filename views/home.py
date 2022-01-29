from flask import render_template, request
from config import app
from models.passw import Passw


class HomeViews(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html', context={
            'page_title': 'Главная',
            'passw_list': Passw.get_all_passw()
        })

    @staticmethod
    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('home/create.html', context={
                'page_title': 'Добавление',
            })
        else:
            resource = request.form.get('resource')
            login = request.form.get('login')
            passw = request.form.get('passw')
            new_passw = {
                'resource': resource,
                'login': login,
                'passw': passw
            }
            Passw.create_passw(new_passw)
            return render_template('home/result.html', context={
                'message': 'Пароль успешно добавлен'
            })
