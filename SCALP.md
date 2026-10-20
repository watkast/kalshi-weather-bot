# Range-Scalp Bot

*Updated Tue Oct 20 08:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25403 | 22127 | 3276 (31) | 0 | $-7373.18 | -4.6% |
| **+10¢** | 19122 | 15336 | 3786 (46) | 0 | $-6521.45 | -5.4% |
| **+15¢** | 16001 | 11923 | 4078 (70) | 1 | $-5856.43 | -5.8% |
| **+20¢** | 14145 | 9876 | 4269 (88) | 0 | $-5237.48 | -5.9% |
| **+10¢ (15¢ stop)** | 31176 | 31124 | 52 (30) | 0 | $-11523.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 08:49 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 08:49 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-20 08:49 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 08:49 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-20 08:49 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-20 08:48 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-20 08:48 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-20 08:48 | +5 | NEAR | DOWN | 0.62 | 0.69 | 0.38 |
| 10-20 08:47 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.26 |
| 10-20 08:47 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-20 08:47 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-20 08:47 | +15 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-20 08:47 | +10 | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-20 08:47 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-20 08:46 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 10-20 08:46 | +20 | BNB | DOWN | 0.61 | 0.86 | 2.24 |
| 10-20 08:46 | +15 | BNB | DOWN | 0.61 | 0.80 | 1.61 |
| 10-20 08:46 | +10 | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 10-20 08:46 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 10-20 08:46 | +10 stop | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 10-20 08:46 | +20 | SOL | DOWN | 0.71 | 0.93 | 2.00 |
| 10-20 08:46 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-20 08:46 | +10 | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 10-20 08:46 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-20 08:46 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 08:46 | +20 | ETH | DOWN | 0.69 | 0.90 | 1.92 |
| 10-20 08:46 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-20 08:46 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-20 08:46 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 10-20 08:46 | +10 stop | ZEC | DOWN | 0.53 | 0.69 | 1.24 |
| 10-20 08:46 | +20 | ZEC | DOWN | 0.53 | 0.78 | 2.17 |
| 10-20 08:46 | +15 | ZEC | DOWN | 0.53 | 0.69 | 1.24 |
| 10-20 08:46 | +10 | ZEC | DOWN | 0.53 | 0.69 | 1.24 |
| 10-20 08:46 | +5 | ZEC | DOWN | 0.53 | 0.69 | 1.24 |
| 10-20 08:46 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 10-20 08:46 | +20 | NEAR | DOWN | 0.60 | 0.87 | 2.45 |
| 10-20 08:46 | +15 | NEAR | DOWN | 0.60 | 0.87 | 2.45 |
| 10-20 08:46 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 10-20 08:46 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 10-20 08:46 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
