'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element 
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the 
.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person 
if there is some email that is common to both accounts. Note that even if two accounts have the 
same name, they may belong to different people as people could have the same name. A person can 
have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of 
each account is the name, and the rest of the elements are emails in sorted order. The accounts
 themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", 
"johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by 
other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], 
['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be 
accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''
from collections import defaultdict

def accounts_merge(accounts):
    graph = defaultdict(set)
    components_id = {}

    def add_edge(u, v):
        graph[u].add(v)
        graph[v].add(u)

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            add_edge(account[1], email)
            components_id[email] = name

    def dfs(source):
        nonlocal emails
        seen.add(source)
        emails.append(source)

        for node in graph[source]:
            if node not in seen:
                dfs(node)

    result, seen = [], set()
    for email in graph:
        if email not in seen:
            emails = list()
            dfs(email)
            result.append([components_id[email]] + sorted(emails))

    return result 