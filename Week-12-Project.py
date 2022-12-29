#Creating an empty list, populating the list with AWS services using apped/insert, printing the list and its length, removing 2 specific services from the list, printing the list and its length

aws_services_list = []

aws_services_list[::] = ['AWS Lambda', 'EC2', 'Elastic Beanstalk', 'CloudFormation', 'CodeBuild']

print(aws_services_list)
print(len(aws_services_list))

aws_services_list[3::] = []

print(aws_services_list)
print(len(aws_services_list))