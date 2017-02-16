from redis import Redis

import django_rq

print "opening redis connection"

redis_conn = Redis(host='redis')
global queue
queue = Queue(connection=redis_conn) 
