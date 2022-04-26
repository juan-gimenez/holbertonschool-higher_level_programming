#!/bin/bash
# send get request w a header value
curl -s "$1" GET -L -H "X-School-User-Id:98"
