# TODO create a passing and a failing test for this in test.py
def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    Finds the longest common prefix from a given list of words

    Args:
        strs (List[str]): a list of strings

    Returns:
        str: A string representation of the longest common prefix of the given strings
    """
    if not strs: return ""

    word1 = min(strs)
    word2 = max(strs)
    for it, char in enumerate(word1):
        if char != word2[it]:
            return word1[:it]
    return word1
