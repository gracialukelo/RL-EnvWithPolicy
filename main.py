from showerEnv import ShowerEnv
from showerPolicy import SimplePolicy


def main() -> None:
    env = ShowerEnv()
    policy = SimplePolicy()

    total_reward = 0
    state = env.reset()
    done = False

    while not done:
        action = policy.choose_action(state)
        state, reward, done, _ = env.step(action)
        print(f"Reward: {total_reward}")
        total_reward += reward

    print(f"Gesamtbelohnung: {total_reward}")


if __name__ == "__main__":
    main()
