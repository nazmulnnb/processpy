import multiprocessing
from typing import Any, Callable, Dict

class ProcessManager(object):
    def __init__(self, func: Callable, kill_previous: Any = False, concurrent_running: Any = False) -> None:
        """ProcessManager initializer

        Args:
            func (Callable): function to be executed
            kill_previous (Any, optional): Do you want to kill previous process? if not, new process won't be executed if concurrent is set to False. 
                                           If True, it will kill the unfinished previous process and start the new one.
                                           Defaults to False.
            concurrent_running (Any, optional): If True, all the process of the function will run concurrently. Defaults to False.

        Raises:
            ValueError: kill_previous and concurrent_running can't be used together. If you kill previous, what do you wanna run concurrently?
        """
        if concurrent_running and kill_previous:
            raise ValueError("Using kill_previous is not allowed while using concurrent_running.")
        self.func = func
        self.kill_previous = kill_previous
        self.concurrent_running = concurrent_running
        
        """
        We really don't need to keep track of multiple process. We will need that only when concurrent_running is true
        and we don't need to terminate any process. So, no use of the process ids. 
        In the future, all the process management will be added if needed.
        """
        self.process = None
    
    def run(self, kwargs: Dict = None) -> None:
        """ create a new process of the function

        Args:
            kwargs (Dict, optional): arguments to be passed to your function. Defaults to None.
        """
        if self.concurrent_running == False and self.process is not None and self.process.is_alive():
            if self.kill_previous:
                self.kill()
            else:
                return

        if kwargs == None:
            self.process = multiprocessing.Process(target=self.func)
        else:
            self.process = multiprocessing.Process(target=self.func, kwargs=kwargs)
        self.process.daemon = True
        self.process.start()
    
    def kill(self) -> None:
        """terminate the currently running process
        """
        if self.process is not None and self.process.is_alive:
            self.process.terminate()
