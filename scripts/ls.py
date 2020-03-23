import os


class Meta(type):
    def __repr__(cls):
        cwd = os.getcwd()
        buffer = []
        for file_ in sorted(os.listdir(cwd)):
            buffer.append(file_)
        return '\n'.join(buffer)


class ls(metaclass=Meta):
    pass


# Now you can type 'ls' and have it do what ls does
