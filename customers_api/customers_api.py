from diagrams import Cluster, Diagram
from diagrams.aws.security import Cognito
from diagrams.aws.integration import Appsync
from diagrams.aws.database import DDB
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.engagement import SES
from diagrams.aws.general import User
from diagrams.aws.security import IAMRole
from diagrams.aws.compute import EB
from diagrams.aws.general import Client

with Diagram("customers_api", show=True, direction="LR"):
    client = Client("client")

    with Cluster("aws"):
        iam = IAMRole("iam role")
        ebs = EB("elastic beanstalk")
        ddb = DDB("dynamodb")

    client >> ebs >> ddb

    iam >> ebs
    ddb >> ebs
    ebs >> client
