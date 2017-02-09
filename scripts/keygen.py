import os
import sys
import boto
import boto.ec2
import boto.manage.cmdshell

keyname=sys.argv[1]
region=sys.argv[2]
key_dir=sys.argv[3]

conn_region = boto.ec2.connect_to_region(region)

def generate_key(key_name=keyname,
                    key_dir=key_dir,
                    ssh_passwd=None):

      ec2 = conn_region 

      try:
        key = ec2.get_all_key_pairs(keynames=[key_name])[0]
        
      except ec2.ResponseError, e:
        if e.code == 'InvalidKeyPair.NotFound':
            # Create an SSH key 
            key = ec2.create_key_pair(key_name)
      
            #Save key 
            key.save(key_dir)
            print "Success"
        else:
            raise



if __name__ == "__main__": 
    generate_key()
