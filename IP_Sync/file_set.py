# -*- encoding: utf-8 -*-
'''
@Description:  :
@Date          :2020/11/03 20:53:59
@Author        :a76yyyy
@version       :1.0
'''
import os
def file_set(file= None, type = None):
    if not os.path.exists(file):
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        if type == 'dir':
            os.makedirs(file)
        if type == 'file':
            with open(file, 'wb+') as handle:
                handle.close()
        if not os.path.exists(file):
            if os.path.isdir(file):
                os.makedirs(file)
            elif os.path.isfile(file):
                if not os.path.exists(os.path.dirname(file)):
                    os.makedirs(os.path.dirname(file))
                with open(file, 'wb+') as handle:
                    handle.close()
        return 0
    return 1