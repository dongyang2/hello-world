class CustomError(Exception):

    def __init__(self, info):
        self.error_info = info


if __name__ == '__main__':
    import time
    print('-'*16, 'Start', time.ctime(), '-'*16, '\n')

    a = 1
    if a == 1:
        raise WindowsError

    print('\n', '-'*16, 'End', time.ctime(), '-'*16)
