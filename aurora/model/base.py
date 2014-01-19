import json, redis
class Base:
    redis = None
    def connect(self):
        self.redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    def pack_json(self, dict):
        return json.dumps(dict)

    def unpack_json(self, json_data):
        return json.loads(json_data);
        
