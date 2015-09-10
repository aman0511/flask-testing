from flask import Blueprint, render_template, request

mod = Blueprint('main', __name__, url_prefix="",
                template_folder="templates")


@mod.before_request
def before_request():
    print "Before request called"


@mod.after_request
def after_request(response):
    print "After request called"
    return response


@mod.teardown_request
def teardown_request(response):
    print "Tear Down called"
    return response


@mod.route("/", methods=['GET'])
def index():
    print request.args.get('email')
    print "Index is called"
    context = {
        'app': request.args.get('email')
    }
    return render_template('index.html', **context)


@mod.route('/test', methods=['GET'])
def test():
    return render_template('test.html')
