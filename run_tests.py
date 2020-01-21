#!/usr/bin/env python
import os

def RunTest(toolset, addressModel, branch):
    runner = '--runner=BI-{toolset}-{addressModel} '.format(toolset=toolset, addressModel=addressModel)
    toolsets = '--toolsets={} '.format(toolset)
    bjamOptions = '"--bjam-options=-j8 address-model={}" '.format(addressModel)
    tag = '--tag={} '.format(branch)
    os.system('python run.py ' + runner + toolsets + bjamOptions + tag + '--comment=info.html')

RunTest('msvc-14.1', '32', 'develop')
RunTest('msvc-14.1', '64', 'develop')
RunTest('msvc-14.2', '32', 'develop')
RunTest('msvc-14.2', '64', 'develop')

RunTest('msvc-14.1', '32', 'master')
RunTest('msvc-14.1', '64', 'master')
RunTest('msvc-14.2', '32', 'master')
RunTest('msvc-14.2', '64', 'master')
