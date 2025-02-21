#!/bin/bash
while read domain; do
    if ! whois "$domain" | grep -q "No match"; then
        echo "$domain is TAKEN"
    else
        echo "$domain is AVAILABLE"
    fi
done < domains.txt

#Give execution permission:
    #chmod +x check_domains.sh
#Run the script:
    #./check_domains.sh
