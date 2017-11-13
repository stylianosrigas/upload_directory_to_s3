import boto3
import os
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def uploadDirectory(path,bucketname):
	
	for root,dirs,files in os.walk(path):
		if files:   #Checks if directory not empty
			for file in files:    #Iterates through the file of the directory
				print '### Uploading file - %s ###' %os.path.join(root,file)
				if root.split(path)[1]:
					key = root.split(path)[1] + '/' + file
				else:
					key = file #This check helps to avoid creating an empty directory for files in the root dir
				try:
					s3_client.upload_file(os.path.join(root,file),bucketname,key)
				except ClientError as e:
					print e

uploadDirectory('/Users/stylianosrigas/Repos/github/upload_directory_to_s3/', 'stelios-test-bucket')

