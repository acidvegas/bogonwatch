# BogonWatch

Automated tracking of Team Cymru's Bogon IP lists. This repository automatically updates every 4 hours to track changes in bogon IP address space.

## What are Bogons?

Bogon IP addresses are addresses that should never appear on the public internet. These include:
- Private networks (RFC1918)
- Reserved addresses
- Unallocated address blocks

## Files

- `bogons_ipv4.txt` - Current IPv4 bogon list
- `bogons_ipv6.txt` - Current IPv6 bogon list

## Update Schedule

Lists are automatically updated every 4 hours via GitHub Actions.

## Data Source

Lists are sourced from Team Cymru's Bogon Reference:
- IPv4: https://team-cymru.org/Services/Bogons/fullbogons-ipv4.txt
- IPv6: https://team-cymru.org/Services/Bogons/fullbogons-ipv6.txt 