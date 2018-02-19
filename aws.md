1. The default settings for MySQL instances on RDS is stupid. Create a parameter group with (significantly) longer timeouts.
1. Django-South does not work on RDS.
1. Copying a file across S3 buckets is just copying its key -- S3 is one uniform storage resource. Having a key that points to a file in both buckets means that, effectively, the file exists in both buckets.
1. [`htop` missing](http://aws.blandnet.org/wordpress/htop-install/)
1. [Upgrading an instance](http://stackoverflow.com/a/8243307/1558430): stop the instance, wait for a while, and select "Change Instance Type"
1. VPC is Virtual Private Cloud, not Virtual PC.
1. If you can't move an RDS server's region, at least move the EC2 instances' availabiltiy zones to match it.
1. `/etc/httpd/conf/httpd.conf` has a load of stuff you can disable.
1. `/etc/httpd/conf.d/wsgi.conf` also has a load of stuff you can tweak.
1. Get everything from an s3 bucket: `s3cmd get s3://(bucket name)/*`
1. EC2 will wipe out all of your `authorized_keys` in newly-spawned instances unless the instance was created with the "no reboot" option checked.
1. You can restore a Postgres snapshot with a different name while the current one is being deleted, then rename the new database to the old name to replace it with no downtime.
1. From within an instance, get its hostname: [`curl http://169.254.169.254/latest/meta-data/public-hostname`](http://serverfault.com/questions/403440/print-external-host-name-of-ec2-instance)
1. [Blue-green deployment](http://martinfowler.com/bliki/BlueGreenDeployment.html) involves spinning up a new version of the application, waiting for deployment to complete and its state verified, then replacing green (current) instances in the load balancer with the ones you just spun up (blue).
1. Load balancers send your requests to different servers (perhaps evenly, perhaps not). Auto scaling groups tell the thingy how many servers you want to have. Launch configurations tell the bois how big you want each server to be.
1. Sections in the `~/.aws/config` file, apart from `[default]`, [need to be prefixed with `profile `](http://boto3.readthedocs.io/en/latest/guide/configuration.html#aws-config-file), i.e. `[profile whatever]`. However, sections in the `~/.aws/credentials` file [must not be prefixed with `profile `](http://boto3.readthedocs.io/en/latest/guide/configuration.html#shared-credentials-file), so only `[whatever]` will work.
1. You make an instance so you can make an AMI with it.
1. You make an AMI so you can specify one in a Launch Configuration (LC).
1. You make a Launch Configurations because Auto Scaling Groups (ASGs) need one to know what to launch and scale up/down.
1. You make an ASG so you can have multiple instances of the same AMI doing the same thing.
1. You can "View/edit rules" for each load balancer (under Listeners) to configure which requests get sent to which Target Group, depending on headers or request path. For some reason you need at least one Target Group (TG) for your Application Load Balancer (ALB) because I don't know.
1. You make a load balancer because otherwise only one instance in your ASG will get requests. Also, you can only attach a Route53 record set to a load balancer or directly to an instance, so you do that. After that, maybe you can have a working website. All these are bound by Security Groups (SGs), which are just firewall rules.
1. Amazon Aurora is "one-tenth the cost" of enterprise databases, not one-tenth the cost of their other offerings.
