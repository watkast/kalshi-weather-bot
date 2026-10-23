# Range-Scalp Bot

*Updated Fri Oct 23 08:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29990 | 26110 | 3880 (39) | 0 | $-8815.52 | -4.7% |
| **+10¢** | 22482 | 17989 | 4493 (55) | 0 | $-7932.89 | -5.6% |
| **+15¢** | 18827 | 13998 | 4829 (78) | 1 | $-7142.31 | -6.0% |
| **+20¢** | 16667 | 11609 | 5058 (101) | 2 | $-6434.64 | -6.1% |
| **+10¢ (15¢ stop)** | 36795 | 36736 | 59 (32) | 0 | $-13828.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 08:15 | +10 stop | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-23 08:15 | +20 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-23 08:15 | +15 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-23 08:15 | +10 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-23 08:15 | +5 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-23 08:15 | +10 stop | BNB | UP | 0.69 | 0.82 | 1.04 |
| 10-23 08:15 | +20 | BNB | UP | 0.69 | open |  |
| 10-23 08:15 | +15 | BNB | UP | 0.69 | open |  |
| 10-23 08:15 | +10 | BNB | UP | 0.69 | 0.82 | 1.01 |
| 10-23 08:15 | +5 | BNB | UP | 0.69 | 0.82 | 1.01 |
| 10-23 08:15 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-23 08:15 | +20 | SOL | UP | 0.70 | open |  |
| 10-23 08:15 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 08:15 | +10 | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-23 08:15 | +5 | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-23 08:11 | +10 stop | HYPE | UP | 0.56 | 0.78 | 1.90 |
| 10-23 08:11 | +5 | HYPE | UP | 0.56 | 0.65 | 0.57 |
| 10-23 08:09 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-23 08:09 | +5 | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-23 08:08 | +10 stop | XRP | UP | 0.65 | 0.78 | 1.01 |
| 10-23 08:08 | +10 stop | XRP | UP | 0.44 | 0.54 | 0.64 |
| 10-23 08:06 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.69 |
| 10-23 08:06 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-23 08:06 | +5 | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-23 08:05 | +10 stop | XRP | UP | 0.67 | 0.52 | -1.84 |
| 10-23 08:05 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-23 08:05 | +10 stop | XRP | DOWN | 0.49 | 0.59 | 0.65 |
| 10-23 08:04 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 10-23 08:04 | +5 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 10-23 08:04 | +10 stop | BTC | UP | 0.55 | 0.68 | 0.96 |
| 10-23 08:04 | +10 stop | NEAR | UP | 0.55 | 0.65 | 0.66 |
| 10-23 08:04 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.71 |
| 10-23 08:03 | +5 | BNB | UP | 0.61 | 0.73 | 0.89 |
| 10-23 08:02 | +10 stop | XRP | UP | 0.64 | 0.46 | -2.15 |
| 10-23 08:02 | +5 | DOGE | UP | 0.71 | 0.76 | 0.25 |
| 10-23 08:01 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-23 08:01 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-23 08:01 | +5 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-23 08:01 | +10 stop | BNB | UP | 0.57 | 0.73 | 1.28 |
| 10-23 08:01 | +20 | BNB | UP | 0.57 | 0.82 | 2.21 |
