
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP25 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P25 : OC_Category_GP25 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C25 : OC_Category_P25 {
}
@end

@implementation
OC_Category_P25 (Cat)
- (id)gpMethod1
{
    return @"P25 - gpMethod1 - P25(Cat)";
}
- (id)gpMethod5
{
    return @"P25 - gpMethod5 - P25(Cat)";
}
- (id)pMethod1
{
    return @"P25 - pMethod1 - P25(Cat)";
}
- (id)pMethod3
{
    return @"P25 - pMethod3 - P25(Cat)";
}
- (id)method1
{
    return @"P25 - method1 - P25(Cat)";
}
- (id)method2
{
    return @"P25 - method2 - P25(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_p25", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_p25(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_p25(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
