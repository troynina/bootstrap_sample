from flask import Flask
from flask import render_template
from flask import request

def toweb(f):
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def myfunc():
        about = f.__doc__
        a = f.__annotations__
        if 'return' in a:
            a.pop('return')

        if request.form:
            res = f(**request.form)
        else:
            res = None

        return render_template('index2.html', about = about, a = a, res = res)

    return app

@toweb
def upper(s1: str, s2: str, s3: str) -> str:
    """
    Капитализируй это!

    Уменьши шрифт!

    Удлини введенную строку в 3 раза
    """
    return s1.upper() + ' ' + s2.lower() + ' ' + s3*3


upper.run(host='0.0.0.0', port="5001")