def convert_complaints_python(num):
    if isinstance(num, str):
        return int(num.split('/')[1])
    return 0