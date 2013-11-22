import os

from openelex import COUNTRY_DIR

class PlaceBase(object):
    """Base class with common functionality for working 
    with state modules. 

    Intended to be subclassed by other base modules or
    state specific modules
    """

    def __init__(self, state='', place=''):
        if not state:
            self.state = self.__module__.split('.')[-2]
        else:
            self.state = state
        if not place:
            self.place = self.__module__.split('.')
        else:
           self.place = place
        # Save files to cache/ dir inside state directory
        self.cache_dir = os.path.join(COUNTRY_DIR, self.state, self.place, 'cache')
        self.mappings_dir = os.path.join(COUNTRY_DIR, self.state, self.place, 'mappings')
        try:
            os.makedirs(self.cache_dir)
        except OSError:
            pass
        try:
            os.makedirs(self.mappings_dir)
        except OSError:
            pass
        # Create ocd mappings csv if it doesn't exist
        open(os.path.join(self.mappings_dir, self.state + '_' + self.place + '.csv'), 'a').close()