
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP37 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P37 : OC_Category_GP37 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C37 : OC_Category_P37 {
}
@end

@implementation
OC_Category_P37 (Cat)
- (id)gpMethod1
{
    return @"P37 - gpMethod1 - P37(Cat)";
}
- (id)gpMethod5
{
    return @"P37 - gpMethod5 - P37(Cat)";
}
- (id)pMethod1
{
    return @"P37 - pMethod1 - P37(Cat)";
}
- (id)pMethod3
{
    return @"P37 - pMethod3 - P37(Cat)";
}
- (id)method1
{
    return @"P37 - method1 - P37(Cat)";
}
- (id)method2
{
    return @"P37 - method2 - P37(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_p37", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_p37(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_p37(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}