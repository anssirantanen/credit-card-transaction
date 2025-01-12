param(
[string]$task_name
)
docker exec spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./spark-tasks/$task_name