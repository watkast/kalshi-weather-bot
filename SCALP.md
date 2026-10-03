# Range-Scalp Bot

*Updated Sat Oct 03 12:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 727 | 631 | 96 (1) | 2 | $-221.36 | -4.8% |
| **+10¢** | 553 | 447 | 106 (2) | 2 | $-163.25 | -4.7% |
| **+15¢** | 469 | 355 | 114 (3) | 2 | $-147.20 | -5.0% |
| **+20¢** | 409 | 289 | 120 (3) | 2 | $-147.62 | -5.7% |
| **+10¢ (15¢ stop)** | 935 | 934 | 1 (1) | 1 | $-512.20 | -8.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 12:08 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-03 12:08 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-03 12:06 | +10 stop | NEAR | DOWN | 0.71 | 0.55 | -1.92 |
| 10-03 12:05 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 10-03 12:03 | +5 | ETH | UP | 0.70 | open |  |
| 10-03 12:03 | +10 stop | NEAR | UP | 0.66 | 0.20 | -4.88 |
| 10-03 12:03 | +5 | NEAR | UP | 0.66 | open |  |
| 10-03 12:03 | +5 | HYPE | UP | 0.63 | 0.85 | 1.90 |
| 10-03 12:02 | +10 stop | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-03 12:02 | +20 | XRP | UP | 0.71 | 0.92 | 1.89 |
| 10-03 12:02 | +15 | XRP | UP | 0.71 | 0.89 | 1.58 |
| 10-03 12:02 | +10 | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-03 12:02 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 10-03 12:02 | +5 | NEAR | UP | 0.53 | 0.60 | 0.35 |
| 10-03 12:02 | +5 | HYPE | UP | 0.55 | 0.67 | 0.91 |
| 10-03 12:02 | +10 stop | HYPE | UP | 0.58 | 0.85 | 2.44 |
| 10-03 12:02 | +20 | HYPE | UP | 0.58 | 0.85 | 2.44 |
| 10-03 12:02 | +15 | HYPE | UP | 0.58 | 0.85 | 2.44 |
| 10-03 12:02 | +10 | HYPE | UP | 0.58 | 0.85 | 2.44 |
| 10-03 12:02 | +5 | HYPE | UP | 0.58 | 0.65 | 0.37 |
| 10-03 12:01 | +10 stop | NEAR | UP | 0.70 | 0.49 | -2.43 |
| 10-03 12:01 | +20 | NEAR | UP | 0.70 | open |  |
| 10-03 12:01 | +15 | NEAR | UP | 0.66 | open |  |
| 10-03 12:01 | +10 | NEAR | UP | 0.66 | open |  |
| 10-03 12:01 | +5 | NEAR | UP | 0.66 | 0.73 | 0.40 |
| 10-03 12:01 | +10 stop | ETH | UP | 0.62 | 0.16 | -4.87 |
| 10-03 12:01 | +20 | ETH | UP | 0.62 | open |  |
| 10-03 12:01 | +15 | ETH | UP | 0.62 | open |  |
| 10-03 12:01 | +10 | ETH | UP | 0.62 | open |  |
| 10-03 12:01 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 10-03 11:58 | +10 stop | BNB | DOWN | 0.69 | 0.01 | -6.97 |
| 10-03 11:57 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 10-03 11:56 | +5 | ZEC | UP | 0.61 | no | -6.23 |
| 10-03 11:56 | +10 stop | ZEC | UP | 0.62 | 0.01 | -6.33 |
| 10-03 11:54 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-03 11:54 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.76 |
| 10-03 11:54 | +20 | DOGE | UP | 0.67 | no | -6.81 |
| 10-03 11:54 | +15 | DOGE | UP | 0.67 | no | -6.83 |
| 10-03 11:54 | +10 | DOGE | UP | 0.67 | 0.77 | 0.74 |
| 10-03 11:54 | +5 | DOGE | UP | 0.67 | 0.77 | 0.74 |
