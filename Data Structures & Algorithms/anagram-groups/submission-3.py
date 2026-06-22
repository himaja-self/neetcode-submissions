class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for string in strs:
            if ''.join(sorted(string)) in hashMap:
                hashMap[''.join(sorted(string))].append(string)
            else:
                hashMap[''.join(sorted(string))] = [string]
        
        return list(hashMap.values())