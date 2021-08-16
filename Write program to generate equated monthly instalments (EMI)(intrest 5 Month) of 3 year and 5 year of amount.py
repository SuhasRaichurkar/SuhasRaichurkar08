#Write program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-

a=161258

e3=a/36

e5=a/60

emi3=e3+(0.05*e3)

emi5=e5+(0.05*e5)

print("EMI for 3 years with intrest 5%",emi3)

print("EMI for 5 years with intrest 5%",emi5)