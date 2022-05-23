import time
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
  def speed_diff():
    time1 = time.time()
    #print(time1)
    function()
    time2 = time.time()
    #print(time2)
    print(f"{function.__name__} run speed: {time2 - time1}s")
    return speed_diff
  speed_diff()

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
def slow_function():
    for i in range(100000000):
        i * i
