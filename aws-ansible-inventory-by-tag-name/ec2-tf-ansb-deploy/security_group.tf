#Create SG for allowing TCP/22 from your IP in us-east-1
resource "aws_security_group" "plutoTFsg-ssh" {

  name        = "plutoTFsg-ssh"
  description = "Allow TCP/8080 & TCP/22"
  vpc_id      = aws_vpc.plutoTFvpc.id
  ingress {
    description = "Allow 22 from our public IP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "plutoTFsg-ssh"
  }
}

resource "aws_security_group" "plutoTFsg-egress" {
  name        = "plutoTFsg-egress"
  description = "secgrp-egress"
  vpc_id      = aws_vpc.plutoTFvpc.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "plutoTFsg-egress"
  }
}

