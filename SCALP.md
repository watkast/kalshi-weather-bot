# Range-Scalp Bot

*Updated Sat Oct 03 10:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 574 | 494 | 80 (1) | 4 | $-204.51 | -5.6% |
| **+10¢** | 439 | 349 | 90 (2) | 6 | $-170.42 | -6.1% |
| **+15¢** | 371 | 275 | 96 (3) | 6 | $-156.42 | -6.7% |
| **+20¢** | 324 | 225 | 99 (3) | 7 | $-143.97 | -7.0% |
| **+10¢ (15¢ stop)** | 758 | 757 | 1 (1) | 3 | $-408.13 | -8.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 10:08 | +10 stop | HYPE | UP | 0.66 | open |  |
| 10-03 10:08 | +10 stop | DOGE | UP | 0.59 | open |  |
| 10-03 10:08 | +20 | DOGE | UP | 0.59 | open |  |
| 10-03 10:08 | +15 | DOGE | UP | 0.60 | open |  |
| 10-03 10:08 | +10 | DOGE | UP | 0.59 | open |  |
| 10-03 10:08 | +5 | DOGE | UP | 0.59 | 0.67 | 0.47 |
| 10-03 10:07 | +5 | SOL | UP | 0.69 | open |  |
| 10-03 10:05 | +10 stop | SOL | UP | 0.62 | open |  |
| 10-03 10:05 | +10 | SOL | UP | 0.62 | open |  |
| 10-03 10:05 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 10-03 10:05 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-03 10:05 | +10 stop | XRP | DOWN | 0.48 | 0.63 | 1.15 |
| 10-03 10:05 | +10 stop | ZEC | UP | 0.61 | 0.74 | 0.99 |
| 10-03 10:05 | +5 | ZEC | UP | 0.61 | 0.70 | 0.58 |
| 10-03 10:05 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-03 10:04 | +10 stop | ZEC | DOWN | 0.55 | 0.36 | -2.20 |
| 10-03 10:03 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-03 10:03 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-03 10:03 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 10-03 10:03 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 10-03 10:03 | +5 | XRP | DOWN | 0.59 | open |  |
| 10-03 10:02 | +10 stop | BNB | DOWN | 0.62 | 0.33 | -3.23 |
| 10-03 10:02 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-03 10:02 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-03 10:02 | +10 | BNB | DOWN | 0.62 | open |  |
| 10-03 10:02 | +5 | BNB | DOWN | 0.62 | open |  |
| 10-03 10:02 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 10-03 10:02 | +10 stop | HYPE | DOWN | 0.63 | 0.46 | -2.05 |
| 10-03 10:02 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-03 10:02 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-03 10:02 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-03 10:02 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-03 10:01 | +5 | DOGE | UP | 0.61 | 0.68 | 0.37 |
| 10-03 10:01 | +10 stop | XRP | DOWN | 0.57 | 0.41 | -1.95 |
| 10-03 10:01 | +20 | XRP | DOWN | 0.57 | open |  |
| 10-03 10:01 | +15 | XRP | DOWN | 0.57 | open |  |
| 10-03 10:01 | +10 | XRP | DOWN | 0.57 | open |  |
| 10-03 10:01 | +5 | XRP | DOWN | 0.57 | 0.63 | 0.25 |
| 10-03 10:01 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-03 10:01 | +20 | SOL | DOWN | 0.63 | open |  |
