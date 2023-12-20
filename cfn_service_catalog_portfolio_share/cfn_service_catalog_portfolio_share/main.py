from aws_lambda_powertools import Logger
from crhelper import CfnResource

logger = Logger()

cfn_helper = CfnResource()

@cfn_helper.create
def create(event, _context):
    logger.info("create")
    portfolio_id = event["ResourceProperties"].get("PortfolioId")

    if not portfolio_id:
        raise ValueError("Property PortfolioId not provided")

@cfn_helper.update
def update(event, _context):
    logger.info("update")

    portfolio_id = event["ResourceProperties"].get("PortfolioId")

    if not portfolio_id:
        raise ValueError("Property PortfolioId not provided")

@cfn_helper.delete
def delete(event, _context):
    logger.info("delete")

    portfolio_id = event["ResourceProperties"].get("PortfolioId")

    if not portfolio_id:
        raise ValueError("Property PortfolioId not provided")

@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    cfn_helper(event, context)
