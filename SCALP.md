# Range-Scalp Bot

*Updated Sat Nov 07 23:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51645 | 45031 | 6614 (80) | 2 | $-14325.26 | -4.4% |
| **+10¢** | 38536 | 30823 | 7713 (106) | 2 | $-13347.32 | -5.5% |
| **+15¢** | 32271 | 23958 | 8313 (135) | 2 | $-12249.32 | -6.1% |
| **+20¢** | 28705 | 19989 | 8716 (180) | 2 | $-10807.37 | -6.0% |
| **+10¢ (15¢ stop)** | 62889 | 62786 | 103 (61) | 0 | $-23298.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 23:11 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 11-07 23:09 | +10 stop | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 11-07 23:06 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-07 23:06 | +10 stop | DOGE | UP | 0.59 | 0.75 | 1.29 |
| 11-07 23:06 | +10 stop | ETH | DOWN | 0.65 | 0.50 | -1.84 |
| 11-07 23:06 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.80 |
| 11-07 23:06 | +20 | HYPE | UP | 0.67 | 0.93 | 2.42 |
| 11-07 23:06 | +15 | HYPE | UP | 0.67 | 0.85 | 1.54 |
| 11-07 23:06 | +10 | HYPE | UP | 0.67 | 0.78 | 0.80 |
| 11-07 23:06 | +5 | HYPE | UP | 0.67 | 0.74 | 0.39 |
| 11-07 23:05 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 11-07 23:05 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-07 23:04 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 23:04 | +10 stop | DOGE | UP | 0.66 | 0.50 | -1.94 |
| 11-07 23:04 | +10 stop | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-07 23:04 | +10 stop | XRP | UP | 0.58 | 0.39 | -2.25 |
| 11-07 23:03 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.04 |
| 11-07 23:02 | +20 | ZEC | DOWN | 0.54 | 0.76 | 1.89 |
| 11-07 23:02 | +15 | ZEC | DOWN | 0.54 | 0.76 | 1.89 |
| 11-07 23:02 | +10 stop | SOL | DOWN | 0.57 | 0.27 | -3.32 |
| 11-07 23:02 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:02 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:02 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:02 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:01 | +10 stop | XRP | DOWN | 0.63 | 0.45 | -2.15 |
| 11-07 23:01 | +20 | XRP | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 23:01 | +15 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 11-07 23:01 | +10 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 11-07 23:01 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-07 23:01 | +10 stop | BNB | DOWN | 0.69 | 0.48 | -2.43 |
| 11-07 23:01 | +20 | BNB | DOWN | 0.69 | 0.90 | 1.88 |
| 11-07 23:01 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-07 23:01 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-07 23:01 | +5 | BNB | DOWN | 0.69 | 0.75 | 0.31 |
| 11-07 23:01 | +10 stop | NEAR | UP | 0.61 | 0.77 | 1.25 |
| 11-07 23:01 | +20 | NEAR | UP | 0.61 | 0.88 | 2.45 |
| 11-07 23:01 | +15 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 11-07 23:01 | +10 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 11-07 23:01 | +5 | NEAR | UP | 0.60 | 0.69 | 0.53 |
| 11-07 23:01 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
