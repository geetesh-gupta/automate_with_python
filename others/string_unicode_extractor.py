import re

unicode = re.sub(r"[\x00-\x7f]+", "", name)