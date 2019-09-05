import jsonlines
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import mpl_toolkits.axes_grid1 as axes_grid1

PREDICTIONS_PATH = "/Users/seangupta/Google Drive/Studies/UCL/Thesis/predictions"
GROUND_TRUTH_PATH = "/Users/seangupta/Google Drive/Studies/UCL/Thesis/drop_dataset/drop_dataset_dev.json"
OUTPUT_PATH = "/Users/seangupta/Google Drive/Studies/UCL/Thesis/qualitative_results_true_W.txt"
HIST_PATH = "/Users/seangupta/Google Drive/Studies/UCL/Thesis/hist_entries"
HEATMAP_PATH = "/Users/seangupta/Google Drive/Studies/UCL/Thesis/heatmap"

pred = {}
to_print = open(OUTPUT_PATH, "w+")

with open(PREDICTIONS_PATH, 'r+') as f:
    for item in jsonlines.Reader(f):
        pred[item["question_id"]] = item["answer"]

with open(GROUND_TRUTH_PATH, 'r+') as file:
    true = json.load(file)

total_true = 0
total_false = 0

true_questions = []
false_questions = []

W_all = np.array([])
W_heatmap = np.expand_dims(np.zeros(25), axis=0)

for passage in true:
    passage_printed = False
    Qs = true[passage]['qa_pairs']
    for qa_pair in Qs:
        query_id = qa_pair["query_id"]
        if query_id in pred:
            if not passage_printed:
                to_print.write(true[passage]['passage'] + "\n\n")
            passage_printed = True
            to_print.write(qa_pair['question'] + "\n")
            prediction = pred[query_id]["value"]
            calc = pred[query_id]["calc"]
            new_nums = np.array([w for w, raw_num in calc])
            W_all = np.concatenate([W_all, new_nums])
            W_heatmap = np.concatenate([W_heatmap, np.expand_dims(new_nums, axis=0)], axis=0)

            if qa_pair["answer"]["number"]:
                ground_truth = qa_pair["answer"]["number"]
            elif any(qa_pair["answer"]["date"][key] for key in qa_pair["answer"]["date"].keys()):
                ground_truth = qa_pair["answer"]["date"]
            elif qa_pair["answer"]["spans"]:
                ground_truth = qa_pair["answer"]["spans"]
            ground_truth = int(ground_truth)
            prediction = int(prediction)
            to_print.write("prediction = %s, ground truth = %s \n" % (prediction, ground_truth))
            if prediction == ground_truth:
                to_print.write("correct\n\n")
                to_print.write(true[passage]['passage'] + "\n\n")
                to_print.write(qa_pair['question'] + "\n")
                to_print.write("prediction = %s, ground truth = %s \n\n" % (prediction, ground_truth))
                to_print.write(str(calc) + "\n\n")
                total_true += 1
            else:
                to_print.write("incorrect\n\n")
                total_false += 1

print("Total true =", total_true)
to_print.write("Total true = " + str(total_true))
print("Total false =", total_false)
to_print.write("Total false = " + str(total_false))
to_print.close()

large_neg_count = len([num for num in W_all if num < -0.5])
large_pos_count = len([num for num in W_all if num > 0.5])

print("Large negative count =", large_neg_count)
print("Large positive count =", large_pos_count)

plt.hist(W_all, bins=20)
plt.xlabel("W entries")
plt.ylabel("Frequency")
plt.savefig(HIST_PATH)

row_count = W_heatmap.shape[0]
random_indices = random.choices(range(row_count), k=50)
W_heatmap = W_heatmap[random_indices]

fig = plt.figure()
plt.imshow(W_heatmap)
plt.colorbar()
plt.xlabel("Number indices")
plt.ylabel("QA pairs")
plt.savefig(HEATMAP_PATH)