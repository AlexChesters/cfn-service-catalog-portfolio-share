from aws_lambda_powertools import Logger
from crhelper import CfnResource
import boto3

from cfn_service_catalog_portfolio_share.utils.sanitise_properties import sanitise_properties

logger = Logger()
cfn_helper = CfnResource()
service_catalog = boto3.client("servicecatalog")

@cfn_helper.create
def create(event, _context):
    logger.info("create")

    sanitised_properties = sanitise_properties(event["ResourceProperties"])
    service_catalog.create_portfolio_share(**sanitised_properties)

@cfn_helper.update
def update(event, _context):
    logger.info("update")

    sanitised_properties = sanitise_properties(event["ResourceProperties"])
    service_catalog.update_portfolio_share(**sanitised_properties)

@cfn_helper.delete
def delete(event, _context):
    logger.info("delete")

    sanitised_properties = sanitise_properties(event["ResourceProperties"])
    service_catalog.delete_portfolio_share(
        PortfolioId=sanitised_properties["PortfolioId"]
    )

@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    cfn_helper(event, context)
