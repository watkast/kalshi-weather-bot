# Range-Scalp Bot

*Updated Fri Nov 20 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66472 | 58014 | 8458 (128) | 2 | $-17877.17 | -4.3% |
| **+10¢** | 49627 | 39739 | 9888 (170) | 5 | $-16637.18 | -5.3% |
| **+15¢** | 41617 | 30955 | 10662 (217) | 5 | $-14951.50 | -5.7% |
| **+20¢** | 37052 | 25856 | 11196 (273) | 5 | $-13223.74 | -5.7% |
| **+10¢ (15¢ stop)** | 80940 | 80774 | 166 (100) | 0 | $-29891.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 17:44 | +10 stop | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-20 17:41 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-20 17:41 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-20 17:41 | +10 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-20 17:41 | +5 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-20 17:41 | +10 stop | SOL | DOWN | 0.50 | 0.69 | 1.57 |
| 11-20 17:41 | +15 | SOL | DOWN | 0.50 | 0.69 | 1.57 |
| 11-20 17:41 | +10 | SOL | DOWN | 0.51 | 0.69 | 1.45 |
| 11-20 17:41 | +5 | SOL | DOWN | 0.51 | 0.69 | 1.45 |
| 11-20 17:40 | +10 stop | XRP | DOWN | 0.58 | 0.37 | -2.45 |
| 11-20 17:40 | +5 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-20 17:39 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 11-20 17:39 | +20 | DOGE | UP | 0.48 | 0.71 | 1.97 |
| 11-20 17:39 | +15 | DOGE | UP | 0.48 | 0.65 | 1.36 |
| 11-20 17:39 | +10 | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 11-20 17:39 | +5 | DOGE | UP | 0.50 | 0.55 | 0.14 |
| 11-20 17:38 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 11-20 17:38 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 11-20 17:38 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-20 17:38 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-20 17:38 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-20 17:38 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 11-20 17:37 | +10 stop | HYPE | UP | 0.45 | 0.56 | 0.74 |
| 11-20 17:37 | +10 stop | BNB | UP | 0.52 | 0.36 | -1.95 |
| 11-20 17:37 | +10 stop | XRP | UP | 0.68 | 0.42 | -2.94 |
| 11-20 17:37 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-20 17:37 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-20 17:36 | +10 stop | XRP | DOWN | 0.44 | 0.54 | 0.64 |
| 11-20 17:36 | +10 stop | NEAR | UP | 0.71 | 0.32 | -4.21 |
| 11-20 17:36 | +10 | NEAR | UP | 0.70 | open |  |
| 11-20 17:36 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-20 17:36 | +10 stop | BNB | DOWN | 0.57 | 0.39 | -2.15 |
| 11-20 17:36 | +10 stop | ETH | DOWN | 0.53 | 0.25 | -3.12 |
| 11-20 17:35 | +10 stop | XRP | DOWN | 0.68 | 0.52 | -1.94 |
| 11-20 17:35 | +20 | XRP | DOWN | 0.68 | 0.90 | 2.01 |
| 11-20 17:35 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 11-20 17:35 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-20 17:35 | +5 | XRP | DOWN | 0.68 | 0.77 | 0.61 |
| 11-20 17:35 | +10 stop | NEAR | UP | 0.49 | 0.65 | 1.22 |
| 11-20 17:35 | +10 | NEAR | UP | 0.49 | 0.65 | 1.22 |
