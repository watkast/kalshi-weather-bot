# Range-Scalp Bot

*Updated Sun Oct 25 05:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32651 | 28467 | 4184 (42) | 0 | $-9318.02 | -4.5% |
| **+10¢** | 24443 | 19597 | 4846 (60) | 0 | $-8349.08 | -5.4% |
| **+15¢** | 20463 | 15251 | 5212 (83) | 0 | $-7497.63 | -5.8% |
| **+20¢** | 18127 | 12673 | 5454 (105) | 1 | $-6637.48 | -5.8% |
| **+10¢ (15¢ stop)** | 40118 | 40058 | 60 (32) | 0 | $-15364.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 05:45 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 10-25 05:45 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-25 05:45 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-25 05:45 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-25 05:45 | +10 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-25 05:45 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 10-25 05:34 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 10-25 05:33 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-25 05:33 | +5 | BNB | UP | 0.63 | no | -6.43 |
| 10-25 05:32 | +10 stop | ZEC | DOWN | 0.68 | 0.83 | 1.25 |
| 10-25 05:32 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.25 |
| 10-25 05:32 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.21 |
| 10-25 05:32 | +10 stop | BNB | UP | 0.67 | 0.32 | -3.86 |
| 10-25 05:32 | +10 stop | NEAR | UP | 0.58 | 0.20 | -4.10 |
| 10-25 05:32 | +10 stop | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-25 05:32 | +10 stop | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-25 05:32 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 10-25 05:32 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-25 05:32 | +10 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-25 05:32 | +5 | ETH | DOWN | 0.60 | 0.69 | 0.58 |
| 10-25 05:31 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 05:31 | +20 | ZEC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-25 05:31 | +15 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-25 05:31 | +10 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-25 05:31 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-25 05:31 | +10 stop | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-25 05:31 | +20 | DOGE | DOWN | 0.67 | 0.89 | 1.97 |
| 10-25 05:31 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-25 05:31 | +10 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-25 05:31 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-25 05:31 | +10 stop | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-25 05:31 | +20 | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-25 05:31 | +15 | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-25 05:31 | +10 | BTC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-25 05:31 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-25 05:31 | +10 stop | BNB | UP | 0.60 | 0.42 | -2.15 |
| 10-25 05:31 | +20 | BNB | UP | 0.60 | no | -6.17 |
| 10-25 05:31 | +15 | BNB | UP | 0.60 | no | -6.17 |
| 10-25 05:31 | +10 | BNB | UP | 0.60 | no | -6.17 |
| 10-25 05:31 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
