function name: dynamodb-lambda-aggregate

layers: aws scipy version 20

Add as trigger to DynamoDB

Role: dynamodb-lambda-role
	policies:
		AmazonDynamoDBFullAccess
		AWSLambdaDynamoDBExecutionRole
		AWSLambdaInvocation-DynamoDB
