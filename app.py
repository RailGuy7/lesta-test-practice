import redis
from flask import Flask

app = Flask(__name__)

# Подключение к Redis (хост будет "redis", так как это имя контейнера)
redis_cache = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/ping', methods=['GET'])
def ping():
    return {"status": "ok"}

@app.route('/count', methods=['GET'])
def count():
    # Увеличение счетчика в Redis
    visit_count = redis_cache.incr('visit_count')
    return {"visits": visit_count}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
