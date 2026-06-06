pipeline {
  agent any

  environment {
    REGISTRY = "ghcr.io/your-org/devops-microservices"
    IMAGE_TAG = "${env.BUILD_NUMBER}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Unit Smoke Tests') {
      steps {
        bat 'python -m compileall apps'
      }
    }

    stage('Build Images') {
      steps {
        bat 'docker build -t %REGISTRY%/catalog:%IMAGE_TAG% apps/catalog'
        bat 'docker build -t %REGISTRY%/orders:%IMAGE_TAG% apps/orders'
      }
    }

    stage('Push Images') {
      when {
        branch 'main'
      }
      steps {
        bat 'docker push %REGISTRY%/catalog:%IMAGE_TAG%'
        bat 'docker push %REGISTRY%/orders:%IMAGE_TAG%'
      }
    }

    stage('Deploy with Helm') {
      when {
        branch 'main'
      }
      steps {
        bat 'helm upgrade --install demo helm/microservices --namespace demo --create-namespace --set image.tag=%IMAGE_TAG%'
      }
    }
  }
}

