import wandb

# Start a new run
wandb.init(
    project="test_project",  # Replace with your project name
)

# Log a simple metric
wandb.log({"test_metric": 1})

# Finish the run
wandb.finish()
