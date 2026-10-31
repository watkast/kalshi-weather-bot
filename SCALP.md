# Range-Scalp Bot

*Updated Sat Oct 31 09:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42075 | 36706 | 5369 (55) | 4 | $-11840.45 | -4.5% |
| **+10¢** | 31367 | 25154 | 6213 (79) | 5 | $-10576.96 | -5.4% |
| **+15¢** | 26223 | 19525 | 6698 (107) | 6 | $-9674.27 | -5.9% |
| **+20¢** | 23287 | 16273 | 7014 (138) | 6 | $-8513.21 | -5.8% |
| **+10¢ (15¢ stop)** | 51301 | 51226 | 75 (41) | 1 | $-19368.03 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 09:42 | +10 stop | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 10-31 09:42 | +10 stop | ETH | UP | 0.64 | open |  |
| 10-31 09:42 | +15 | ETH | UP | 0.64 | open |  |
| 10-31 09:42 | +10 stop | BNB | DOWN | 0.56 | 0.70 | 1.07 |
| 10-31 09:42 | +20 | BNB | DOWN | 0.56 | open |  |
| 10-31 09:42 | +10 | BNB | DOWN | 0.56 | 0.70 | 1.07 |
| 10-31 09:42 | +5 | BNB | DOWN | 0.56 | 0.70 | 1.07 |
| 10-31 09:41 | +10 stop | BTC | DOWN | 0.71 | 0.43 | -3.13 |
| 10-31 09:41 | +15 | BTC | DOWN | 0.70 | open |  |
| 10-31 09:41 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-31 09:41 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-31 09:41 | +10 stop | ETH | DOWN | 0.65 | 0.35 | -3.32 |
| 10-31 09:41 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-31 09:41 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-31 09:41 | +10 stop | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 10-31 09:41 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-31 09:41 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-31 09:41 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-31 09:41 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-31 09:40 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-31 09:40 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 09:40 | +5 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 09:40 | +10 stop | ETH | DOWN | 0.40 | 0.62 | 1.86 |
| 10-31 09:40 | +10 | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 10-31 09:40 | +5 | ETH | DOWN | 0.41 | 0.62 | 1.76 |
| 10-31 09:39 | +10 stop | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-31 09:39 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 09:39 | +10 stop | DOGE | DOWN | 0.62 | 0.39 | -2.64 |
| 10-31 09:39 | +10 stop | ETH | UP | 0.48 | 0.62 | 1.05 |
| 10-31 09:39 | +20 | ETH | UP | 0.48 | 0.72 | 2.07 |
| 10-31 09:39 | +15 | ETH | UP | 0.48 | 0.64 | 1.25 |
| 10-31 09:39 | +10 | ETH | UP | 0.48 | 0.62 | 1.05 |
| 10-31 09:39 | +5 | ETH | UP | 0.51 | 0.62 | 0.75 |
| 10-31 09:39 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-31 09:39 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-31 09:39 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-31 09:39 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-31 09:38 | +10 stop | ZEC | UP | 0.62 | 0.40 | -2.54 |
| 10-31 09:38 | +10 stop | DOGE | UP | 0.64 | 0.40 | -2.74 |
| 10-31 09:38 | +10 | DOGE | UP | 0.63 | open |  |
