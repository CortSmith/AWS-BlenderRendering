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
  * The name must be unique across all S3 buckets anyone has created.
    * The description should describe its use case, for our case we are using this 
    bucket for storing our blender rendering output images.
  
  * Launch EC2 instance
  * Connect to your instance
  * Install dependencies and software
