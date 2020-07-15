ThingName: MyIoTTHing

Users: Administrator
	Policies:
		Administrator Access

Policies: My_Iot_policy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:*",
      "Resource": "*"
    }
  ]
}

----------------


Rule Name: testRule
Rule query Statement: 	SELECT * FROM 'envParams'
Actions: Insert a message into DynamoDB Table
		table: sensorData
		ClientID: ${clientID}
		Timestamp: ${timestamp()}
		Write message to column: 'Payload'
		Role: DBRole
			policies: aws-iot-role-dynamoPut_-XXXXXXX

		Error Action:
			Send message data to cloudWatch Logs
			Role: rule_test_role
				policies:aws-iot-role-cloudwatch-logs_XXXXXXX


