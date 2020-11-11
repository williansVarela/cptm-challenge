from django.forms.utils import ErrorList

class CustomErrorList(ErrorList):
    """
    Modified version of the original Django ErrorList class.

    ErrorList.as_text() does not print asterisks anymore.
    """
    def as_text(self):
        return '\n'.join(self)