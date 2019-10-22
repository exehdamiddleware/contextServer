#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Read_JSON(object):

    def read(self, name_of_file):
        file = name_of_file + ".json"

        with open(file) as f:
            d = json.load(f)

        return d

