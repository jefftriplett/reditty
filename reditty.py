"""
REST-based application that integrates with Itty and Redis

Based off ``redbottle`` (http://github.com/tnm/redbottle/)

"""
__author__ = 'Jeff Triplett'
__version__ = ('0', '1', '0')

import redis
from itty import get, post, run_itty, Response


r = redis.Redis()

def template(file, vars={}, **args):
    """
    Super simple template language...

    """
    contents = open(file, 'r').read()
    return str(contents % (dict(vars, **args)))


def keys_template(all_keys):
    temp = []
    for keys in all_keys:
        temp.append('<p><a href="/keyvalue/show/%(keys)s">%(keys)s</p>' % ({'keys': keys}))
    return '\n'.join(temp)


@get('/keyvalue/')
def template_keyvalue(request):
    all_keys = r.keys('*')
    values = dict(title='Key-Value Store', all_keys=keys_template(all_keys))
    return Response(template('templates/keys.html', values))


@post('/keyvalue/add/')
def template_add(request):
    key = request.POST.get('key')
    value = request.POST.get('value')
    if key and value:
        r.set(key, value)
    all_keys = r.keys('*')
    values = dict(title="Key-Value Pair", key=key, value=value, all_keys=keys_template(all_keys))
    return Response(template('templates/keys.html', values))


@post('/keyvalue/delete/')
def template_delete(request):
    key_delete = request.POST.get('key_delete')
    if key_delete:
        r.delete(key_delete)
    all_keys = r.keys('*')
    values = dict(title="Key-Value Pair", key=key_delete, all_keys=all_keys)
    return Response(template('templates/delete.html', values))


@get('/keyvalue/show/(?P<key>\w+)/')
def template_show(request, key):
    the_key = key.strip()
    value = r.get(the_key)
    values = dict(title=the_key, the_key=the_key, value=value)
    return Response(template('templates/show.html', values))


if __name__ == '__main__':
    run_itty()
