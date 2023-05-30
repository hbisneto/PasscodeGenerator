"""
Requirements.py

- This file is used to check if system matches with the minimum requirements to run
"""
## Requirements File
## This file is used to check if system matches with the minimum requirements to run

import sys
import subprocess
from exception import Exceptions

## Change "REQUIRE" to "False" to skip system check
REQUIRE = True
## Change "REQUIRE" to "True" to allow system check

if REQUIRE == True:
   ## Target System
   TargetMajor = 3
   TargetMinor = 9
   TargetBuild = 0
   TargetVersion = f'{TargetMajor}.{TargetMinor}.{TargetBuild}'
   ## Target System

   ## Current System
   MajorVersion = sys.version_info[0]
   MinorVersion = sys.version_info[1]
   BuildVersion = sys.version_info[2]
   CurrentVersion = f'{MajorVersion}.{MinorVersion}.{BuildVersion}'
   ## Current System

   ## Uncomment to see information about your system
   ## print(f'>> My system current version: Python {CurrentVersion}')
   ## print(f'>> Required version to run: Python {TargetVersion}')

   def CheckVersion():
      if TargetMajor < MajorVersion:
         Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
      elif TargetMajor > MajorVersion:
         Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)
      else:
         if TargetMinor < MinorVersion:
            Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
         elif TargetMinor > MinorVersion:
            Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)
         else:
            if TargetBuild < BuildVersion:
               Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
            elif TargetBuild > BuildVersion:
               Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)