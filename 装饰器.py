

def My_decorate(f):
    def fn(*args, **kwargs):
        print('decorate called')
        return f(*args, **kwargs)
    return fn


@My_decorate
def fx():
    print('fx called')


fx()
