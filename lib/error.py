

class FatalError(Exception):
    '''An error from which we cannot recover.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FatalConfigError(FatalError):
    '''Something with the configuration is really bad.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)