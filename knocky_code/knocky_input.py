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

import sys
import select
import time

inputDeviceName = '/dev/ttyACM0'
inputDevice = open(inputDeviceName, 'r+')

def cleanBuffer():
    ready = select.select([inputDevice], [], [], 6)
    if inputDevice in ready[0]:
        inputDevice.read()

def openLock():
    inputDevice.write("open")
    inputDevice.flush()

def getKey():
    mVal = 0
    mInterval = 0
    minSensivity = 0.1
    mTime = time.time()
    isFirst = True
    passWd = []
    while True:
        ready = select.select([inputDevice], [], [], 6)
        if inputDevice in ready[0]:
            lin += inputDevice.readline()
            if '\n' in lin:
                lin = lin.replace('\n', '')
                try:
                  lTime = 0
                  if ':' in lin:
                      vals = map(lambda x: x.strip(), lin.split(':'))
                      if vals[0][0]=='V':
                        mVal = max(mVal, int(vals[1]))
                      elif vals[0][0]=='D':
                        if not mInterval:
                            mInterval += int(vals[1])/1000.0
                        lTime = time.time() - mTime + mInterval
                  if mVal and (lTime > minSensivity):
                      passWd.append((mVal, lTime if isFirst else 0))
                      mVal = 0
                      mInterval = 0
                      mTime = time.time()
                except ValueError:
                  pass
                except IndexError:
                  pass
        else:
            lTime = time.time() - mTime + mInterval
            if mVal and (lTime > minSensivity):
                  passWd.append([(mVal, lTime)])
            return passWd
