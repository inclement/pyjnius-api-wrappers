from os import environ
from jnius import autoclass

# Kivy activity detection taken from plyer
if 'PYTHON_SERVICE_ARGUMENT' in environ:
    PythonService = autoclass('org.renpy.android.PythonService')
    activity = PythonService.mService
else:
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    activity = PythonActivity.mActivity

api_level = autoclass('android.os.Build$VERSION').SDK_INT

class ApiLevelError(NotImplementedError):
    def __init__(self, level):
        self.level = level
    def __str__(self):
        return ('This function needs access to Android API '
                'level {}'.format(self.level))

def check_for_api(level):
    '''Checks if api_level <= level, raising an error if not.'''
    if api_level < level:
        raise ApiLevelError(level)
    
