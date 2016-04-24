#coding:utf-8

import redis
from src import config

def getrediscli():
    pool=redis.ConnectionPool(host=config.redis_config['host'],
                              port=config.redis_config['port'],
                              db=config.redis_config['db'])

    # return redis.StrictRedis(connection_pool=pool,decode_responses=True)

    return redis.StrictRedis(host=config.redis_config['host'],
                              port=config.redis_config['port'],decode_responses=True)