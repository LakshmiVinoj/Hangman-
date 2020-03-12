import check
def letter_update(secret,dashes,guess):
    if secret=="":
        return ""
    if secret[0]==dashes[0]:
        return secret[0] + letter_update(secret[1:],dashes[1:],guess)
    elif guess==secret[0]:
        return guess + letter_update(secret[1:],dashes[1:],guess)
    else:
        return "-" + letter_update(secret[1:],dashes[1:],guess)

def update_dashes(secret,dashes,guess):
    print(letter_update(secret,dashes,guess))
   
##Examples:  
check.set_print_exact("p-----")
check.expect("Example 1:",update_dashes("python","p-----","x"),None)
check.set_print_exact("b-bb-e")
check.expect("Example 2:",update_dashes("bubble","b-bb--","e"),None)
check.set_print_exact("b-bb--")
check.expect("Example 3:",update_dashes("bubble","------","b"),None)

##Tests:
check.set_print_exact("spring")
check.expect("Q3T1",update_dashes("spring","sprin-","g"),None)
check.set_print_exact("--ll---")
check.expect("Q3T2",update_dashes("college","--ll---","l"),None)
check.set_print_exact("---------")
check.expect("Q3T3",update_dashes("firetruck","---------","w"),None)
