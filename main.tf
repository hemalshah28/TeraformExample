terraform {
    required_providers {
        docker = {
        source  = "hashicorp/docker"
        version = "3.0.2"  
        }
    }
}

provider "docker" {
    host = "tcp://localhost:2375/"
}