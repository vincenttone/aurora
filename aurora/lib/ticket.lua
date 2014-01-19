--initlize data                                                                                                    
local count = 0
local idc = ARGV[1]
local process = ARGV[2]
local count_key = "count"
--get count                                                                                                        
local count_exists = redis.call('exists', count_key)
if  count_exists == 0  then
    redis.call("set", count_key, 0)
    redis.call("expire", count_key, 1)
else
    redis.call("incr", count_key)
    count = redis.call("get", count_key)
end
count = string.format("%04d", count)
idc = string.format("%03d", idc)
process = string.format("%02d", process)
--get timestamp                                                                                                    
local time=redis.call('time')
local timestamp = time[1] - 360000000
local micro_second = time[2]
 
local id = timestamp..count..idc..process
return id
