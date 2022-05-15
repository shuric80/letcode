#! /usr/bin/env python

import pytest
from collections import defaultdict


def convert(s: str, numRows: int) -> str:
    cnt = 0
    result = defaultdict(list)
    is_direct = True
    for index, w in enumerate(s):
        if is_direct:
            cnt += 1
            if cnt > numRows:
                is_direct = False
                cnt -= 2
        else:
            cnt -= 1
            if cnt == 0:
                is_direct = True
                cnt = 2
        result[cnt].append(w)

    output = str()
    for key, value in result.items():
        output += ''.join(value)
    return output


@pytest.mark.parametrize('s, num, output', (('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'), ('ABC', 1, 'ABC')))
def test_convert(s, num, output):
    assert convert(s, num) == output



if __name__ == "__main__":
    test_convert()
