
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP21 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P21 : OC_Category_GP21 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C21 : OC_Category_P21 {
}
@end

@implementation
OC_Category_GP21 (Cat)
- (id)gpMethod1
{
    return @"GP21 - gpMethod1 - GP21(Cat)";
}
- (id)gpMethod5
{
    return @"GP21 - gpMethod5 - GP21(Cat)";
}
- (id)pMethod1
{
    return @"GP21 - pMethod1 - GP21(Cat)";
}
- (id)pMethod3
{
    return @"GP21 - pMethod3 - GP21(Cat)";
}
- (id)method1
{
    return @"GP21 - method1 - GP21(Cat)";
}
- (id)method2
{
    return @"GP21 - method2 - GP21(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp21", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp21(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp21(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
