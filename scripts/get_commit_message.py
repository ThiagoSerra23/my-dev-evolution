import os

def main():
    msg_file = os.path.join(os.path.dirname(__file__), 'last_commit_msg.txt')
    if os.path.exists(msg_file):
        with open(msg_file, 'r', encoding='utf-8') as f:
            print(f.read().strip())
    else:
        print("chore: automated evolution update")

if __name__ == "__main__":
    main()
