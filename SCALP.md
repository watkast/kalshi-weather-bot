# Range-Scalp Bot

*Updated Tue Oct 20 02:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24929 | 21708 | 3221 (31) | 0 | $-7259.38 | -4.6% |
| **+10¢** | 18756 | 15032 | 3724 (46) | 0 | $-6452.07 | -5.5% |
| **+15¢** | 15700 | 11688 | 4012 (70) | 0 | $-5822.24 | -5.9% |
| **+20¢** | 13883 | 9682 | 4201 (88) | 0 | $-5225.82 | -6.0% |
| **+10¢ (15¢ stop)** | 30582 | 30530 | 52 (30) | 0 | $-11390.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 02:03 | +10 stop | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 10-20 02:03 | +20 | BNB | DOWN | 0.58 | 0.86 | 2.53 |
| 10-20 02:03 | +15 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 10-20 02:03 | +10 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 10-20 02:03 | +5 | BNB | DOWN | 0.58 | 0.66 | 0.46 |
| 10-20 02:02 | +10 stop | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-20 02:02 | +10 | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-20 02:02 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-20 02:02 | +10 stop | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-20 02:02 | +10 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-20 02:02 | +5 | ZEC | DOWN | 0.62 | 0.81 | 1.62 |
| 10-20 02:02 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
| 10-20 02:01 | +10 stop | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 10-20 02:01 | +20 | SOL | DOWN | 0.53 | 0.76 | 1.99 |
| 10-20 02:01 | +15 | SOL | DOWN | 0.53 | 0.68 | 1.16 |
| 10-20 02:01 | +10 | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 10-20 02:01 | +5 | SOL | DOWN | 0.53 | 0.58 | 0.14 |
| 10-20 02:01 | +10 stop | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-20 02:01 | +20 | ZEC | DOWN | 0.52 | 0.81 | 2.61 |
| 10-20 02:01 | +15 | ZEC | DOWN | 0.52 | 0.81 | 2.61 |
| 10-20 02:01 | +10 | ZEC | DOWN | 0.52 | 0.62 | 0.65 |
| 10-20 02:01 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 10-20 02:01 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-20 02:01 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-20 02:01 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 02:01 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-20 02:01 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 10-20 02:01 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 02:01 | +20 | NEAR | DOWN | 0.70 | 0.94 | 2.16 |
| 10-20 02:01 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-20 02:01 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 02:01 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-20 02:01 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-20 02:01 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.83 |
| 10-20 02:01 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.30 |
| 10-20 02:01 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.20 |
| 10-20 02:01 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.37 |
| 10-20 02:01 | +10 stop | XRP | DOWN | 0.56 | 0.71 | 1.17 |
| 10-20 02:01 | +20 | XRP | DOWN | 0.56 | 0.77 | 1.79 |
| 10-20 02:01 | +15 | XRP | DOWN | 0.56 | 0.71 | 1.17 |
