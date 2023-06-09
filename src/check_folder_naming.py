import sys
import re

command_output = sys.argv[1]
parsedString = command_output.replace('£', ' ')
finalString = parsedString.replace('@', '\n')

folder = [ x.strip() for x in finalString.split('\n') ]

for i in folder:
    result = re.fullmatch(r"(?i)(1. DEV-TEST|2. PPE|3. STAGING|4. PRODUCTION)\/(api|apw|apa)-([A-Za-z]+)-([Uu][Ss]\d+)-([A-Za-z]+)(-\d)?\/(.*)$", i)
    if result == None:
        print(f"::set-output name=error_output::{'True'}")
        print(f"::set-output name=error_folder::{i}")
        sys.exit()
