# CI/CD Pipeline Automation with Jenkins, Docker and Kubernetes

This project demonstrates an end-to-end CI/CD setup for a small microservices application.

## What is included

- Two FastAPI services: `catalog` and `orders`.
- Dockerfiles and `docker-compose.yml` for local container testing.
- `Jenkinsfile` with build, test, image build, push, and Helm deploy stages.
- GitHub Actions workflow for CI checks.
- Helm chart with Deployment, Service, Ingress, ConfigMap, probes, resource limits, and HPA.

## Run locally

From this folder:

```powershell
docker compose up --build
```

Then check:

- Catalog service: `http://localhost:8001/health`
- Orders service: `http://localhost:8002/health`
- Order flow: `http://localhost:8002/orders`

## Run without Docker

```powershell
cd apps/catalog
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8001
```

Open a second terminal for `apps/orders` and run it on port `8002`.

Ignore this Comment

## GitHub Actions CI/CD

This repository now includes a GitHub Actions workflow that runs on `main` and performs:

- Python compile checks
- Docker image builds for `catalog` and `orders`
- Helm chart rendering
- GHCR image push
- Helm deploy to Kubernetes

To deploy from GitHub Actions, configure these repository secrets:

- `GHCR_USERNAME`
- `GHCR_TOKEN`
- `IMAGE_REGISTRY`
- `KUBE_CONFIG`

## Kubernetes check

Render the chart:

```powershell
helm template demo .\helm\microservices
```

Deploy to a cluster:

```powershell
helm upgrade --install demo .\helm\microservices --namespace demo --create-namespace
kubectl get pods -n demo
kubectl get hpa -n demo
```

## What to verify

- Docker images build for both services.
- `/health` returns `{"status":"ok"}`.
- Helm template renders without errors.
- Deployments include liveness and readiness probes.
- HPA exists for each service.
- Jenkins/GitHub Actions stages show test and deploy gates clearly.

