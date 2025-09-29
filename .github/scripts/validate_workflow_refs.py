import os
import yaml
import re
import glob

def validate_workflow_references():
    """Validate that all workflow references exist and have valid syntax."""
    errors = []
    
    # Get all workflow files
    workflow_files = glob.glob(".github/workflows/*.y*ml")
    workflow_names = [os.path.basename(f) for f in workflow_files]
    
    # Check each workflow file
    for workflow_file in workflow_files:
        with open(workflow_file, 'r') as f:
            try:
                workflow = yaml.safe_load(f)
                
                # Check for workflow_call references
                if workflow.get('jobs'):
                    for job_id, job in workflow['jobs'].items():
                        if job.get('uses') and job['uses'].startswith('./'):
                            # Extract the referenced workflow
                            referenced_workflow = job['uses'].split('/')[-1]
                            if referenced_workflow not in workflow_names:
                                errors.append(f"In {workflow_file}, job {job_id} references non-existent workflow {referenced_workflow}")
            except yaml.YAMLError as e:
                errors.append(f"Error parsing {workflow_file}: {e}")
    
    # Report errors
    if errors:
        print("WORKFLOW VALIDATION ERRORS:")
        for error in errors:
            print(f"  - {error}")
        exit(1)
    else:
        print("All workflow references are valid.")

if __name__ == "__main__":
    validate_workflow_references()
