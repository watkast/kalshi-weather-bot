# Range-Scalp Bot

*Updated Mon Oct 05 10:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3663 | 3145 | 518 (3) | 1 | $-1327.19 | -5.7% |
| **+10¢** | 2827 | 2231 | 596 (4) | 4 | $-1223.93 | -6.9% |
| **+15¢** | 2375 | 1749 | 626 (7) | 6 | $-1059.95 | -7.1% |
| **+20¢** | 2120 | 1468 | 652 (12) | 6 | $-913.56 | -6.9% |
| **+10¢ (15¢ stop)** | 4548 | 4547 | 1 (1) | 2 | $-1755.96 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 10:04 | +10 stop | ZEC | UP | 0.38 | 0.52 | 1.05 |
| 10-05 10:04 | +20 | ZEC | UP | 0.38 | open |  |
| 10-05 10:04 | +15 | ZEC | UP | 0.38 | open |  |
| 10-05 10:04 | +10 | ZEC | UP | 0.38 | 0.52 | 1.05 |
| 10-05 10:04 | +5 | ZEC | UP | 0.38 | 0.52 | 1.05 |
| 10-05 10:02 | +10 stop | DOGE | UP | 0.58 | 0.72 | 1.08 |
| 10-05 10:02 | +5 | DOGE | UP | 0.58 | 0.72 | 1.08 |
| 10-05 10:02 | +10 stop | NEAR | UP | 0.58 | open |  |
| 10-05 10:02 | +20 | NEAR | UP | 0.58 | open |  |
| 10-05 10:02 | +15 | NEAR | UP | 0.58 | open |  |
| 10-05 10:02 | +10 | NEAR | UP | 0.58 | open |  |
| 10-05 10:02 | +5 | NEAR | UP | 0.58 | 0.66 | 0.47 |
| 10-05 10:02 | +10 stop | ETH | UP | 0.69 | open |  |
| 10-05 10:02 | +20 | ETH | UP | 0.69 | open |  |
| 10-05 10:02 | +15 | ETH | UP | 0.69 | open |  |
| 10-05 10:02 | +10 | ETH | UP | 0.69 | open |  |
| 10-05 10:02 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 10-05 10:02 | +10 stop | XRP | UP | 0.60 | 0.73 | 0.99 |
| 10-05 10:02 | +20 | XRP | UP | 0.60 | 0.84 | 2.13 |
| 10-05 10:02 | +15 | XRP | UP | 0.60 | 0.77 | 1.40 |
| 10-05 10:02 | +10 | XRP | UP | 0.60 | 0.73 | 0.99 |
| 10-05 10:02 | +5 | XRP | UP | 0.60 | 0.73 | 0.99 |
| 10-05 10:02 | +10 stop | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 10:02 | +20 | SOL | UP | 0.61 | open |  |
| 10-05 10:02 | +15 | SOL | UP | 0.61 | open |  |
| 10-05 10:02 | +10 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 10:02 | +5 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 10:01 | +5 | DOGE | DOWN | 0.51 | 0.57 | 0.24 |
| 10-05 10:01 | +10 stop | BNB | DOWN | 0.55 | 0.36 | -2.29 |
| 10-05 10:01 | +20 | BNB | DOWN | 0.55 | open |  |
| 10-05 10:01 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-05 10:01 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-05 10:01 | +5 | BNB | DOWN | 0.57 | open |  |
| 10-05 10:00 | +10 stop | DOGE | DOWN | 0.61 | 0.46 | -1.86 |
| 10-05 10:00 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-05 10:00 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-05 10:00 | +10 | DOGE | DOWN | 0.61 | open |  |
| 10-05 10:00 | +5 | DOGE | DOWN | 0.61 | 0.70 | 0.56 |
| 10-05 09:58 | +10 stop | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-05 09:58 | +10 | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
