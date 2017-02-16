from rq import Queue
from redis import Redis

print "opening redis connection"

redis_conn = Redis(host='localhost')
queue = Queue(connection=redis_conn) 

print "enqueuing message"

queue.enqueue("polls.worker.doit", 1)