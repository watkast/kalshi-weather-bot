# Range-Scalp Bot

*Updated Wed Nov 25 19:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71962 | 62806 | 9156 (158) | 3 | $-19194.61 | -4.2% |
| **+10¢** | 53691 | 42999 | 10692 (203) | 3 | $-17785.56 | -5.3% |
| **+15¢** | 44962 | 33445 | 11517 (260) | 3 | $-15877.98 | -5.6% |
| **+20¢** | 40033 | 27903 | 12130 (326) | 3 | $-14278.56 | -5.7% |
| **+10¢ (15¢ stop)** | 87612 | 87403 | 209 (128) | 3 | $-32138.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 19:16 | +10 stop | NEAR | UP | 0.71 | open |  |
| 11-25 19:16 | +20 | NEAR | UP | 0.71 | open |  |
| 11-25 19:16 | +15 | NEAR | UP | 0.71 | open |  |
| 11-25 19:16 | +10 | NEAR | UP | 0.71 | open |  |
| 11-25 19:16 | +5 | NEAR | UP | 0.71 | open |  |
| 11-25 19:15 | +10 stop | HYPE | UP | 0.67 | open |  |
| 11-25 19:15 | +20 | HYPE | UP | 0.67 | open |  |
| 11-25 19:15 | +15 | HYPE | UP | 0.67 | open |  |
| 11-25 19:15 | +10 | HYPE | UP | 0.68 | open |  |
| 11-25 19:15 | +5 | HYPE | UP | 0.68 | open |  |
| 11-25 19:15 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-25 19:15 | +20 | BNB | UP | 0.71 | open |  |
| 11-25 19:15 | +15 | BNB | UP | 0.71 | open |  |
| 11-25 19:15 | +10 | BNB | UP | 0.71 | open |  |
| 11-25 19:15 | +5 | BNB | UP | 0.70 | open |  |
| 11-25 19:08 | +10 stop | SOL | UP | 0.69 | 0.89 | 1.78 |
| 11-25 19:08 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 11-25 19:08 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-25 19:08 | +10 stop | NEAR | UP | 0.59 | 0.80 | 1.80 |
| 11-25 19:07 | +10 stop | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 11-25 19:04 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-25 19:03 | +10 stop | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-25 19:03 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-25 19:03 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-25 19:03 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-25 19:03 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-25 19:03 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-25 19:02 | +10 stop | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 11-25 19:01 | +5 | DOGE | DOWN | 0.55 | yes | -5.68 |
| 11-25 19:01 | +10 stop | HYPE | DOWN | 0.51 | 0.29 | -2.53 |
| 11-25 19:01 | +20 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 11-25 19:01 | +15 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 11-25 19:01 | +10 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 11-25 19:01 | +5 | HYPE | DOWN | 0.51 | yes | -5.28 |
| 11-25 19:01 | +10 stop | XRP | DOWN | 0.50 | 0.30 | -2.33 |
| 11-25 19:01 | +20 | XRP | DOWN | 0.50 | yes | -5.18 |
| 11-25 19:01 | +15 | XRP | DOWN | 0.52 | yes | -5.38 |
| 11-25 19:01 | +10 | XRP | DOWN | 0.52 | yes | -5.38 |
| 11-25 19:01 | +5 | XRP | DOWN | 0.53 | yes | -5.48 |
| 11-25 19:01 | +10 stop | SOL | DOWN | 0.61 | 0.41 | -2.34 |
