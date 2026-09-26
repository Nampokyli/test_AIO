def ex1(tp, fp, fn):
    if type(tp) is not int:
        print("tp must be int")
        return

    if type(fp) is not int:
        print("fp must be int")
        return

    if type(fn) is not int:
        print("fn must be int")
        return

    if tp < 0 or fp < 0 or fn < 0:
        print("tp, fp and fn must be greater than or equal to 0")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    return precision, recall, f1_score
tp=input("Nhập giá tp: ")
fp=input("Nhập giá fp: ")
fn=input("Nhập giá fn: ")
print(ex1(int(tp), int(fp), int(fn)))
