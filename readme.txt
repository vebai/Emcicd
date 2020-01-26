The following are the prerequisites for the jenkins CICD machine


Install latest version of the AWS CLI using the following procedure:

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux-mac.html

Install latest linux/Mac pip version with the following command:

sudo pip install awscli --upgrade --user

Install latest docker version.

Configure AWS CLI credentials with : aws configure.

install Install eksctl with the following procedure:

https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html

Verify installation with the following command:

eksctl version: 
This should return: version.Info{BuiltAt:"", GitCommit:"", GitTag:"0.13.0"}

Install kubectl

