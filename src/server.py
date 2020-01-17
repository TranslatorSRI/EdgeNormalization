"""Sanic BL server."""
from sanic import Sanic, response
from src.resolver import EdgeNormalizer
from src.apidocs import bp as apidocs_blueprint

app = Sanic()
app.config.ACCESS_LOG = False
app.blueprint(apidocs_blueprint)


@app.route('/resolve')
async def resolve(request):
    """
    :param request:
    :param concept:
    :param key:
    :return:
    """
    result = {}
    resolver = EdgeNormalizer()
    if isinstance(request.args['key'], list):
        for key in request.args['key']:
            answer = resolver.resolve_curie(key)
            if answer:
                result[key] = {
                    'identifier': answer.identifier,
                    'label': answer.label
                }
    else:
        key = request.args['key']
        answer = resolver.resolve_curie(key)
        if answer:
            result[key] = {
                'identifier': answer.identifier,
                'label': answer.label
            }
    return response.json(result)