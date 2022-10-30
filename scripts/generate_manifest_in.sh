#!/bin/bash

##
## Lists the files to include in sdist distribution. This can be used to
## generate the MANIFEST.in contents:
##
##     tools/generate_manifest_in.sh > MANIFEST.in
##

echo "include README.md"
echo "include README.rst"

echo

find pyguetzli -name "*.[hc]*" -exec echo "include" "{}" ";" \
    | grep -v ".*\.pyc$"

echo

find guetzli -type f -exec echo "include" "{}" ";" \
    | grep -v "^include guetzli/\(.git\|obj\|bin\|tests\|tools\|.travis\)" \
    | grep -v "\.\(ya\?ml\|svg\)$" \
    | grep -v "\(BUILD\|WORKSPACE\)$"
