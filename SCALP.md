# Range-Scalp Bot

*Updated Sat Oct 03 11:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 657 | 564 | 93 (1) | 2 | $-247.04 | -5.9% |
| **+10¢** | 499 | 395 | 104 (2) | 3 | $-208.88 | -6.6% |
| **+15¢** | 427 | 316 | 111 (3) | 3 | $-188.20 | -7.0% |
| **+20¢** | 371 | 257 | 114 (3) | 3 | $-175.00 | -7.5% |
| **+10¢ (15¢ stop)** | 853 | 852 | 1 (1) | 1 | $-465.48 | -8.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 11:07 | +10 stop | HYPE | UP | 0.57 | 0.40 | -2.09 |
| 10-03 11:07 | +10 stop | HYPE | DOWN | 0.68 | 0.45 | -2.68 |
| 10-03 11:07 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-03 11:07 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-03 11:07 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-03 11:07 | +5 | BTC | UP | 0.68 | open |  |
| 10-03 11:06 | +5 | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-03 11:05 | +10 stop | ETH | DOWN | 0.61 | 0.43 | -2.15 |
| 10-03 11:05 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-03 11:05 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-03 11:05 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-03 11:05 | +10 stop | BTC | UP | 0.59 | open |  |
| 10-03 11:05 | +20 | BTC | UP | 0.59 | open |  |
| 10-03 11:05 | +15 | BTC | UP | 0.59 | open |  |
| 10-03 11:05 | +10 | BTC | UP | 0.59 | open |  |
| 10-03 11:05 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 10-03 11:03 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.13 |
| 10-03 11:03 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.81 |
| 10-03 11:03 | +15 | ZEC | DOWN | 0.64 | 0.82 | 1.55 |
| 10-03 11:03 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.13 |
| 10-03 11:03 | +5 | ZEC | DOWN | 0.64 | 0.78 | 1.13 |
| 10-03 11:02 | +10 stop | BNB | UP | 0.58 | 0.70 | 0.90 |
| 10-03 11:01 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 11:01 | +20 | XRP | DOWN | 0.59 | 0.85 | 2.34 |
| 10-03 11:01 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 11:01 | +10 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 11:01 | +5 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 11:01 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 11:01 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-03 11:01 | +15 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-03 11:01 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 11:01 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 11:01 | +10 stop | HYPE | DOWN | 0.61 | 0.77 | 1.26 |
| 10-03 11:01 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-03 11:01 | +15 | HYPE | DOWN | 0.61 | 0.77 | 1.26 |
| 10-03 11:01 | +10 | HYPE | DOWN | 0.61 | 0.77 | 1.26 |
| 10-03 11:01 | +5 | HYPE | DOWN | 0.61 | 0.77 | 1.26 |
| 10-03 11:01 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.83 |
| 10-03 11:01 | +20 | BNB | UP | 0.70 | 0.90 | 1.82 |
| 10-03 11:01 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
