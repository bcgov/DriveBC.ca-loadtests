#!/bin/sh

locust --worker -f $TEST_FILE --master-host locust.c59ecc-dev.svc.cluster.local
