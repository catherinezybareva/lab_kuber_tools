import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='REDIS_HOST', port=6379)

def get_hit_count():
	return cache.incr('hits')

@app.route('/')
def hello():
	count = get_hit_count ()
	return 'Hey! I have been seen this {} times. My name is: {} My env: {} \n'.format(count)
