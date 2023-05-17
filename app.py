#!/usr/bin/env python3
import os

import aws_cdk as cdk

import constants
from sample_environment.sample_environment_stack import SampleEnvironmentStack

app = cdk.App()
env_name=os.environ["ENV_NAME"]
sample_environment_stack = SampleEnvironmentStack(app, f"sample-environmnet-{env_name}", vpc_cidr=os.environ["VPC_CIDR"], env_name=env_name, ecs_image=constants.ECS_IMAGE)

app.synth()
