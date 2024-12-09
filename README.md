# Fullstack Monitoring

This project provides a full-stack monitoring solution, integrating various tools such as Prometheus, Loki, Traefik, and Terraform for infrastructure management. The goal of the project is to set up a reliable monitoring and logging system with support for easy deployment and configuration.

## Project Structure

The project directory structure is organized as follows:

```
.
├── db.compose.yaml                # Database related Docker Compose configuration
├── docker-compose.yaml            # Main Docker Compose configuration for services
├── .env                            # Environment configuration file
├── .git/                           # Git repository directory
├── .gitignore                      # Git ignore file
├── letsencrypt/                    # SSL certificates and ACME configuration
│   ├── acme-production.json        # Production SSL certificate configuration
│   └── acme-staging.json           # Staging SSL certificate configuration
├── monitoring/                     # Monitoring system configurations
│   ├── loki-config.yaml            # Loki configuration for log aggregation
│   ├── prometheus-config.yaml      # Prometheus configuration for metrics collection
│   └── promtail-config.yaml        # Promtail configuration for log forwarding
├── monitoring.compose.yaml         # Docker Compose configuration for monitoring services
├── README.md                       # Project overview and documentation
├── reverse-proxy/                  # Reverse proxy configuration using Traefik
│   └── traefik.yaml                # Traefik configuration
├── .sample.env                     # Sample environment configuration
├── terraform/                      # Infrastructure as Code (IaC) using Terraform
│   ├── ec2.tf                      # EC2 instance setup
│   ├── main.tf                     # Main Terraform configuration
│   ├── scripts/
│   │   └── user_data.sh            # User data script for EC2 instance
│   ├── security-group-rules.tf     # Security group rules configuration
│   ├── security-group.tf           # Security group setup
│   ├── subnets.tf                  # Subnets configuration
│   ├── terraform.tfstate           # Terraform state file
│   └── terraform.tfstate.backup    # Terraform state backup
├── todo-api/                       # Backend API service (FastAPI)
│   ├── (backend files)             # FastAPI project files and configurations
│   └── todo-api-logs.log           # Logs for the todo-api service
├── todo-frontend/                  # Frontend application (React/Other)
│   ├── (frontend files)            # Frontend code and configurations
└── traefik.compose.yaml            # Docker Compose for Traefik reverse proxy
```

### Key Components

- **Docker Compose**: Used for orchestrating the containerized services. The main `docker-compose.yaml` file defines the services, while additional Compose files are used for monitoring (`monitoring.compose.yaml`) and Traefik (`traefik.compose.yaml`).
- **Monitoring**: Configurations for Prometheus, Loki, and Promtail are located in the `monitoring/` folder. These tools are used for collecting and visualizing metrics and logs.

- **Reverse Proxy**: Traefik is configured in the `reverse-proxy/` folder, which manages incoming traffic to the services using automatic routing and SSL certificates.

- **Terraform**: Infrastructure as Code (IaC) files for provisioning AWS EC2 instances and related resources like security groups and subnets. This is defined in the `terraform/` directory.

- **Backend (FastAPI)**: The backend API service is located in the `todo-api/` directory. It is built with FastAPI and provides the API for managing todo items.

- **Frontend (React/Other)**: The frontend service is located in the `todo-frontend/` directory. It provides the user interface for interacting with the backend API.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- [Git](https://git-scm.com/)
- [Node.js & npm](https://nodejs.org/) (for frontend)

## Setup

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/fullstack-monitoring.git
cd fullstack-monitoring
```

### 2. Configure Environment Variables

Copy the `.sample.env` file to `.env`:

```bash
cp .sample.env .env
```

Edit the `.env` file and configure the necessary environment variables based on your setup.

### 3. Docker Compose Setup

To start all the services using Docker Compose, run the following command:

```bash
docker-compose up -d
```

This will bring up the following services:

- Backend (FastAPI) application
- Frontend application
- Traefik reverse proxy
- Monitoring stack (Prometheus, Grafana, Loki, Promtail)

You can check the logs to ensure that everything is running correctly:

```bash
docker-compose logs -f
```

### 4. Terraform Setup

To deploy infrastructure using Terraform, follow these steps:

1. Initialize Terraform:

   ```bash
   terraform init
   ```

2. Apply the Terraform configuration to provision resources:

   ```bash
   terraform apply
   ```

   Follow the prompts to confirm the changes.

### 5. Accessing the Services

- **Frontend**: Access the frontend application via your browser at `http://localhost:3000` (or the appropriate port configured in your `.env` or Docker Compose files).
- **Backend**: Access the FastAPI backend at `http://localhost:8000` (or the appropriate port).

- **Traefik Dashboard**: If Traefik is configured to expose a dashboard, you can access it at `http://localhost:8080` (or the configured port).

### 6. Monitoring

- **Prometheus**: Access Prometheus at `http://localhost:9090` for querying metrics.
- **Grafana**: If you have Grafana set up in your `monitoring/` setup, you can access it at `http://localhost:3001` (or the configured port).

## Troubleshooting

- If you encounter issues with Docker Compose, check the container logs:

  ```bash
  docker-compose logs <service_name>
  ```

- Ensure that all services are running:

  ```bash
  docker ps
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Prometheus](https://prometheus.io/) for metrics collection
- [Loki](https://grafana.com/oss/loki/) for log aggregation
- [Traefik](https://traefik.io/) for reverse proxy management
- [FastAPI](https://fastapi.tiangolo.com/) for the backend API
- [Terraform](https://www.terraform.io/) for infrastructure provisioning
