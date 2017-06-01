import sys
import json

from eval import eval_dag

if __name__ == '__main__':
    dag_str = sys.argv[1]
    dag_json = dag_str.replace("\'", "\"")

    dataset_file = sys.argv[2]
    dag = json.loads(dag_json)

    res, _, _ = eval_dag(dag, dataset_file)
    print("result: " + str(res))
