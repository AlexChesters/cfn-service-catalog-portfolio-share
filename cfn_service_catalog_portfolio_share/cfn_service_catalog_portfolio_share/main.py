from aws_lambda_powertools import Logger
from crhelper import CfnResource
import boto3

logger = Logger()
cfn_helper = CfnResource()
service_catalog = boto3.client("servicecatalog")

@cfn_helper.create
def create(event, _context):
    logger.info("create")

    accept_language = event["ResourceProperties"].get("AcceptLanguage")
    portfolio_id = event["ResourceProperties"].get("PortfolioId")
    account_id = event["ResourceProperties"].get("AccountId")
    organisation_node = event["ResourceProperties"].get("OrganizationNode")
    share_tag_options = event["ResourceProperties"].get("ShareTagOptions", False)
    share_principals = event["ResourceProperties"].get("SharePrincipals", False)

    if accept_language and accept_language not in ["jp", "zh"]:
        raise ValueError(f"AcceptLanguage property {accept_language} not valid. Valid options: jp, zh")

    if not portfolio_id:
        raise ValueError("Property PortfolioId not provided")

    if account_id and organisation_node:
        raise ValueError("Cannot specify both AccountId and OrganizationNode")

    if not account_id and not organisation_node:
        raise ValueError("One of AccountId or OrganizationNode must be specified")

    create_portfolio_share_kwargs = {
        "PortfolioId": portfolio_id,
        "ShareTagOptions": share_tag_options,
        "SharePrincipals": share_principals
    }

    if accept_language:
        create_portfolio_share_kwargs["AcceptLanguage"] = accept_language

    if organisation_node:
        organisation_node_type = organisation_node.get("Type")
        organisation_node_value = organisation_node.get("Value")

        if not organisation_node_type or organisation_node_value:
            raise ValueError("Property OrganizationNode is invalid (must contain a Type and Value)")

        create_portfolio_share_kwargs["OrganizationNode"] = {
            "Type": organisation_node_type,
            "Value": organisation_node_value
        }


    service_catalog.create_portfolio_share(**create_portfolio_share_kwargs)

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
