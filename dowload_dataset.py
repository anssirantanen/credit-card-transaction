import requests
import csv
import shutil

trainin_dataset_url = "https://huggingface.co/datasets/pointe77/credit-card-transaction/resolve/main/credit_card_transaction_train.csv"
testing_dataset_url = "https://huggingface.co/datasets/pointe77/credit-card-transaction/resolve/main/credit_card_transaction_test.csv"

staging_folder = "./datalake/staging/"
local_training_name =staging_folder+ "credit_card_transaction_train.csv"
local_testing_name = staging_folder+"credit_card_transaction_test.csv"
credict_card_transaction = staging_folder+"credit_card_transaction.csv"

def dowload_large_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                
dowload_large_file(trainin_dataset_url, local_training_name)
dowload_large_file(testing_dataset_url, local_testing_name)

shutil.copy(local_training_name, credict_card_transaction)

with open(credict_card_transaction) as target, open(local_testing_name, 'w') as output:
    reader = csv.reader(target)
    writer = csv.writer(output)
    next(reader,None)
    for row in reader:
        writer.writerow(row)
