import redis

REDIS_HOST = "redis-17429.c256.us-east-1-2.ec2.cloud.redislabs.com"
REDIS_PORT = 17429
REDIS_DB_NAME = "NetflixNepal"
REDIS_PASSWORD = "Wh5tVyqRa70JR0lypAhC1Ah9hhZ7al5M"

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
)

def is_user_approved(user_id):
    return redis_client.sismember(f"{REDIS_DB_NAME}:approved_users", user_id)

def set_user_approved(user_id, approved=True):
    if approved:
        redis_client.sadd(f"{REDIS_DB_NAME}:approved_users", user_id)
    else:
        redis_client.srem(f"{REDIS_DB_NAME}:approved_users", user_id)

def is_user_registered(user_id):
    return redis_client.hexists(f"{REDIS_DB_NAME}:user_stats", user_id)

def register_user(user_id):
    redis_client.hset(f"{REDIS_DB_NAME}:user_stats", user_id, 0)

def increment_user_stat(user_id):
    redis_client.hincrby(f"{REDIS_DB_NAME}:user_stats", user_id, 1)

def get_user_stat(user_id):
    return int(redis_client.hget(f"{REDIS_DB_NAME}:user_stats", user_id) or 0)

def is_user_in_cooldown(user_id):
    return redis_client.exists(f"{REDIS_DB_NAME}:cooldown:{user_id}")

def set_user_cooldown(user_id, duration):
    redis_client.setex(f"{REDIS_DB_NAME}:cooldown:{user_id}", duration, "1")
