resource "aws_s3_bucket" "plutotf003" {
  bucket = "plutotf003"
  acl    = "private"
  versioning {
    enabled = false
  }

  tags = {
    Name = "plutotf003"
  }


}

