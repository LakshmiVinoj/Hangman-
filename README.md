# Hangman-

The function update_dashes(secret, dashes, guess) that consumes three strings:

• secret, which is the word the player is attempting to guess 

• dashes, which is the representation of secret using a string of hyphens and already guessed letters, if any 

• guess, which is the player’s newest guess The function does not return a value, instead it prints the updated version of dashes if guess is in secret. If guess is not in secret, the original dashes is printed.

# letter_update 
A function that returns the updated word if a letter is correctly guessed, otherwise it returns the original dashes, 
after consuming three strings secret, dashes and guess.

letter_update: Str Str Str->Str

Requires:

*dashes can be a mix of letters or hyphens

*secret and guess are only letters

*string length of dashes = string length of secret

*guess is only one character

*all three parameters are non-empty strings and lowercase letters
___________________________________________________________________________________________________________________________________
 
# update_dashes 
A function that prints the updated word if a letter is correctly guessed, otherwise it prints the original dashes, 
after consuming three strings secret,dashes and guess.
    
Effects: Prints to the screen 
    
update_dashes: Str Str Str->None

Requires:

*dashes can be a mix of letters or hyphens

*secret and guess are only letters

*string length of dashes = string length of secret

*guess is only one character

*all three parameters are non-empty strings and lowercase letters
____________________________________________________________________________________________________________________________________    

Examples:

*Calling update_dashes("python","p-----","x") prints "p-----"

*Calling update_dashes("bubble","b-bb--","e") prints "b-bb-e"

*Calling update_dashes("bubble","------","b") prints "b-bb--"
 
