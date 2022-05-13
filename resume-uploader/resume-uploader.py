from diagrams import Cluster, Diagram
from diagrams.aws.security import Cognito
from diagrams.aws.integration import Appsync
from diagrams.aws.database import DDB
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.engagement import SES
from diagrams.aws.general import User

with Diagram("resume_uploader", show=True):
    user = User("user")

    with Cluster("amplify"):
        amplify_group1 = Cognito("authentication") >> Appsync("appsync") >> DDB(
            "dynamodb")
        amplify_group_2 = Lambda("function")
        amplify_group_3 = S3("storage")

    ses = SES("email")
    user >> amplify_group1 >> amplify_group_2 >> amplify_group_3
    amplify_group_2 >> ses
