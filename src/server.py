"""Sanic BL server."""
from sanic import Sanic, response
from src.resolver import EdgeNormalizer
from src.apidocs import bp as apidocs_blueprint

app = Sanic()
app.config.ACCESS_LOG = False
app.blueprint(apidocs_blueprint)


@app.route('/resolve_predicate')
async def resolve(request):
    """
    :param request:
    :param concept:
    :param key:
    :return:
    """
    result = {}
    version = request.args.get('version', 'latest')
    resolver = EdgeNormalizer(bl_version=version)
    if isinstance(request.args['predicate'], list):
        for key in request.args['predicate']:
            answer = resolver.resolve_curie(key)
            if answer:
                result[key] = {
                    'identifier': answer.identifier,
                    'label': answer.label
                }
    else:
        key = request.args['predicate']
        answer = resolver.resolve_curie(key)
        if answer:
            result[key] = {
                'identifier': answer.identifier,
                'label': answer.label
            }
    return response.json(result)