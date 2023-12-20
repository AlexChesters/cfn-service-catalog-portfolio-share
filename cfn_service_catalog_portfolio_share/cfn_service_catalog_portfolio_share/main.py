from aws_lambda_powertools import Logger, Tracer
from crhelper import CfnResource

logger = Logger()
tracer = Tracer()

cfn_helper = CfnResource()

@cfn_helper.create
def create(_event, _context):
    logger.info("create")

@cfn_helper.update
def update(_event, _context):
    logger.info("update")

@cfn_helper.delete
def delete(_event, _context):
    logger.info("delete")

@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    cfn_helper(event, context)
