#!/usr/bin/env python
#encoding: utf-8
#
#   (C) 2016 José Millán Soto <fid@gpul.org>
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

from knocky import *

import threading
import time
import os

global lastKey
lastKey = 0

global keys
keys = [['Fid', [(600, 0.3), (600, 2), (600, 0.3), (600, 2), (600, 0)]],
        ['Pablo', [(600, 2), (600, 0)]],
        ['Alberto', [(600, 3), (600, 1), (600, 0)]],
        ['Rach', [(600, 2), (600, 2), (600, 0)]],
        ['Javi', [(600, 4), (600, 1), (600, 0)]],
        ['Santi', [(600, 1), (600, 4), (600, 0)]]]

def hasKey(key):
    global keys
    print key, getCorrectKey(key, keys)


class getDataThread(threading.Thread):
    def run(self):
        while True:
            global lastKey
            t = raw_input()
            if t == 'bye':
                os.abort()
            lastKey = time.time()

class convertDataThread(threading.Thread):
    def __init__(self):
        super(convertDataThread, self).__init__()
        self._currentPassWd = []
        self._lastPress = 0
        self._listening = False
    def run(self):
        global lastKey
        while True:
            time.sleep(0.1)
            t = time.time()
            if self._listening:
                if (t - self._lastPress > 6) and len(self._currentPassWd):
                    self._currentPassWd.append((600, 0))
                    hasKey(self._currentPassWd)
                    self._currentPassWd = []
                    self._listening = False
                elif lastKey:
                    m = lastKey - self._lastPress
                    self._lastPress = lastKey
                    lastKey = 0
                    print m
                    self._currentPassWd.append((600, m))
            elif lastKey:
                self._listening = True
                self._lastPress = lastKey
                lastKey = 0

thread1 = getDataThread()
thread2 = convertDataThread()
thread1.start()
thread2.start()
