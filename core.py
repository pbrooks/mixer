import re


class NamedObject(object):

    @property
    def name(self):
        return " ".join(re.sub('([a-z])([A-Z])', r'\1 \2',  type(self).__name__).split())
