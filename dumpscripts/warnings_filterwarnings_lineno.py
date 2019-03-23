# warnings_filterwarnings_lineno.py

import warnings

warnings.filterwarnings(
    'ignore',
    '.*',
    UserWarning,
    'warnings_filter',
    6,
)

import warnings_filter
