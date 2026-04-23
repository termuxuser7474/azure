# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.


For deploying the CMS application, both Virtual Machines (VMs) and Azure App Service are possible options, but they differ in cost, scalability, availability, and workflow.

In terms of cost, App Service is usually cheaper for web applications because Azure manages the infrastructure and maintenance. With VMs, we have to maintain the server, install updates, and monitor the system, which can increase both time and cost.

Regarding scalability, App Service provides built-in scaling features, so the application can handle increased traffic automatically. In contrast, scaling with VMs requires manually creating or configuring additional machines.

For availability, App Service offers high availability by default since Azure manages the platform. With VMs, availability has to be configured manually using availability sets or other configurations.

Looking at the workflow, App Service makes deployment easier because it supports quick deployment and integrates well with CI/CD pipelines. Using VMs requires setting up the server environment, installing dependencies, and managing deployments manually.

Considering these factors, Azure App Service is the better choice for deploying this CMS app because it reduces management effort and allows faster and simpler deployment.

### Assess app changes that would change your decision.

The decision could change if the application required more control over the server environment or operating system. For example, if the CMS needed special software installations, custom configurations, or multiple services running on the same server, a Virtual Machine might be more suitable.

In such cases, the flexibility of VMs would be useful because they allow full control over the infrastructure. However, for a typical web CMS application, App Service is still the simpler and more efficient option.