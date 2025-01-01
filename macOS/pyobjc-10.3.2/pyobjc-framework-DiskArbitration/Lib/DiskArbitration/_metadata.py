# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:28:38 2024
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
constants = """$kDADiskDescriptionBusNameKey$kDADiskDescriptionBusPathKey$kDADiskDescriptionDeviceGUIDKey$kDADiskDescriptionDeviceInternalKey$kDADiskDescriptionDeviceModelKey$kDADiskDescriptionDevicePathKey$kDADiskDescriptionDeviceProtocolKey$kDADiskDescriptionDeviceRevisionKey$kDADiskDescriptionDeviceTDMLockedKey$kDADiskDescriptionDeviceUnitKey$kDADiskDescriptionDeviceVendorKey$kDADiskDescriptionMatchMediaUnformatted@^{__CFDictionary=}$kDADiskDescriptionMatchMediaWhole@^{__CFDictionary=}$kDADiskDescriptionMatchVolumeMountable@^{__CFDictionary=}$kDADiskDescriptionMatchVolumeUnrecognized@^{__CFDictionary=}$kDADiskDescriptionMediaBSDMajorKey$kDADiskDescriptionMediaBSDMinorKey$kDADiskDescriptionMediaBSDNameKey$kDADiskDescriptionMediaBSDUnitKey$kDADiskDescriptionMediaBlockSizeKey$kDADiskDescriptionMediaContentKey$kDADiskDescriptionMediaEjectableKey$kDADiskDescriptionMediaEncryptedKey$kDADiskDescriptionMediaEncryptionDetailKey$kDADiskDescriptionMediaIconKey$kDADiskDescriptionMediaKindKey$kDADiskDescriptionMediaLeafKey$kDADiskDescriptionMediaNameKey$kDADiskDescriptionMediaPathKey$kDADiskDescriptionMediaRemovableKey$kDADiskDescriptionMediaSizeKey$kDADiskDescriptionMediaTypeKey$kDADiskDescriptionMediaUUIDKey$kDADiskDescriptionMediaWholeKey$kDADiskDescriptionMediaWritableKey$kDADiskDescriptionVolumeKindKey$kDADiskDescriptionVolumeMountableKey$kDADiskDescriptionVolumeNameKey$kDADiskDescriptionVolumeNetworkKey$kDADiskDescriptionVolumePathKey$kDADiskDescriptionVolumeTypeKey$kDADiskDescriptionVolumeUUIDKey$kDADiskDescriptionWatchVolumeName@^{__CFArray=}$kDADiskDescriptionWatchVolumePath@^{__CFArray=}$"""
enums = """$err_local_diskarbitration@14286848$kDADiskClaimOptionDefault@0$kDADiskEjectOptionDefault@0$kDADiskMountOptionDefault@0$kDADiskMountOptionWhole@1$kDADiskOptionDefault@0$kDADiskOptionEjectUponLogout@1$kDADiskOptionMountAutomatic@16$kDADiskOptionMountAutomaticNoDefer@32$kDADiskOptionPrivate@256$kDADiskRenameOptionDefault@0$kDADiskUnmountOptionDefault@0$kDADiskUnmountOptionForce@524288$kDADiskUnmountOptionWhole@1$kDAReturnBadArgument@-119930877$kDAReturnBusy@-119930878$kDAReturnError@-119930879$kDAReturnExclusiveAccess@-119930876$kDAReturnNoResources@-119930875$kDAReturnNotFound@-119930874$kDAReturnNotMounted@-119930873$kDAReturnNotPermitted@-119930872$kDAReturnNotPrivileged@-119930871$kDAReturnNotReady@-119930870$kDAReturnNotWritable@-119930869$kDAReturnSuccess@0$kDAReturnUnsupported@-119930868$"""
misc.update({})
misc.update({})
misc.update({})
functions = {
    "DASessionGetTypeID": (b"Q",),
    "DADiskClaim": (
        b"v^{__DADisk=}I^?^v^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"^{__DADissenter=}"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__DADissenter=}"},
                            2: {"type": b"^v"},
                        },
                    }
                },
            }
        },
    ),
    "DARegisterDiskDescriptionChangedCallback": (
        b"v^{__DASession=}^{__CFDictionary=}^{__CFArray=}^?^v",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__CFArray=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "DADiskCreateFromBSDName": (
        b"^{__DADisk=}^{__CFAllocator=}^{__DASession=}^t",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"c_array_delimited_by_null": True, "type_modifier": "n"}},
        },
    ),
    "DAApprovalSessionCreate": (
        b"^{__DASession=}^{__CFAllocator=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DADiskGetBSDName": (
        b"^t^{__DADisk=}",
        "",
        {"retval": {"c_array_delimited_by_null": True}},
    ),
    "DARegisterDiskDisappearedCallback": (
        b"v^{__DASession=}^{__CFDictionary=}^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                }
            }
        },
    ),
    "DASessionCreate": (
        b"^{__DASession=}^{__CFAllocator=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DARegisterDiskAppearedCallback": (
        b"v^{__DASession=}^{__CFDictionary=}^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                }
            }
        },
    ),
    "DASessionUnscheduleFromRunLoop": (
        b"v^{__DASession=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "DADiskGetTypeID": (b"Q",),
    "DADiskCopyIOMedia": (
        b"I^{__DADisk=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DADissenterCreate": (
        b"^{__DADissenter=}^{__CFAllocator=}i^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DADiskCreateFromIOMedia": (
        b"^{__DADisk=}^{__CFAllocator=}^{__DASession=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DASessionScheduleWithRunLoop": (b"v^{__DASession=}^{__CFRunLoop=}^{__CFString=}",),
    "DAUnregisterCallback": (b"v^{__DASession=}^v^v",),
    "DADissenterGetStatusString": (b"^{__CFString=}^{__DADissenter=}",),
    "DADiskSetOptions": (b"i^{__DADisk=}IZ",),
    "DAApprovalSessionUnscheduleFromRunLoop": (
        b"v^{__DASession=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "DASessionSetDispatchQueue": (b"v^{__DASession=}@",),
    "DADiskCreateFromVolumePath": (
        b"^{__DADisk=}^{__CFAllocator=}^{__DASession=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DADiskCopyDescription": (
        b"^{__CFDictionary=}^{__DADisk=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DADiskIsClaimed": (b"Z^{__DADisk=}",),
    "DADiskGetOptions": (b"I^{__DADisk=}",),
    "DADiskMountWithArguments": (
        b"v^{__DADisk=}^{__CFURL=}I^?^v^^{__CFString=}",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__DADissenter=}"},
                            2: {"type": b"^v"},
                        },
                    }
                },
                5: {"c_array_delimited_by_null": True, "type_modifier": "n"},
            }
        },
    ),
    "DAApprovalSessionScheduleWithRunLoop": (
        b"v^{__DASession=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "DAApprovalSessionGetTypeID": (b"Q",),
    "DADiskRename": (
        b"v^{__DADisk=}^{__CFString=}I^?^v",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__DADissenter=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "DADissenterGetStatus": (b"i^{__DADissenter=}",),
    "DARegisterDiskPeekCallback": (
        b"v^{__DASession=}^{__CFDictionary=}q^?^v",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                }
            }
        },
    ),
    "DADiskUnclaim": (b"v^{__DADisk=}",),
    "DADiskEject": (
        b"v^{__DADisk=}I^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__DADissenter=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "DARegisterDiskMountApprovalCallback": (
        b"v^{__DASession=}^{__CFDictionary=}^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"^{__DADissenter=}"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                }
            }
        },
    ),
    "DAUnregisterApprovalCallback": (b"v^{__DASession=}^v^v",),
    "DARegisterDiskEjectApprovalCallback": (
        b"v^{__DASession=}^{__CFDictionary=}^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"^{__DADissenter=}"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                }
            }
        },
    ),
    "DARegisterDiskUnmountApprovalCallback": (
        b"v^{__DASession=}^{__CFDictionary=}^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"^{__DADissenter=}"},
                        "arguments": {0: {"type": b"^{__DADisk=}"}, 1: {"type": b"^v"}},
                    }
                }
            }
        },
    ),
    "DADiskCopyWholeDisk": (
        b"^{__DADisk=}^{__DADisk=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "DADiskUnmount": (
        b"v^{__DADisk=}I^?^v",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__DADissenter=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "DADiskMount": (
        b"v^{__DADisk=}^{__CFURL=}I^?^v",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^{__DADisk=}"},
                            1: {"type": b"^{__DADissenter=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
}
cftypes = [
    ("DAApprovalSessionRef", b"^{__DASession=}", "DAApprovalSessionGetTypeID", None),
    ("DADiskRef", b"^{__DADisk=}", "DADiskGetTypeID", None),
    ("DADissenterRef", b"^{__DADissenter=}", "DADissenterGetTypeID", None),
    ("DASessionRef", b"^{__DASession=}", "DASessionGetTypeID", None),
]
expressions = {}

# END OF FILE