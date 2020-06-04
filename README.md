# AWS-BlenderRendering

## Steps to begin rendering images with blender on AWS EC2

### Step 1 -- Create an S3 Bucket for Blender output files
  * Setup S3 storage
    * Click the Services dropdown at the top left of the website.
    * Navigate to the search bar and enter "S3".
    ![](./source-md/S3-1-SearchS3.png)
    * Click the Create Bucket button.
    ![](./source-md/S3-2-CreateBucket.png)
    * Give it a name; must be unique among all buckets on the internet.
    * Select the region you will be running your ec2 instance from.
    ![](./source-md/S3-3-SetNameAndRegion.png)
    * Skip the next two sections. 
        Those are additional options for more control over bucket access, and
        versioning.
    ![](./source-md/S3-4-SetVersioningAndLogging.png)
    ![](./source-md/S3-5-SetAccessLevels.png)
    * Look over the settings of your bucket and click Create
    ![](./source-md/S3-6-CreateBucket.png)
    * Take note of your S3 bucket name, you will need it if you want access to it from the aws cli on 
    your own computer or ec2 instance.
    * The description should describe its use case, for our case we are using this 
    bucket for storing our blender rendering output images.
  * This is what your bucket should look like:
  ![](./source-md/S3-7-bucketList.png)
  ![](./source-md/S3-8-insideBucket.png)
    
### Step 2 -- Create an IAM Role and Security Group
  * Search IAM under the Services tab.
  
  * Find and select the Roles section. It should be located on the initial page.
  ![](./source-md/IAM-1-SelectRoles.png)
  
  * Select Create Role, to create a new role for our ec2 instance.
  ![](./source-md/IAM-2-SelectCreateRole.png)
  
  * Select the EC2 use case.
  ![](./source-md/IAM-3-SelectIAMUseCase.png)
  
  * Now to add our permissions, search S3 and choose 'AmazonS3FullAccess'.
    * Ideally we would select specific functions that our ec2 instance would require, however, 
    for this tutorial we will simply use full access.
    ![](./source-md/IAM-4-SearchAndSelectS3Access.png)
  
  * Enter the name and description and click create.
  ![](./source-md/IAM-5-SetNameAndDescriptionCreate.png)
  
  * This is what you should see after you create the role:
  ![](./source-md/IAM-6-RoleCreated.png)
  
### Step 3 [Optional] -- Setup an EC2 instance volume.
* Volumes are storage blocks that allow you to save your files without having to re-download files, 
software, and other dependencies.
* Navigate to the EC2 service page by searching EC2 under the Services tab.
### Creating your key-pair for SSH
### Launch your EC2 instance
### Connect to your instance
### Install dependencies
### Expenses

