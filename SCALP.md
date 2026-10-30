# Range-Scalp Bot

*Updated Fri Oct 30 10:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40622 | 35455 | 5167 (51) | 1 | $-11351.32 | -4.4% |
| **+10¢** | 30268 | 24293 | 5975 (74) | 1 | $-10103.19 | -5.3% |
| **+15¢** | 25308 | 18877 | 6431 (101) | 3 | $-9121.38 | -5.7% |
| **+20¢** | 22461 | 15719 | 6742 (131) | 4 | $-8051.31 | -5.7% |
| **+10¢ (15¢ stop)** | 49533 | 49463 | 70 (37) | 1 | $-18756.11 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 10:32 | +5 | NEAR | UP | 0.61 | open |  |
| 10-30 10:31 | +10 stop | HYPE | UP | 0.56 | 0.69 | 0.97 |
| 10-30 10:31 | +20 | HYPE | UP | 0.56 | 0.79 | 1.96 |
| 10-30 10:31 | +15 | HYPE | UP | 0.55 | 0.79 | 2.10 |
| 10-30 10:31 | +10 | HYPE | UP | 0.55 | 0.69 | 1.07 |
| 10-30 10:31 | +5 | HYPE | UP | 0.55 | 0.69 | 1.07 |
| 10-30 10:31 | +10 stop | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-30 10:31 | +20 | BNB | UP | 0.53 | open |  |
| 10-30 10:31 | +15 | BNB | UP | 0.53 | open |  |
| 10-30 10:31 | +10 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-30 10:31 | +5 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-30 10:31 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-30 10:31 | +20 | BTC | UP | 0.69 | open |  |
| 10-30 10:31 | +15 | BTC | UP | 0.69 | 0.87 | 1.57 |
| 10-30 10:31 | +10 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-30 10:31 | +5 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-30 10:31 | +10 stop | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 10-30 10:31 | +20 | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 10-30 10:31 | +15 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 10-30 10:31 | +10 | DOGE | UP | 0.66 | 0.83 | 1.44 |
| 10-30 10:31 | +5 | DOGE | UP | 0.66 | 0.75 | 0.60 |
| 10-30 10:31 | +10 stop | NEAR | UP | 0.60 | open |  |
| 10-30 10:31 | +20 | NEAR | UP | 0.60 | open |  |
| 10-30 10:31 | +15 | NEAR | UP | 0.60 | open |  |
| 10-30 10:31 | +10 | NEAR | UP | 0.60 | open |  |
| 10-30 10:31 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 10-30 10:30 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-30 10:30 | +20 | SOL | UP | 0.70 | open |  |
| 10-30 10:30 | +15 | SOL | UP | 0.70 | open |  |
| 10-30 10:30 | +10 | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-30 10:30 | +5 | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-30 10:28 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.12 |
| 10-30 10:27 | +10 stop | XRP | UP | 0.59 | 0.38 | -2.44 |
| 10-30 10:27 | +20 | XRP | UP | 0.59 | 0.87 | 2.55 |
| 10-30 10:27 | +15 | XRP | UP | 0.59 | 0.87 | 2.55 |
| 10-30 10:27 | +10 | XRP | UP | 0.59 | 0.87 | 2.55 |
| 10-30 10:27 | +5 | XRP | UP | 0.59 | 0.67 | 0.47 |
| 10-30 10:27 | +10 stop | BTC | UP | 0.31 | 0.58 | 2.37 |
| 10-30 10:27 | +5 | BTC | UP | 0.29 | 0.58 | 2.57 |
| 10-30 10:23 | +10 stop | ETH | DOWN | 0.53 | 0.20 | -3.60 |
