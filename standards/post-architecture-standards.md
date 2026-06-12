# POST Platform Architecture Standards

## Platform Strategy

Approved Technologies:

* GitHub Actions
* GitHub Reusable Workflows
* GitOps Deployment Model
* ArgoCD
* Google Kubernetes Engine (GKE)
* Google Artifact Registry (GAR)
* Java 17
* Workload Identity Federation

Do not flag approved platform choices as risks.

---

## Reusable Actions

Production:

* Reusable actions must use version tags (e.g. @v1).

Lab / Prototype:

* @develop references are permitted.

---

## Security Standards

Required:

* SBOM generation
* Container image scanning
* Dependency scanning
* No static cloud credentials
* Workload Identity Federation preferred

---

## GitOps Standards

Required:

* Deployments must occur through GitOps repositories.
* Direct cluster deployments are not permitted.
* ArgoCD is the approved deployment controller.

---

## Reliability Standards

Required:

* Deployment observability
* Rollback strategy
* Versioned reusable actions for production workloads

---

## Review Guidance

Focus on:

* Architecture concerns
* Security concerns
* Reliability concerns
* Scalability concerns

Ignore:

* Code formatting
* Naming conventions
* Minor style issues

Lab Context:

This repository is currently operating in a lab/prototype environment. Experimental patterns are acceptable if clearly identified and documented.
Review the PR.

Identify findings.

For each finding provide:

- severity
- category
- issue
- recommendation

After identifying findings:

Calculate overall risk score.

The risk score must be justified by the findings.

If no findings exist:

Risk score must be 0 or 1.
State explicitly why.
