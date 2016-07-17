#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

warnings.filterwarnings(
	'ignore',
	'.*',
	UserWarning, 
	'warnings_filtering', 
	14
)
import warnings_filtering