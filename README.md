# KEY-DISTRIBUTOR
## A SAFE AND EASY WAY TO DISTRIBUTE YOUR PRIVTE KEY

Uses Shamir's secret sharing scheme and preserves the ease of using a mnemonic phrase

### To split your key up
select "Distribute" from the menu. Enter the threshold value, k, and the number of secrets, n. This describes a k out of n scheme. Your mnemonic is mapped to n different mnemonics referred to as "secrets." Only k of those mnemonics are needed to recover your private key. After you type in your private key, the program will print your n secrets as well as their secret numbers. Save the secrets and their corresponding secret number.

### To Recover your key
select "Recover" from the menu. Enter the length of the private key you are trying to recover, as well as the threshold, k, determined when you split up your private key. For each of the k secrets you have possession of, first enter the secret number, then enter the secret. When all k secrets have been entered, your private key will be displayed.
