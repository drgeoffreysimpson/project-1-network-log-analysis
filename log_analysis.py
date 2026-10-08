import json
import pprint
import pathlib
import os,os.path
from pathlib import Path

def get_user_auth_times(user_id):
    """
    Returns a list of the date and time of logins for user userid from log/auth.log.x
    """

    return True


# Get all user ids that are failed logins with invalid user names. Return a dictionary mapping the userid to the number of invalid attempts
def get_invalid_logins():
    """
    Returns a dictionary mapping invalid user ids to # of failed logins on log/auth.log.x
    """

    return True


# Find all IP addresses for invalid logins, then see which IPs are also used for scanning
def compare_invalid_IPs():
    ''' '''
    return True


if __name__=="__main__":
    
    print(get_user_auth_times("tmoore"))
    print(get_invalid_logins())
    compare_invalid_IPs()
    #extract_log_files("ufw.log")
    #extract_log_files("auth.log")
    
