module "ec2_instance" {
  source                      = "/media/davidshare/Tersu/TersuCorp/tersu tech/learning DevOps/terraform-aws-modules/ec2"
  ami                         = "ami-0453ec754f44f9a4a"
  instance_type               = "t2.micro"
  key_name                    = "monitoring"
  subnet_id                   = module.subnets.id
  vpc_security_group_ids      = [module.security_group.id]
  associate_public_ip_address = true
  user_data                   = file("./scripts/user_data.sh")

  tags = {
    Name = "monitoring instance"
  }
}