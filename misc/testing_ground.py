import time

def thread_timer(arg, arg1='j', arg2='d'):
    print(f'Starting! {arg} {arg2}')
    time.sleep(5)
    print('Stopped!')


def loadr(function):
    import time
    import threading
    t = threading.Thread(target=function)
    t.start()
    time.sleep(0.1)
    while t.is_alive():
        for i in range(4):
            if t.is_alive():
                print(f"Loading{'.' * i}   ", end='\r', flush=True)
                time.sleep(0.5)
    print('Loading Complete.')

if __name__ =='__main__':
    loadr(lambda: thread_timer('hey', arg2='hello'))

# from rich.console import Console
# from rich.live import Live
# from rich.text import Text
# import itertools
# dot_cycle = itertools.cycle(['','.','..','...'])
# console = Console()
# with Live('', refresh_per_second=10, console=console) as live:
#     while True:
#         current_dot = next(dot_cycle)
#         live.update(Text(f'Loading{current_dot}'))
#         time.sleep(0.5)



# t= threading.Thread(target=thread_timer)
# t.start()
# while t.is_alive():
#     for i in range(4):
#         print(f"Loading{'.' * i}   ", end='\r', flush=True)
#         time.sleep(0.5)
