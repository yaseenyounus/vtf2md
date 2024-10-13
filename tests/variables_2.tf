variable "project_name" {
  type        = string
  description = "Name of the project"
  default     = "my-awesome-project"
}

variable "environment" {
  type        = string
  description = "Deployment environment (e.g. dev, staging, prod)"
  default     = "dev"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "CIDR blocks for public subnets"
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "CIDR blocks for private subnets"
  default     = ["10.0.10.0/24", "10.0.20.0/24"]
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "instance_count" {
  type        = number
  description = "Number of EC2 instances to launch"
  default     = 2
}

variable "db_engine" {
  type        = string
  description = "Database engine type"
  default     = "mysql"
}

variable "db_instance_class" {
  type        = string
  description = "Database instance class"
  default     = "db.t3.micro"
}

variable "db_settings" {
  type = map(string)
  description = "Database settings"
  default = {
    "engine_version" = "5.7"
    "storage_type"   = "gp2"
    "storage_size"   = "20"
  }
}

variable "tags" {
  type = object({
    environment = string
    project     = string
    owner       = string
  })
  description = "Resource tags"
  default = {
    environment = "dev"
    project     = "my-project"
    owner       = "devops-team"
  }
}

variable "db_password" {
  type        = string
  description = "Database password"
  sensitive   = true
}
