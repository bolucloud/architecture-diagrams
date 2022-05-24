from diagrams import Cluster, Diagram
from diagrams.aws.database import DDB
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
