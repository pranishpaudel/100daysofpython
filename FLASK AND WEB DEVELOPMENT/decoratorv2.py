import time



def fast_or_slow(function):

    def return_time():
        time.sleep(2)
        function
    return return_time
    


def fast_time():
    for i in range (10000000):
        i*i

@fast_or_slow
def slow_time():
    for i in range(10000000000):
        i*i

def calc_time(funct):
    initial_time= time.time()
    funct()
    final_time=time.time()
    print(final_time-initial_time)

calc_time(fast_time)
