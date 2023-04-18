from spaceone.core.error import *


class ERROR_UNSUPPORTED_SERVICE(ERROR_INVALID_ARGUMENT):
    _message = 'Unsupported service. (supported_services={services})'


class ERROR_UNSUPPORTED_RESOURCE(ERROR_INVALID_ARGUMENT):
    _message = 'Unsupported resource. (service={service}, resource={resource})'
