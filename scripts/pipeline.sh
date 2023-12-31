set -e

aws cloudformation deploy \
  --template-file ci/codepipeline.yml \
  --stack-name codepipeline-cfn-service-catalog-portfolio-share \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --region eu-west-1 \
  --profile service-catalog

aws cloudformation deploy \
  --template-file ci/codepipeline.yml \
  --stack-name codepipeline-cfn-service-catalog-portfolio-share \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --region us-east-1 \
  --profile service-catalog
