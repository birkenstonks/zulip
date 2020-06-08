########################################################################
# DEFAULT VALUES FOR SETTINGS
########################################################################

# For any settings that are not set in the site-specific configuration file
# (/etc/zulip/settings.py in production, or dev_settings.py or test_settings.py
# in dev and test), we want to initialize them to sane defaults.
from .default_settings import *  # isort: skip

# Import variables like secrets from the prod_settings file
# Import prod_settings after determining the deployment/machine type
from .config import PRODUCTION
if PRODUCTION:
    from .prod_settings import *  # isort: skip
else:
    from .dev_settings import *  # isort: skip