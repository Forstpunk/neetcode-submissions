class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for m in emails:
            local, domain = m.split("@")    # split at @
            local = local.split("+")[0]          # remove everything after +
            local = local.replace(".", "")       # remove all dots
            seen.add(local+ "@" +domain)            # add cleaned email
        
        return len(seen)
        