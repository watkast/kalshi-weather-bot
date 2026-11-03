# Range-Scalp Bot

*Updated Tue Nov 03 13:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46013 | 40065 | 5948 (70) | 0 | $-13263.54 | -4.6% |
| **+10¢** | 34349 | 27459 | 6890 (92) | 1 | $-12124.54 | -5.6% |
| **+15¢** | 28747 | 21339 | 7408 (120) | 1 | $-11072.03 | -6.1% |
| **+20¢** | 25533 | 17769 | 7764 (157) | 1 | $-9837.41 | -6.1% |
| **+10¢ (15¢ stop)** | 56120 | 56031 | 89 (53) | 1 | $-21030.49 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 13:30 | +20 | ETH | UP | 0.69 | open |  |
| 11-03 13:30 | +5 | ETH | UP | 0.69 | 0.75 | 0.31 |
| 11-03 13:30 | +10 stop | ETH | UP | 0.71 | open |  |
| 11-03 13:30 | +15 | ETH | UP | 0.70 | open |  |
| 11-03 13:30 | +10 | ETH | UP | 0.70 | open |  |
| 11-03 13:28 | +10 stop | DOGE | UP | 0.59 | 0.80 | 1.81 |
| 11-03 13:28 | +20 | DOGE | UP | 0.59 | 0.80 | 1.81 |
| 11-03 13:28 | +15 | DOGE | UP | 0.59 | 0.80 | 1.81 |
| 11-03 13:28 | +10 | DOGE | UP | 0.59 | 0.80 | 1.81 |
| 11-03 13:28 | +5 | DOGE | UP | 0.58 | 0.80 | 1.90 |
| 11-03 13:27 | +10 stop | HYPE | UP | 0.27 | 0.63 | 3.29 |
| 11-03 13:27 | +20 | HYPE | UP | 0.27 | 0.63 | 3.29 |
| 11-03 13:27 | +15 | HYPE | UP | 0.27 | 0.63 | 3.29 |
| 11-03 13:27 | +10 | HYPE | UP | 0.36 | 0.63 | 2.36 |
| 11-03 13:27 | +5 | HYPE | UP | 0.35 | 0.63 | 2.47 |
| 11-03 13:27 | +10 stop | BNB | UP | 0.35 | 0.64 | 2.57 |
| 11-03 13:27 | +10 stop | SOL | UP | 0.27 | 0.57 | 2.67 |
| 11-03 13:25 | +10 stop | ETH | DOWN | 0.60 | 0.22 | -4.10 |
| 11-03 13:23 | +5 | BTC | UP | 0.68 | 0.89 | 1.87 |
| 11-03 13:23 | +10 stop | ETH | DOWN | 0.53 | 0.69 | 1.27 |
| 11-03 13:23 | +10 stop | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-03 13:22 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-03 13:22 | +5 | BTC | UP | 0.57 | 0.65 | 0.46 |
| 11-03 13:21 | +5 | BTC | UP | 0.53 | 0.59 | 0.25 |
| 11-03 13:21 | +10 stop | BNB | UP | 0.56 | 0.39 | -2.05 |
| 11-03 13:21 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 11-03 13:21 | +10 | XRP | UP | 0.63 | 0.87 | 2.15 |
| 11-03 13:21 | +5 | XRP | UP | 0.63 | 0.71 | 0.48 |
| 11-03 13:21 | +10 stop | DOGE | DOWN | 0.48 | 0.59 | 0.75 |
| 11-03 13:21 | +5 | DOGE | DOWN | 0.48 | 0.59 | 0.75 |
| 11-03 13:20 | +10 stop | DOGE | UP | 0.57 | 0.41 | -1.95 |
| 11-03 13:20 | +20 | DOGE | UP | 0.57 | 0.91 | 3.17 |
| 11-03 13:20 | +15 | DOGE | UP | 0.57 | 0.91 | 3.17 |
| 11-03 13:20 | +10 | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 11-03 13:20 | +5 | DOGE | UP | 0.56 | 0.62 | 0.25 |
| 11-03 13:19 | +5 | NEAR | UP | 0.66 | yes | 3.24 |
| 11-03 13:19 | +5 | ETH | UP | 0.68 | 0.77 | 0.61 |
| 11-03 13:19 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-03 13:19 | +10 stop | BNB | UP | 0.71 | 0.54 | -2.03 |
| 11-03 13:19 | +5 | BNB | UP | 0.71 | 0.83 | 0.95 |
