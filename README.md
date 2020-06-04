# AWS-BlenderRendering

Learn how to programmatically render thousands of images using 
Amazon Web Services, Blender, and Python.

---

###Step 1 - Create an S3 Bucket for Blender output files

- Setup S3 storage
    
    - Click the Services dropdown at the top left of the website.
    
    - Navigate to the search bar and enter "S3".
    
    - Click the Create Bucket button.
    
    - Give it a name; must be unique among all buckets on the internet.
    
    - Select the region you will be running your ec2 instance from.
    
    - Skip the next two sections. 
        Those are additional options for more control over bucket access, and
        versioning.
    
    - Look over the settings of your bucket and click Create
    
    - Take note of your S3 bucket name, you will need it if you want access to it from the aws cli on 
    your own computer or ec2 instance.
    
    - This is what your bucket should look like:
    
---

###Step 2 - Create an IAM Role and Security Group

  - Search IAM under the Services tab.
  
  - Find and select the Roles section. It should be located on the initial page.
  
  - Select Create Role, to create a new role for our ec2 instance.
  
  - Select the EC2 use case.
  
  - Now to add our permissions, search S3 and choose 'AmazonS3FullAccess'.
    
    - Ideally we would select specific functions that our ec2 instance would require, however, 
    for this tutorial we will simply use full access.
  
  - Enter the name and description and click create.
  
  - The description should describe its use case, for our case we are using this 
    bucket for storing our blender rendering output images.
  
  - This is what you should see after you create the role:

---

###Step 3 [Optional] - Setup an EC2 instance volume.

- Volumes are storage blocks that allow you to save your files without having to re-download files, 
software, and other dependencies.

- Navigate to the EC2 service page by searching EC2 under the Services tab.

---

###Creating your key-pair for SSH

Key-pairs are used to connect to aws via ssh encryption, to keep your connection secure. Keys are also required in order to connect to your ec2 instance.

- Search EC2 in the Services tab search bar and navigate to the EC2 dashboard.

- On the left-hand side column there is a list of services for ec2. \
Under Network & Security, find and select Security Groups.

- On the top right of the page, click the Create Security Group button.

- Enter a name and description.

- For simplicities sake, we will adding only one rule for All Traffic.

- Under Inbound Rules and Outbound Rules, click Add Rule.

    - Change the Type to All Traffic.
    
    - Change Source to My IP
    
    - Do the same under Outbound Rules

---

### Launch your EC2 instance

---

### Connect to your instance

---

### Install dependencies

---

### Expenses

