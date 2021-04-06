#Create key-pair for logging into EC2 in us-east-1
resource "aws_key_pair" "plutoTFkey" {
  key_name   = "plutoTFkey"
  public_key = file("~/.ssh/plutoTFkey.pub")
}



resource "aws_instance" "plutoAlpha-p" {
  ami                    = "ami-0533f2ba8a1995cf9"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.plutoTFsg-egress.id]
  subnet_id              = aws_subnet.plutoTFSB_2p.id
  key_name               = "plutoec2key"
  root_block_device {
    volume_type = "gp2"
    volume_size = "8"
  }

  tags = {
    Name   = "plutoAlpha-p"
    Owner  = "hz"
    Type   = "dev",
    Desc   = "test Instance"
    Group  = "alpha"
    Public = "no"
  }

}

resource "aws_instance" "plutoBravo-p" {
  ami                    = "ami-0533f2ba8a1995cf9"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.plutoTFsg-egress.id]
  subnet_id              = aws_subnet.plutoTFSB_2p.id
  key_name               = "plutoec2key"
  root_block_device {
    volume_type = "gp2"
    volume_size = "8"
  }

  tags = {
    Name   = "plutoBravo-p"
    Owner  = "hz"
    Type   = "dev",
    Desc   = "test Instance"
    Group  = "bravo"
    Public = "no"
  }
}

resource "aws_instance" "plutoAlpha-w" {
  ami           = "ami-0533f2ba8a1995cf9"
  instance_type = "t2.micro"

  vpc_security_group_ids = [
    aws_security_group.plutoTFsg-ssh.id
  ]

  subnet_id = aws_subnet.plutoTFSB_1w.id
  key_name  = "plutoec2key"

  root_block_device {
    volume_type = "gp2"
    volume_size = "8"
  }

  tags = {
    Name   = "plutoAlpha-w"
    Owner  = "hz"
    Type   = "dev",
    Desc   = "test Instance"
    Group  = "alpha"
    Public = "yes"
  }
}

resource "aws_instance" "plutoBravo-w" {
  ami                    = "ami-0533f2ba8a1995cf9"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.plutoTFsg-ssh.id]
  subnet_id              = aws_subnet.plutoTFSB_1w.id
  #key_name               = aws_key_pair.plutoTFkey.key_name
  key_name = "plutoec2key"
  root_block_device {
    volume_type = "gp2"
    volume_size = "8"
  }

  tags = {
    Name   = "plutoBravo-w"
    Owner  = "hz"
    Type   = "dev",
    Desc   = "test Instance"
    Group  = "bravo"
    Public = "yes"
  }
}

