from spaceone.core.error import *


class ERROR_SERVICE_NOT_FOUND(ERROR_UNAVAILAVBLE):
    _message = 'Accessed the wrong service (service = {service})'

