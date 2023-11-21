r"""
Time tracking.
"""

# from tkinter import *s
from tkinter import ttk
from lachesis.util import create_logger

class Application(ttk.Frame):
    r"""
    Application
    """
    # pylint: disable=too-many-ancestors
    def __init__(self, main=None):
        #
        # Create a logger and start using it.
        logger = create_logger('Application.__init__')
        logger.debug('starting')
        #
        # Initialize UI
        ttk.Frame.__init__(self, main)
        self.grid()
        self.createWidgets()  # pylint: disable=invalid-name

    def createWidgets(self):
        r"""
        Create widgets
        """
        # pylint: disable=invalid-name
        self.quitButton = ttk.Button(self,
                                     text='Quit',
                                     command=self.quit)
        self.quitButton.grid()
        self.btn_create_event = ttk.Button(self,
                                           text='Create Event',
                                           command=self.create_event)
        self.btn_create_event.grid()

    def create_event(self):
        r"""
        Create an event
        """

if __name__ == '__main__':
    # sys.exit(main())
    app = Application()
    app.master.title('Sample Application')
    app.mainloop()
