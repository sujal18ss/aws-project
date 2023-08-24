# aws-project
LW project

Step-1. Create aws Ec2 for base OS
Step-2. In Ec2 run this commands yum install -y httpd docker 
        yum start httpd yum enable httpd
        yum start docker yum enable docker
Step-3. Download aws cli for aws services
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
        unzip awscliv2.zip
        sudo ./aws/install  (for checking installed or not "aws --version")
Step-4. Install python & pip & boto3 
        yum install -y python3 (install python version 3)
        curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
        sudo python get-pip.py (install pip library )
        pip install boto3 (install boto3)
Step-4. Copy this files in html folder inside /var/www/html/ folder
        cp aws.svg docker.svg linux.svg backend.js index.html style.css styles.css /var/www/html/
Step-5. Copy this files in cgi-bin folder inside /var/www/cgi-bin/ folder
        cp create.py del.py run.py /var/www/cgi-bin
        chmod +x create.py del.py run.py (make these executable)
Step-6. visudo
        apache ALL=(ALL) NOPASSWD:ALL (add this 
        apache ALL=(ALL) NOPASSWD:ALL (add this commnds in 'vidsudo' file)
Step-7. Now you can access your website through your ec2 public IP address , for this you have to replace it to your IP in backend.js file





        
