class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_sorted(self):
        result = []
        self.collect(self.root, "", result)
        return result

    def collect(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)
        for char in sorted(node.children.keys()):
            self.collect(node.children[char], prefix + char, result)


def find_suffix(k, s):
    trie = Trie()
    # 모든 접미어를 Trie 에 삽입
    for i in range(len(s)):
        trie.insert(s[i:])

    sorted_suffixes = trie.get_sorted()
    if k - 1 < len(sorted_suffixes):
        return sorted_suffixes[k - 1]
    else:
        return "none"


if __name__ == "__main__":
    T = int(input())

    results = []
    for tc in range(1, T + 1):
        K = int(input())
        S = input()

        answer = find_suffix(K, S)
        print(f"#{tc} {answer}")
