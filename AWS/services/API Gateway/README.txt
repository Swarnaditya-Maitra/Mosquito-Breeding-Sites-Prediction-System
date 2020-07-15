API name: Api_Db
type: REST API
Endpoint Type: Regional
Role: Api_Role
	policies: AmazonAPIGatewayPushToCloudWatchLogs
				Api_policy
					service: DynamoDB
					action: Query
					table: ARN of summary table
					

	/
		/summary
			/{id}
				GET
				OPTIONS


GET- Integration Request
	Integration Type: AWS Service
	Action: Query

	Managing Templates: When there are no templates defined (recommended)

	Content-Type: application/json

	{
    "TableName": "summary",
    "Primarykey": "clientID",
    "KeyConditionExpression": "clientID = :v1",
    "ExpressionAttributeValues": {
        ":v1": {
            "S": "$input.params('id')"
        	}
    	}
	}

OPTIONS:
	default values

