from awsfunctions import get_EC2_dns, get_session_credentials



####################
EC2_dns = get_EC2_dns()

print(EC2_dns)
print(get_session_credentials())