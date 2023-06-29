import datetime
import config

from application.db.people import get_employees
from application.salary import calculate_salary
from flask import render_template
from test_package.dirty_main import *

app = config.connex_app
app.add_api(config.basedir / 'spec.yml')


@app.route('/')
def index():
    return render_template('index.html', title='Flask',
                           cur_date=datetime.date.today(),
                           operations=func_list)


@app.route('/arithmetic/ui/')
def docs():
    pass


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print('Current date:', datetime.date.today())
    app.run(debug=True)
