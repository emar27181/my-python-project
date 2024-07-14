# 初期化
actions = ["Move", "Turn", "Left", "Right"]
V = {action: 0 for action in actions}  # 各行動に対する強化値を初期化


def reinforce(actions, rewards, alpha, gamma):
    for t in range(len(actions)):
        V[actions[t]] += alpha * (gamma ** (len(actions) - 1 - t)) * rewards


# 使用例
actions_sequence = ["Move", "Turn", "Left", "Right"]
rewards = 100
alpha = 0.1
gamma = 0.9

reinforce(actions_sequence, rewards, alpha, gamma)

print(V)
