# Long version
def compute_accuracy(gt, pred):
  counter = 0
  for n in range(len(pred)):
    if pred[n] == gt[n]:
      counter += 1
  return counter / len(pred)

compute_accuracy(data_y, y_pred)

# Short version
def compute_accuracy_short(gt, pred):
  return len([x for x,y in zip(gt, pred) if x == y]) / len(pred)


compute_accuracy_short(data_y, y_pred)