import math

def calculate_entropy(probabilities):
    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# 示例用法
if __name__ == "__main__":
    probs = []
    while True:
        try:
            s = input("请输入一个概率（输入空行结束）：")
            if s.strip() == "":
                break
            p = float(s)
            if p < 0 or p > 1:
                print("概率应在0到1之间。")
                continue
            probs.append(p)
        except ValueError:
            print("请输入有效的数字。")
    if not probs:
        probs = [0.2, 0.3, 0.5]
print("信源熵为:", calculate_entropy(probs))