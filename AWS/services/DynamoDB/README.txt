Table name: sensorData
	Keys: 
		primary: 
			clientID:'S'
		sort:
			timestamp:'N'

	other columns:
		Payload:
			sensor data : "M"

	Triggers:
		dynamodb-lambda-aggregate
	
	Streams:
		both NEW and OLD streams enabled
--------------------------

Table name: summary
	Keys:
		primary:
			clientID: 'S'
		
	other columns:
		env. paramater: 'M'
			count: 'N'
			value: 'S'
		
		prob: 'M'
			value: 'S'

		