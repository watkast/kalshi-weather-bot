# Range-Scalp Bot

*Updated Tue Oct 20 21:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26218 | 22832 | 3386 (32) | 0 | $-7668.74 | -4.6% |
| **+10¢** | 19732 | 15821 | 3911 (47) | 0 | $-6768.03 | -5.5% |
| **+15¢** | 16514 | 12306 | 4208 (71) | 0 | $-6041.27 | -5.8% |
| **+20¢** | 14614 | 10201 | 4413 (90) | 0 | $-5441.12 | -5.9% |
| **+10¢ (15¢ stop)** | 32111 | 32058 | 53 (30) | 0 | $-11743.76 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 21:11 | +10 stop | XRP | UP | 0.63 | 0.75 | 0.89 |
| 10-20 21:11 | +10 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 10-20 21:11 | +5 | XRP | UP | 0.67 | 0.75 | 0.50 |
| 10-20 21:11 | +10 stop | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 21:11 | +10 stop | SOL | UP | 0.63 | 0.45 | -2.15 |
| 10-20 21:08 | +10 stop | BNB | UP | 0.57 | 0.75 | 1.48 |
| 10-20 21:08 | +20 | XRP | UP | 0.69 | 0.94 | 2.31 |
| 10-20 21:08 | +15 | XRP | UP | 0.69 | 0.94 | 2.31 |
| 10-20 21:08 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 10-20 21:08 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 21:08 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-20 21:08 | +15 | SOL | UP | 0.64 | 0.96 | 3.09 |
| 10-20 21:07 | +10 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 10-20 21:07 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 10-20 21:07 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 21:07 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-20 21:07 | +10 | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 21:07 | +5 | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 21:07 | +10 stop | ZEC | DOWN | 0.55 | 0.37 | -2.10 |
| 10-20 21:07 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 10-20 21:05 | +5 | BNB | DOWN | 0.58 | 0.92 | 3.11 |
| 10-20 21:05 | +10 stop | XRP | DOWN | 0.66 | 0.47 | -2.24 |
| 10-20 21:05 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 21:05 | +10 stop | SOL | DOWN | 0.64 | 0.49 | -1.85 |
| 10-20 21:05 | +10 | SOL | DOWN | 0.64 | yes | -6.57 |
| 10-20 21:05 | +5 | SOL | DOWN | 0.69 | yes | -7.05 |
| 10-20 21:05 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-20 21:04 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-20 21:04 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-20 21:04 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-20 21:04 | +20 | ETH | UP | 0.63 | 0.84 | 1.83 |
| 10-20 21:04 | +15 | ETH | UP | 0.63 | 0.80 | 1.41 |
| 10-20 21:04 | +10 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-20 21:04 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 10-20 21:04 | +10 stop | ZEC | DOWN | 0.57 | 0.73 | 1.31 |
| 10-20 21:04 | +5 | NEAR | UP | 0.67 | no | -6.86 |
| 10-20 21:03 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.75 |
| 10-20 21:03 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-20 21:03 | +20 | DOGE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-20 21:03 | +15 | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
