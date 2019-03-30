def slices(series, length):
    if type(series) != 'list':
        raise ValueError('Please supply a series.')
    series_length = len(series)
    if series_length < length:
        return 'Oscar Yankee Oscar is your case'
    while series_length >= length:
        digits = ''.join(str([series[i] for i in range(0, length)]))
        series_length -= 1
        del series[0]

    return digits


# print(slices([1,2,3,4,5], 5))



