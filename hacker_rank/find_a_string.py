org_str = input()
sub_string = input()
# 0123456
# ABCDCDC
# [1, 1]


# Count of substrings using startswith
res = sum(1 for i in range(len(org_str)) if org_str[i:i+len(sub_string)] == sub_string)
# res = sum(1 for i in range(len(org_str)) if org_str.startswith(sub_string, i))

# Printing result
print(res)
