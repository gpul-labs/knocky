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

def getDiff(received, expected, lenDiff = 0):
    if len(received) != len(expected):
        return False #TODO: handle
    return map(lambda x: (abs(x[0][0]- x[1][0]), abs(x[0][1] - x[1][1])),
               zip(received, expected))

def getCorrectKey(received, keys, margin = 0.8):
    aMargin = (len(received) - 1) * margin
    vals = {}
    for i in keys:
        diff = getDiff(received, i[1])
        if diff:
            sDiff = sum(map(lambda x: x[0], diff))/200.0 + sum(map(lambda x:x[1], diff))
            if sDiff < aMargin:
                vals[sDiff] = i
    if len(vals):
        return vals[min(vals)]
    else:
        return False
