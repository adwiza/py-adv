import logging
from threading import Thread
from queue import Queue
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Pool

def setup_logging():
    _log_queue = Queue()
    QueueListener(
        _log_queue, logging.FileHandler('out.log')).start()
    logging.getLogger().addHandler(QueueHandler(_log_queue))

    # Our parent process is running a thread that
    # logs messages:
    def write_logs():
        while True:
            logging.error("hello, I just did something")
    Thread(target=write_logs).start()


def runs_in_subprocess():
    print("About to log...")
    logging.error("hello, I did something")
    print("...logged")


if __name__ == '__main__':
    setup_logging()
    while True:
        with Pool() as pool:
            pool.apply(runs_in_subprocess)

# keep_running pattern
keep_running = True
a = 0
while keep_running:
    a = a+1
    keep_running = False