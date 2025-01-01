# This file is generated by objective.metadata
#
# Last update: Sat May 18 09:32:37 2024
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
enums = """$MPSGraphDeploymentPlatformIOS@1$MPSGraphDeploymentPlatformMacOS@0$MPSGraphDeploymentPlatformTvOS@2$MPSGraphDeploymentPlatformVisionOS@3$MPSGraphDeviceTypeMetal@0$MPSGraphExecutionStageCompleted@0$MPSGraphFFTScalingModeNone@0$MPSGraphFFTScalingModeSize@1$MPSGraphFFTScalingModeUnitary@2$MPSGraphLossReductionTypeAxis@0$MPSGraphLossReductionTypeMean@2$MPSGraphLossReductionTypeNone@0$MPSGraphLossReductionTypeSum@1$MPSGraphNonMaximumSuppressionCoordinateModeCentersHeightFirst@2$MPSGraphNonMaximumSuppressionCoordinateModeCentersWidthFirst@3$MPSGraphNonMaximumSuppressionCoordinateModeCornersHeightFirst@0$MPSGraphNonMaximumSuppressionCoordinateModeCornersWidthFirst@1$MPSGraphOptimizationLevel0@0$MPSGraphOptimizationLevel1@1$MPSGraphOptimizationProfilePerformance@0$MPSGraphOptimizationProfilePowerEfficiency@1$MPSGraphOptionsDefault@1$MPSGraphOptionsNone@0$MPSGraphOptionsSynchronizeResults@1$MPSGraphOptionsVerbose@2$MPSGraphPaddingModeAntiPeriodic@6$MPSGraphPaddingModeClampToEdge@3$MPSGraphPaddingModeConstant@0$MPSGraphPaddingModePeriodic@5$MPSGraphPaddingModeReflect@1$MPSGraphPaddingModeSymmetric@2$MPSGraphPaddingModeZero@4$MPSGraphPaddingStyleExplicit@0$MPSGraphPaddingStyleExplicitOffset@3$MPSGraphPaddingStyleONNX_SAME_LOWER@4$MPSGraphPaddingStyleTF_SAME@2$MPSGraphPaddingStyleTF_VALID@1$MPSGraphPoolingReturnIndicesGlobalFlatten1D@1$MPSGraphPoolingReturnIndicesGlobalFlatten2D@2$MPSGraphPoolingReturnIndicesGlobalFlatten3D@3$MPSGraphPoolingReturnIndicesGlobalFlatten4D@4$MPSGraphPoolingReturnIndicesLocalFlatten1D@5$MPSGraphPoolingReturnIndicesLocalFlatten2D@6$MPSGraphPoolingReturnIndicesLocalFlatten3D@7$MPSGraphPoolingReturnIndicesLocalFlatten4D@8$MPSGraphPoolingReturnIndicesNone@0$MPSGraphRNNActivationHardSigmoid@4$MPSGraphRNNActivationNone@0$MPSGraphRNNActivationRelu@1$MPSGraphRNNActivationSigmoid@3$MPSGraphRNNActivationTanh@2$MPSGraphRandomDistributionNormal@1$MPSGraphRandomDistributionTruncatedNormal@2$MPSGraphRandomDistributionUniform@0$MPSGraphRandomNormalSamplingBoxMuller@1$MPSGraphRandomNormalSamplingInvCDF@0$MPSGraphReductionModeArgumentMax@5$MPSGraphReductionModeArgumentMin@4$MPSGraphReductionModeMax@1$MPSGraphReductionModeMin@0$MPSGraphReductionModeProduct@3$MPSGraphReductionModeSum@2$MPSGraphResizeBilinear@1$MPSGraphResizeNearest@0$MPSGraphResizeNearestRoundingModeCeil@2$MPSGraphResizeNearestRoundingModeFloor@3$MPSGraphResizeNearestRoundingModeRoundPreferCeil@0$MPSGraphResizeNearestRoundingModeRoundPreferFloor@1$MPSGraphResizeNearestRoundingModeRoundToEven@4$MPSGraphResizeNearestRoundingModeRoundToOdd@5$MPSGraphScatterModeAdd@0$MPSGraphScatterModeDiv@3$MPSGraphScatterModeMax@5$MPSGraphScatterModeMin@4$MPSGraphScatterModeMul@2$MPSGraphScatterModeSet@6$MPSGraphScatterModeSub@1$MPSGraphSparseStorageCOO@0$MPSGraphSparseStorageCSC@1$MPSGraphSparseStorageCSR@2$MPSGraphTensorNamedDataLayoutCHW@4$MPSGraphTensorNamedDataLayoutDHWIO@10$MPSGraphTensorNamedDataLayoutHW@6$MPSGraphTensorNamedDataLayoutHWC@5$MPSGraphTensorNamedDataLayoutHWIO@3$MPSGraphTensorNamedDataLayoutNCDHW@7$MPSGraphTensorNamedDataLayoutNCHW@0$MPSGraphTensorNamedDataLayoutNDHWC@8$MPSGraphTensorNamedDataLayoutNHWC@1$MPSGraphTensorNamedDataLayoutOIDHW@9$MPSGraphTensorNamedDataLayoutOIHW@2$"""
misc.update(
    {
        "MPSGraphOptimizationProfile": NewType("MPSGraphOptimizationProfile", int),
        "MPSGraphTensorNamedDataLayout": NewType("MPSGraphTensorNamedDataLayout", int),
        "MPSGraphReductionMode": NewType("MPSGraphReductionMode", int),
        "MPSGraphFFTScalingMode": NewType("MPSGraphFFTScalingMode", int),
        "MPSGraphRNNActivation": NewType("MPSGraphRNNActivation", int),
        "MPSGraphDeploymentPlatform": NewType("MPSGraphDeploymentPlatform", int),
        "MPSGraphOptimization": NewType("MPSGraphOptimization", int),
        "MPSGraphPaddingMode": NewType("MPSGraphPaddingMode", int),
        "MPSGraphPoolingReturnIndicesMode": NewType(
            "MPSGraphPoolingReturnIndicesMode", int
        ),
        "MPSGraphDeviceType": NewType("MPSGraphDeviceType", int),
        "MPSGraphPaddingStyle": NewType("MPSGraphPaddingStyle", int),
        "MPSGraphNonMaximumSuppressionCoordinateMode": NewType(
            "MPSGraphNonMaximumSuppressionCoordinateMode", int
        ),
        "MPSGraphOptions": NewType("MPSGraphOptions", int),
        "MPSGraphExecutionStage": NewType("MPSGraphExecutionStage", int),
        "MPSGraphResizeMode": NewType("MPSGraphResizeMode", int),
        "MPSGraphLossReductionType": NewType("MPSGraphLossReductionType", int),
        "MPSGraphResizeNearestRoundingMode": NewType(
            "MPSGraphResizeNearestRoundingMode", int
        ),
        "MPSGraphRandomNormalSamplingMethod": NewType(
            "MPSGraphRandomNormalSamplingMethod", int
        ),
        "MPSGraphScatterMode": NewType("MPSGraphScatterMode", int),
        "MPSGraphRandomDistribution": NewType("MPSGraphRandomDistribution", int),
        "MPSGraphSparseStorageType": NewType("MPSGraphSparseStorageType", int),
    }
)
misc.update({})
misc.update({})
aliases = {
    "MPSGraphLossReductionTypeAxis": "MPSGraphLossReductionTypeNone",
    "MPSGraphOptionsDefault": "MPSGraphOptionsSynchronizeResults",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MPSGraph",
        b"argSortWithTensor:axis:descending:name:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"argSortWithTensor:axisTensor:descending:name:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"batchToSpaceTensor:spatialAxes:batchAxis:blockDimensions:usePixelShuffleOrder:name:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"batchToSpaceTensor:spatialAxesTensor:batchAxisTensor:blockDimensionsTensor:usePixelShuffleOrder:name:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"concatTensors:dimension:interleave:name:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"controlDependencyWithOperations:dependentBlock:name:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"MPSGraph",
        b"cumulativeMaximumWithTensor:axis:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeMaximumWithTensor:axisTensor:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeMinimumWithTensor:axis:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeMinimumWithTensor:axisTensor:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeProductWithTensor:axis:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeProductWithTensor:axisTensor:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeSumWithTensor:axis:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"cumulativeSumWithTensor:axisTensor:exclusive:reverse:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"depthToSpace2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": "Z"}}},
    )
    r(
        b"MPSGraph",
        b"depthToSpace2DTensor:widthAxisTensor:heightAxisTensor:depthAxisTensor:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": "Z"}}},
    )
    r(
        b"MPSGraph",
        b"forLoopWithLowerBound:upperBound:step:initialBodyArguments:body:name:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraph",
        b"forLoopWithNumberOfIterations:initialBodyArguments:body:name:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraph",
        b"ifWithPredicateTensor:thenBlock:elseBlock:name:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
            }
        },
    )
    r(
        b"MPSGraph",
        b"nonMaximumSuppressionWithBoxesTensor:scoresTensor:IOUThreshold:scoreThreshold:perClassSuppression:coordinateMode:name:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"nonMaximumSuppressionWithBoxesTensor:scoresTensor:classIndicesTensor:IOUThreshold:scoreThreshold:perClassSuppression:coordinateMode:name:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeBilinearWithGradientTensor:input:centerResult:alignCorners:layout:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeBilinearWithTensor:sizeTensor:centerResult:alignCorners:layout:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeBilinearWithTensor:sizeTensor:centerResult:alignCorners:name:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeNearestWithGradientTensor:input:nearestRoundingMode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeNearestWithTensor:sizeTensor:nearestRoundingMode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeNearestWithTensor:sizeTensor:nearestRoundingMode:centerResult:alignCorners:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeTensor:size:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeTensor:sizeTensor:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": "Z"}, 6: {"type": "Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeTensor:sizeTensor:mode:centerResult:alignCorners:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"resizeWithGradientTensor:input:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"sampleGridWithSourceTensor:coordinateTensor:layout:normalizeCoordinates:relativeCoordinates:alignCorners:paddingMode:nearestRoundingMode:constantValue:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}, 7: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"sampleGridWithSourceTensor:coordinateTensor:layout:normalizeCoordinates:relativeCoordinates:alignCorners:paddingMode:samplingMode:constantValue:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}, 7: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"sortWithTensor:axis:descending:name:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"sortWithTensor:axisTensor:descending:name:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"spaceToBatchTensor:spatialAxes:batchAxis:blockDimensions:usePixelShuffleOrder:name:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"spaceToBatchTensor:spatialAxesTensor:batchAxisTensor:blockDimensionsTensor:usePixelShuffleOrder:name:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"spaceToDepth2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": "Z"}}},
    )
    r(
        b"MPSGraph",
        b"spaceToDepth2DTensor:widthAxisTensor:heightAxisTensor:depthAxisTensor:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"MPSGraph",
        b"whileWithInitialInputs:before:after:name:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"MPSGraphCompilationDescriptor",
        b"compilationCompletionHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"MPSGraphCompilationDescriptor",
        b"setCompilationCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphCompilationDescriptor",
        b"setWaitForCompilationCompletion:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPSGraphCompilationDescriptor",
        b"waitForCompilationCompletion",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPSGraphExecutableExecutionDescriptor",
        b"completionHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"MPSGraphExecutableExecutionDescriptor",
        b"scheduledHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"MPSGraphExecutableExecutionDescriptor",
        b"setCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphExecutableExecutionDescriptor",
        b"setScheduledHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphExecutableExecutionDescriptor",
        b"setWaitUntilCompleted:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPSGraphExecutableExecutionDescriptor",
        b"waitUntilCompleted",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPSGraphExecutableSerializationDescriptor",
        b"append",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPSGraphExecutableSerializationDescriptor",
        b"setAppend:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"completionHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}},
                }
            }
        },
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"scheduledHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}},
                }
            }
        },
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"setCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"setScheduledHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"setWaitUntilCompleted:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphExecutionDescriptor", b"waitUntilCompleted", {"retval": {"type": b"Z"}})
    r(b"MPSGraphFFTDescriptor", b"inverse", {"retval": {"type": b"Z"}})
    r(b"MPSGraphFFTDescriptor", b"roundToOddHermitean", {"retval": {"type": b"Z"}})
    r(b"MPSGraphFFTDescriptor", b"setInverse:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"MPSGraphFFTDescriptor",
        b"setRoundToOddHermitean:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphGRUDescriptor", b"bidirectional", {"retval": {"type": b"Z"}})
    r(b"MPSGraphGRUDescriptor", b"flipZ", {"retval": {"type": b"Z"}})
    r(b"MPSGraphGRUDescriptor", b"resetAfter", {"retval": {"type": b"Z"}})
    r(b"MPSGraphGRUDescriptor", b"resetGateFirst", {"retval": {"type": b"Z"}})
    r(b"MPSGraphGRUDescriptor", b"reverse", {"retval": {"type": b"Z"}})
    r(
        b"MPSGraphGRUDescriptor",
        b"setBidirectional:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphGRUDescriptor", b"setFlipZ:", {"arguments": {2: {"type": b"Z"}}})
    r(b"MPSGraphGRUDescriptor", b"setResetAfter:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"MPSGraphGRUDescriptor",
        b"setResetGateFirst:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphGRUDescriptor", b"setReverse:", {"arguments": {2: {"type": b"Z"}}})
    r(b"MPSGraphGRUDescriptor", b"setTraining:", {"arguments": {2: {"type": b"Z"}}})
    r(b"MPSGraphGRUDescriptor", b"training", {"retval": {"type": b"Z"}})
    r(b"MPSGraphLSTMDescriptor", b"bidirectional", {"retval": {"type": "Z"}})
    r(b"MPSGraphLSTMDescriptor", b"forgetGateLast", {"retval": {"type": "Z"}})
    r(b"MPSGraphLSTMDescriptor", b"produceCell", {"retval": {"type": "Z"}})
    r(b"MPSGraphLSTMDescriptor", b"reverse", {"retval": {"type": "Z"}})
    r(
        b"MPSGraphLSTMDescriptor",
        b"setBidirectional:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPSGraphLSTMDescriptor",
        b"setForgetGateLast:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"MPSGraphLSTMDescriptor", b"setProduceCell:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPSGraphLSTMDescriptor", b"setReverse:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPSGraphLSTMDescriptor", b"setTraining:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPSGraphLSTMDescriptor", b"training", {"retval": {"type": "Z"}})
    r(b"MPSGraphPooling2DOpDescriptor", b"ceilMode", {"retval": {"type": b"Z"}})
    r(
        b"MPSGraphPooling2DOpDescriptor",
        b"includeZeroPadToAverage",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPSGraphPooling2DOpDescriptor",
        b"setCeilMode:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPSGraphPooling2DOpDescriptor",
        b"setIncludeZeroPadToAverage:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphPooling4DOpDescriptor", b"ceilMode", {"retval": {"type": b"Z"}})
    r(
        b"MPSGraphPooling4DOpDescriptor",
        b"includeZeroPadToAverage",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPSGraphPooling4DOpDescriptor",
        b"setCeilMode:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPSGraphPooling4DOpDescriptor",
        b"setIncludeZeroPadToAverage:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphShapedType", b"isEqualTo:", {"retval": {"type": b"Z"}})
    r(b"MPSGraphSingleGateRNNDescriptor", b"bidirectional", {"retval": {"type": "Z"}})
    r(b"MPSGraphSingleGateRNNDescriptor", b"reverse", {"retval": {"type": "Z"}})
    r(
        b"MPSGraphSingleGateRNNDescriptor",
        b"setBidirectional:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPSGraphSingleGateRNNDescriptor",
        b"setReverse:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPSGraphSingleGateRNNDescriptor",
        b"setTraining:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"MPSGraphSingleGateRNNDescriptor", b"training", {"retval": {"type": "Z"}})
    r(
        b"null",
        b"concatTensors:dimension:interleave:name:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"controlDependencyWithOperations:dependentBlock:name:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"null",
        b"depthToSpace2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"depthToSpace2DTensor:widthAxisTensor:heightAxisTensor:depthAxisTensor:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"forLoopWithLowerBound:upperBound:step:initialBodyArguments:body:name:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"null",
        b"forLoopWithNumberOfIterations:initialBodyArguments:body:name:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"null",
        b"ifWithPredicateTensor:thenBlock:elseBlock:name:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
            }
        },
    )
    r(
        b"null",
        b"resizeTensor:size:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"resizeTensor:sizeTensor:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"resizeWithGradientTensor:input:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"spaceToDepth2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"spaceToDepth2DTensor:widthAxisTensor:heightAxisTensor:depthAxisTensor:blockSize:usePixelShuffleOrder:name:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"null",
        b"whileWithInitialInputs:before:after:name:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
            }
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "MPSGraphExecutable", b"initWithMPSGraphPackageAtURL:compilationDescriptor:"
)
objc.registerNewKeywordsFromSelector("MPSGraphShapedType", b"initWithShape:dataType:")
objc.registerNewKeywordsFromSelector(
    "MPSGraphTensorData", b"initWithDevice:data:shape:dataType:"
)
objc.registerNewKeywordsFromSelector("MPSGraphTensorData", b"initWithMPSImageBatch:")
objc.registerNewKeywordsFromSelector("MPSGraphTensorData", b"initWithMPSMatrix:")
objc.registerNewKeywordsFromSelector("MPSGraphTensorData", b"initWithMPSMatrix:rank:")
objc.registerNewKeywordsFromSelector("MPSGraphTensorData", b"initWithMPSNDArray:")
objc.registerNewKeywordsFromSelector("MPSGraphTensorData", b"initWithMPSVector:")
objc.registerNewKeywordsFromSelector("MPSGraphTensorData", b"initWithMPSVector:rank:")
objc.registerNewKeywordsFromSelector(
    "MPSGraphTensorData", b"initWithMTLBuffer:shape:dataType:"
)
objc.registerNewKeywordsFromSelector(
    "MPSGraphTensorData", b"initWithMTLBuffer:shape:dataType:rowBytes:"
)
expressions = {}

# END OF FILE