#Creating an empty list, populating the list with AWS services using apped/insert, printing the list and its length, removing 2 specific services from the list, printing the list and its length

#Method 1

aws_services_list1 = []

aws_services_list1[::] = ['AWS Lambda', 'EC2', 'Elastic Beanstalk', 'CloudFormation', 'CodeBuild']

print(aws_services_list1)
print(len(aws_services_list1))

aws_services_list1[3::] = []

print(aws_services_list1)
print(len(aws_services_list1))

#Method 2 

aws_services_list2 = []

aws_services_list2.append('AWS Lambda')
aws_services_list2.append('EC2')
aws_services_list2.append('Elastic Beanstalk')
aws_services_list2.append('CloudFormation')
aws_services_list2.append('CodeBuild')


print(aws_services_list2)
print(len(aws_services_list2))

aws_services_list2.remove('CloudFormation')
aws_services_list2.remove('CodeBuild')

print(aws_services_list2)
print(len(aws_services_list2))