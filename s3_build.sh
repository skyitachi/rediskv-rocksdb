#!/bin/sh

# because mac has BSD version sed for compatibility we use awk here
COMMIT=$(git rev-parse HEAD)
replace="{gsub(\"HEAD\", \"$COMMIT\", \$0); print \$0}"
cat s3.spec | awk "$replace" > _s3.spec
ERU=10.22.12.87:5001 eru-cli image build --tag 1.9.31 --name aws-sdk-cpp _s3.spec
rm _s3.spec
