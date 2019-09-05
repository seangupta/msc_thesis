#!/bin/bash

#$ -cwd
#$ -S /bin/bash
#$ -o $HOME/array.out
#$ -e $HOME/array.err
#$ -t 1-8
#$ -l tmem=10G
#$ -l h_rt=40:00:00
#$ -l gpu=1

export LANG="en_US.utf8"
export LANGUAGE="en_US:en"

# Activate the correct gpu environment
# A cheap way of doing it is to just source the bashrc (example above)
source /home/agupta/.bashrc

cd /home/agupta

# The counter $SGE_TASK_ID will be incremented up to 10; 1 for each job

#test $SGE_TASK_ID -eq 1 && sleep 10 && PYTHONPATH=. python ./hello_world.py
#test $SGE_TASK_ID -eq 1 && sleep 10 && PYTHONPATH=. allennlp fine-tune -m /home/agupta/workspace/drop_dataset/alternative_full_new -c /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet -s /home/agupta/workspace/drop_dataset/alternative_full_new_cont > alternative_full_new_cont.log 2>&1
#test $SGE_TASK_ID -eq 1 && sleep 10 && PYTHONPATH=. allennlp find-lr /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet -s /home/agupta/workspace/drop_dataset/serialized_nalu_findlr > naqanet_nalu_findlr 2>&1
#test $SGE_TASK_ID -eq 1 && sleep 60 && PYTHONPATH=. allennlp predict --output-file /home/agupta/workspace/drop_dataset/predictions --use-dataset-reader /home/agupta/workspace/drop_dataset/serialized_nalug1t1 /home/agupta/workspace/drop_dataset/drop_dataset_dev.json

test $SGE_TASK_ID -eq 1 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/1 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 1, "model.use_encoded_nums": false, "model.loss": "square"}'  > 1_false_square.log 2>&1
test $SGE_TASK_ID -eq 2 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/2 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 1, "model.use_encoded_nums": false, "model.loss": "absolute"}'  > 1_false_abs.log 2>&1
test $SGE_TASK_ID -eq 3 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/3 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 1, "model.use_encoded_nums": true, "model.loss": "square"}'  > 1_true_square.log 2>&1
test $SGE_TASK_ID -eq 4 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/4 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 1, "model.use_encoded_nums": true, "model.loss": "absolute"}'  > 1_true_abs.log 2>&1
test $SGE_TASK_ID -eq 5 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/5 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 10, "model.use_encoded_nums": false, "model.loss": "square"}'  > 10_false_square.log 2>&1
test $SGE_TASK_ID -eq 6 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/6 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 10, "model.use_encoded_nums": false, "model.loss": "absolute"}'  > 10_false_abs.log 2>&1
test $SGE_TASK_ID -eq 7 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/7 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 10, "model.use_encoded_nums": true, "model.loss": "square"}'  > 10_true_square.log 2>&1
test $SGE_TASK_ID -eq 8 && sleep 10 && PYTHONPATH=. allennlp train -s /home/agupta/workspace/drop_dataset/8 /home/agupta/workspace/allennlp/training_config/naqanet.jsonnet --overrides '{"model.g": 10, "model.use_encoded_nums": true, "model.loss": "absolute"}'  > 10_true_abs.log 2>&1