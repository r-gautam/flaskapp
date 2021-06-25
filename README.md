# Deploy sample flask app to GKE cluster

### Prerequisite
K8 cluster integrated with gitlab project<br>
Follow this link to link existing cluster 
https://docs.gitlab.com/ee/user/project/clusters/add_existing_cluster.html 
or create new one Via GUI<br>

### Update the imagepath in deployment.yaml file<br>
Pull image from a private repo? Create secrets and update deployment.yaml accordingly.

### Trigger the pipeline and flaskapp will be deployed to GKE cluster in Dev environmnet<br>
Change environment? Update label environment in deploy stage inside .gitlab-ci.yaml file