#!/bin/sh

locust --worker -f $TEST_FILE --master-host $MASTER_HOST
