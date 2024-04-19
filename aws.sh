#!/bin/bash

aws cloudformation create-stack --stack-name ab-iam-role-stack --capabilities CAPABILITY_NAMED_IAM --template-body file://cloudformation.yml --region us-east-1 --profile dev

aws cloudformation wait stack-create-complete --stack-name ab-iam-role-stack --region us-east-1 --profile dev
