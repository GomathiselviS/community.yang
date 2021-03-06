#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2020 Red Hat
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
---
module: fetch
short_description: Fetch given yang model and it's dependencies
author: Ganesh Nalawade (@ganeshrn)
description:
    - Fetch given yang model and its dependant yang model from device using netconf rpc.
options:
  name:
    description:
      - Name of the yang model to fetched from remote host. This will also fetch all
        the dependent yang models and return as part of result
    required: true
  dir:
    description:
      - This is an optional argument which provide the directory path in which the fetched
        yang modules will be saved. The name of the file is same as that of the yang module
        name prefixed with `.yang` extension.
"""
RETURN = """
number_schema_fetched:
  description: Total number of yang model fetched from remote host
  returned: always apart from low-level errors (such as action plugin)
  type: int
  sample: 10
fetched:
  description: This is a key-value pair were key is the name of the yang model and value
               is the yang model itself in string format
  returned: always apart from low-level errors (such as action plugin)
  type: dict
  sample: {"ietf-inet-types": "module ietf-inet-types ...<--snip-->"}
"""
EXAMPLES = """
- community.yang.fetch:
    name: "{{ item }}"
  loop:
    - openconfig-interface
    - openconfig-bgp
"""
