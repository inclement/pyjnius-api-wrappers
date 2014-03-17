from jnius import autoclass, cast
from . import check_for_api, activity

ActivityInfo = autoclass('android.content.pm.ActivityInfo')

def set_no_preference():
    '''Leaves all orientation choices to the system (activity below, user
    settings etc.)'''
    activity.setRequestedOrientation(
        ActivityInfo.SCREEN_ORIENTATION_UNSPECIFIED)

def lock():
    '''Locks to the current screen orientation.'''
    check_for_api(18)
    activity.setRequestedOrientation(
        ActivityInfo.SCREEN_ORIENTATION_LOCKED)

def set_from_behind():
    '''Uses the orientation of the activity behind the current one.'''
    activity.setRequestedOrientation(
        ActivityInfo.SCREEN_ORIENTATION_BEHIND)

def set_landscape(mode='normal', user=False):
    '''Asks the activity to take a landscape orientation. Can optionally
    take either landscape direction, or use sensor information
    with/without listening to user settings.

    :param mode: One of 'normal', 'reverse', 'sensor' or 'user'.
    :param user: If True, tries to obey the user's orientation
                 settings where applicable. Defaults to False.
    '''

    if mode == 'normal':
        activity.setRequestedOrientation(
            ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE)
    if mode == 'reverse':
        activity.setRequestedOrientation(
            ActivityInfo.SCREEN_ORIENTATION_REVERSE_LANDSCAPE)
    if mode == 'sensor':
        if user:
            check_for_api(18)
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_USER_LANDSCAPE)
        else:
            check_for_api(9)
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_SENSOR_LANDSCAPE)

def set_portrait(mode='normal', user=False):
    '''Asks the activity to take a portrait orientation. Can optionally
    take either portrait direction, or use sensor information
    with/without listening to user settings.

    :param mode: One of 'normal', 'reverse', 'sensor' or 'user'.
    :param user: If True, tries to obey the user's orientation
                 settings where applicable. Defaults to False.
    '''

    if mode == 'normal':
        activity.setRequestedOrientation(
            ActivityInfo.SCREEN_ORIENTATION_PORTRAIT)
    if mode == 'reverse':
        activity.setRequestedOrientation(
            ActivityInfo.SCREEN_ORIENTATION_REVERSE_PORTRAIT)
    if mode == 'sensor':
        if user:
            check_for_api(18)
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_USER_PORTRAIT)
        else:
            check_for_api(9)
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_SENSOR_PORTRAIT)

def set_free(user=False, full=False):
    '''Allows any orientation, following the sensors.

    :param user: If True, try to follow the user's orientation
                 settings. Defaults to False.
    :param full: If True, tries to use the full range of orientations
                 even on devices that don't naturally support them.
                 Defaults to False.
    '''
    if user:
        if full:
            check_for_api(18)
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_FULL_USER)
        else:
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_USER)
    else:
        if full:
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_FULL_SENSOR)
        else:
            activity.setRequestedOrientation(
                ActivityInfo.SCREEN_ORIENTATION_SENSOR)
