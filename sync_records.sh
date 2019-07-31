#!/bin/bash
BUCKET=apollo-usage-logs
aws s3 sync s3://$BUCKET report-logs
