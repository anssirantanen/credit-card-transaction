param(
[Parameter(Mandatory=$true)]
[ValidateNotNullOrEmpty()]
[string]$task_name=$(throw "task_name is mandatory, please provide a value.")
)
docker exec spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./spark-tasks/$task_name