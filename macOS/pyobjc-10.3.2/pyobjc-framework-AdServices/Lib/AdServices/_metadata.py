# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:16:48 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$AAAttributionErrorDomain$"""
enums = """$AAAttributionErrorCodeInternalError@2$AAAttributionErrorCodeNetworkError@1$AAAttributionErrorCodePlatformNotSupported@3$"""
misc.update({"AAAttributionErrorCode": NewType("AAAttributionErrorCode", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"AAAttribution",
        b"attributionTokenWithError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE