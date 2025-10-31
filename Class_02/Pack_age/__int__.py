# __init__.py
# This file is intentionally left blank to indicate that this directory is a package.
# You can add package-level initialization code here if needed.
# For example, you might want to set up logging or import certain modules.



logging.basicConfig(level=logging.INFO)
import logging
logger = logging.getLogger(__name__)
logger.info("Package initialized")

# You can also define package-level variables or functions here.
PACKAGE_VERSION = "1.0.0"
def get_package_version():
    return PACKAGE_VERSION

logger.info(f"Package version: {get_package_version()}")
