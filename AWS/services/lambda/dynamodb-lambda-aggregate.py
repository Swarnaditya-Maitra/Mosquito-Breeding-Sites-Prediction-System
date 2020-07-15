import boto3
import numpy as np
import math
from decimal import Decimal
import logging
logging.getLogger().setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('summary')


def getProbability(temperature,turbidity,humidity,detritus):
  mean_te=30
  mean_tu=475.5
  humid_p=0.01*humidity
  det_p=(math.log10(detritus)*1.843+0.5)/45.6535
  xMinusM=np.matrix([temperature-mean_te,turbidity-mean_tu])

  cov_te=pow(3.334,2)
  cov_tu=pow(8.1667,2)

  sigma=np.matrix([[cov_te, 0],[0, cov_tu]])
  sigin=np.linalg.inv(sigma)
  # det=np.linalg.det(sigma)

  return (1*1.8/(1+np.exp(-(-0.5*(xMinusM.dot(sigin).dot(np.transpose(xMinusM))))))).item()*0.5+0.2*humid_p+0.3*det_p


def lambda_handler(event, context):
    logging.info(event)
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            message=record['dynamodb']
            ID=message['NewImage']['Payload']['M']['clientID']['S']
            new_temp=Decimal(message['NewImage']['Payload']['M']['temperature']['N'])
            new_turb=Decimal(message['NewImage']['Payload']['M']['turbidity']['N'])
            new_detritus=Decimal(message['NewImage']['Payload']['M']['detritus']['N'])
            new_humidity=Decimal(message['NewImage']['Payload']['M']['humidity']['N'])
            
            resp=table.get_item(Key={'clientID': ID})
            if 'Item' in resp.keys():
                prev=resp['Item']
                
                if prev['temperature']['count']<=1000:
                    prev['temperature']['value']=str((Decimal(prev['temperature']['value'])*prev['temperature']['count']+new_temp)/(prev['temperature']['count']+1))
                else:
                    prev['temperature']['value']=str(new_temp)
                    prev['temperature']['count']=0
                prev['temperature']['count']=prev['temperature']['count']+1
                
                if prev['humidity']['count']<=1000:
                    prev['humidity']['value']=str((Decimal(prev['humidity']['value'])*prev['humidity']['count']+new_humidity)/(prev['humidity']['count']+1))
                else:
                    prev['humidity']['value']=str(new_humidity)
                    prev['humidity']['count']=0
                prev['humidity']['count']=prev['humidity']['count']+1
                
                
                if prev['turbidity']['count']<=1000:
                    prev['turbidity']['value']=str((Decimal(prev['turbidity']['value'])*prev['turbidity']['count']+new_turb)/(prev['turbidity']['count']+1))
                else:
                    prev['turbidity']['value']=str(new_turb)
                    prev['turbidity']['count']=0
                prev['turbidity']['count']=prev['turbidity']['count']+1
                
                
                if prev['detritus']['count']<=1000:
                    prev['detritus']['value']=str((Decimal(prev['detritus']['value'])*prev['detritus']['count']+new_detritus)/(prev['detritus']['count']+1))
                else:
                    prev['detritus']['value']=str(new_detritus)
                    prev['detritus']['count']=0
                prev['detritus']['count']=prev['detritus']['count']+1
                
                
                prev['prob']=str(
                    getProbability(
                        float(prev['temperature']['value']),
                        float(prev['turbidity']['value']),
                        float(prev['humidity']['value']),
                        float(prev['detritus']['value'])
                        )
                        )
                item=prev
            else:
                prob=str(getProbability(float(new_temp),float(new_turb),float(new_humidity),float(new_detritus)))
                item={
                    'clientID': ID,
                    'temperature':{
                        'value': str(new_temp),
                            'count':1
                    },
                    'humidity':{
                        'value':str(new_humidity),
                            'count':1
                    },
                    'turbidity':{
                        'value':str(new_turb),
                            'count':1
                    },
                    'detritus':{
                        'value':str(new_detritus),
                            'count':1
                    },
                    'prob': prob
                }
                
            response=table.put_item(Item=item)
            logging.info(response)
            