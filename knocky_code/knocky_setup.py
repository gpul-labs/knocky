#!/usr/bin/env python
#encoding: utf-8
#
#   (C) 2016 José Millán Soto <jmillan@kde-espana.org>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from knocky_input import *
from knocky import *
from knocky_config import *

import os
import sys

def menu():
    os.system('clear')
    print '1. List users'
    print '2. Add user'
    print '3. Delete user'
    print '4. Change password'
    print '5. Save'
    print '6. Open lock'
    print '0. Quit'
    r = raw_input()
    if r[0] not in ['0', '1', '2', '3', '4', '5', '6']:
        return menu()
    return r[0]

if os.path.exists(sys.argv[1]):
    data = load_config(sys.argv[1])
else:
    data = {}

def selectUser(data):
    users = data.keys()
    for i in range(len(users)):
        print i+1, users[i]
    print 'Select user:',
    try:
      u_index = int(raw_input().strip())-1
      if u_index >= 0:
          return users[u_index]
    except:
      return False

while True:
    r = menu()
    if r[0] == '0':
        sys.exit(0)
    elif r[0] == '1':
        print '\n'.join(data.keys())
        raw_input()
    elif r[0] == '2':
        new_user = raw_input()
        data[new_user] = []
    elif r[0] == '3':
        user = selectUser(data)
        if user:
            del data[user]
    elif r[0] == '4':
        user = selectUser(data)
        if user:
            cleanBuffer()
            new_key = getKey()
            data[user] = new_key
            print new_key
            raw_input()
    elif r[0] == '5':
        save_config(sys.argv[1], data)
    elif r[0] == '6':
        openLock()
