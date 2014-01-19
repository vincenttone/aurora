import os
import redis
from helper import singleton

@singleton
class Ticket:
    def get_ticket(self):
        lua_file_path = os.path.dirname(os.path.abspath(__file__))
        print lua_file_path
        lua_file_path = lua_file_path + '/' + 'ticket.lua'
        lua_file = open(lua_file_path, 'r')
        ticket_lua = lua_file.read()
        lua_file.close()
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        au_ticket =r.register_script(ticket_lua)
        return au_ticket(keys=[], args=[1, 1]);


if __name__ == '__main__':
    print Ticket().get_ticket()
