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
    print(result)
    return output
