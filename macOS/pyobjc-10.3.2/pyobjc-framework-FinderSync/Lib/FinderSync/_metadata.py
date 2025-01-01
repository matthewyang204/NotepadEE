# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:29:19 2024
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
constants = """$$"""
enums = """$FIMenuKindContextualMenuForContainer@1$FIMenuKindContextualMenuForItems@0$FIMenuKindContextualMenuForSidebar@2$FIMenuKindToolbarItemMenu@3$"""
misc.update({"FIMenuKind": NewType("FIMenuKind", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"FIFinderSyncController", b"isExtensionEnabled", {"retval": {"type": "Z"}})
    r(
        b"FIFinderSyncController",
        b"setLastUsedDate:forItemWithURL:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"FIFinderSyncController",
        b"setTagData:forItemWithURL:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"NSObject",
        b"beginObservingDirectoryAtURL:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"endObservingDirectoryAtURL:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"makeListenerEndpointForServiceName:itemURL:andReturnError:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"menuForMenuKind:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"Q"}}},
    )
    r(
        b"NSObject",
        b"requestBadgeIdentifierForURL:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"supportedServiceNamesForItemWithURL:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"toolbarItemImage", {"required": False, "retval": {"type": b"@"}})
    r(b"NSObject", b"toolbarItemName", {"required": False, "retval": {"type": b"@"}})
    r(b"NSObject", b"toolbarItemToolTip", {"required": False, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"valuesForAttributes:forItemWithURL:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": "@?",
                },
            },
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
