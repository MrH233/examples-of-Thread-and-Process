import gevent
from gevent import monkey
import time
monkey.patch_all()


def task(msg):
    for i in range(10):     # content of task
        print(f"{task}, index:{i}, msg:{msg}")
        time.sleep(1)


gevent.joinall(
    [gevent.spawn(task, "task1 is going well"),
     gevent.spawn(task, "task2 is going well")]
)
