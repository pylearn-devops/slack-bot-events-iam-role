import boto3
from tabulate import tabulate

client = boto3.client('cloudformation')

# Define your stack name and S3 template URL
stack_name = 'ab-iam-role-stack'
template_body = open('cloudformation.yml').read()

# Create the stack
response = client.create_stack(
    StackName=stack_name,
    TemplateBody=template_body,
    Capabilities=[
        'CAPABILITY_NAMED_IAM',
    ]
)

# Extract information about the resources being created
stack_id = response['StackId']
stack_description = client.describe_stacks(StackName=stack_name)['Stacks'][0]
resources = []
for resource in stack_description['Resources']:
    resources.append([resource['LogicalResourceId'], resource['ResourceType'], resource.get('ResourceStatus', '-')])

# Print the table output
print("Resources being created:")
print(tabulate(resources, headers=['Logical ID', 'Resource Type', 'Status'], tablefmt='grid'))

# Wait for the stack creation to complete if needed
waiter = client.get_waiter('stack_create_complete')
waiter.wait(StackName=stack_name)

print("Stack created successfully.")
