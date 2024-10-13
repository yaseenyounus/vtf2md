variable "vpc_cidr_block" {
  type = string
  description = "The top-level CIDR block for the VPC."
  default     = "10.1.0.0/16"
}

variable "cidr_blocks" {
  type = list(string)
  description = "The CIDR blocks to create the workstations in."
  default     = ["10.1.1.0/24", "10.1.2.0/24"]
}

variable "namespace" {
  type = string
  description = "Default namespace"
}

variable "cluster_id" {
  type = string
  description = "Id to assign the new cluster"
}

variable "public_key_path" {
  type = string
  description = "Path to public key for ssh access"
  default     = "~/.ssh/id_rsa.pub"
}

variable "node_groups" {
  type = number
  description = "Number of nodes groups to create in the cluster"
  default     = 3
}