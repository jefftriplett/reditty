"""
REST-based application that integrates with Itty and Redis

Based off ``redbottle`` (http://github.com/tnm/redbottle/)

"""
__author__ = 'Jeff Triplett'
__version__ = ('0', '1', '1')

import redis
from itty import get, post, run_itty, Response

try:
    import json
except ImportError:
    import simplejson as json


r = redis.Redis()


@post('/keyvalue/add/')
def keyvalue_add(request):
    key = request.POST.get('key')
    value = request.POST.get('value')
    success = False

    if key and value:
        r.set(key, value)
        success = True

    return Response(json.dumps({'status': success}), content_type='application/json')


@post('/keyvalue/delete/')
def keyvalue_delete(request):
    success = False

    if 'key' in request.POST:
        key = request.POST.get('key')
        key = key.strip()
        value = r.get(key)

        if value:
            r.delete(key)
            success = True

    return Response(json.dumps({'status': success}), content_type='application/json')


@get('/keyvalue/(?P<key>\w+)/')
def keyvalue_display(request, key):
    key = key.strip()
    value = r.get(key)
    success = False

    if not value:
        return Response(json.dumps({'status': success}), content_type='application/json')

    return Response(json.dumps({'key': key, 'value': value}), content_type='application/json')


@get('/keyvalue/')
def keyvalue_list(request):
    keys = r.keys('*')

    return Response(json.dumps({'keys': keys}), content_type='application/json')


if __name__ == '__main__':
    run_itty()
