<h1>ERC20 tokenholders list</h1>

## Introduction

Super simple way to get token holders and amount for ERC20 token

Requirements:
  less than 5000 tokenholders (if you have more, use a bigger solution)
  python


use etherscan to download the csv file of the token transfers
https://etherscan.io/token/'address of your token contract'
name export file  export-token.csv (in the current directory)
run  'python3 tokenlist.py > yourfile'

now you have a file with the addresses and amounts of your token



