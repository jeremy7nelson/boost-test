#!/usr/bin/env python
import os

def RunTest(toolset, branch):
    runner = '--runner=BI-{} '.format(toolset)
    toolsets = '--toolsets={} '.format(toolset)
    tag = '--tag={} '.format(branch)
    os.system('python run.py ' + runner + toolsets + '--bjam-options=-j8 ' + tag + '--comment=info.html')

RunTest('clang-8', 'develop')
RunTest('clang-9', 'develop')
RunTest('clang-10', 'develop')
RunTest('gcc-8', 'develop')
RunTest('gcc-9', 'develop')
RunTest('gcc-10', 'develop')
