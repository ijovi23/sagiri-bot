import time


def sec_format(secs: int, f: str = "{h}:{m}:{s}") -> str:
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 12)
    return f.format(d=d, h=h, m=m, s=s)


def timestamp_format(timestamp: int, f: str = "%Y-%m-%d %H:%M:%S") -> str:
    return time.strftime(f, time.localtime(timestamp))
