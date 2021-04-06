#Create VPC in us-east-1

resource "aws_vpc" "plutoTFvpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "plutoTFvpc"
  }

}


#Get all available AZ's in VPC for us-east-1
data "aws_availability_zones" "pluto-azs" {
  state = "available"
}


#Create IGW in us-east-1
resource "aws_internet_gateway" "plutoTFigw" {
  vpc_id = aws_vpc.plutoTFvpc.id
  tags = {
    Name = "plutoTFigw"
  }

}

#Create subnet # 1, pulbic in us-east-1
resource "aws_subnet" "plutoTFSB_1w" {
  availability_zone       = element(data.aws_availability_zones.pluto-azs.names, 0)
  vpc_id                  = aws_vpc.plutoTFvpc.id
  map_public_ip_on_launch = "true"
  cidr_block              = "10.0.1.0/24"
  tags = {
    Name = "plutoTFSB_1w"
    Type = "public"
  }
}

#Create subnet # 2, private in us-east-1
resource "aws_subnet" "plutoTFSB_2p" {
  availability_zone       = element(data.aws_availability_zones.pluto-azs.names, 1)
  vpc_id                  = aws_vpc.plutoTFvpc.id
  map_public_ip_on_launch = "false"
  cidr_block              = "10.0.2.0/24"
  tags = {
    Name = "plutoTFSB_2p"
    Type = "private"
  }
}



#Create routing table in us-east-1
resource "aws_route_table" "plutoTF_route_1w" {
  vpc_id = aws_vpc.plutoTFvpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.plutoTFigw.id
  }
  tags = {
    Name = "PlutoTFPubicRT"
  }
}

#Overwrite default route table of VPC  with our route table entries
resource "aws_route_table_association" "plutoTF-rt-w" {
  subnet_id      = aws_subnet.plutoTFSB_1w.id
  route_table_id = aws_route_table.plutoTF_route_1w.id
}
