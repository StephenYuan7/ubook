from app.libs.red_print import Redprint


api = Redprint('client')


@api.route('/test', methods=['GET'])
def check_client():
    return 'this is a test'
