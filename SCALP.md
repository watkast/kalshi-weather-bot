# Range-Scalp Bot

*Updated Thu Oct 22 03:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28175 | 24555 | 3620 (39) | 3 | $-8064.67 | -4.5% |
| **+10¢** | 21155 | 16972 | 4183 (55) | 6 | $-7117.02 | -5.3% |
| **+15¢** | 17717 | 13218 | 4499 (78) | 8 | $-6328.01 | -5.7% |
| **+20¢** | 15679 | 10962 | 4717 (98) | 8 | $-5684.58 | -5.8% |
| **+10¢ (15¢ stop)** | 34578 | 34519 | 59 (32) | 0 | $-12925.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 03:11 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.78 |
| 10-22 03:10 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 03:10 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 03:10 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 03:10 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-22 03:09 | +10 stop | BNB | UP | 0.55 | 0.36 | -2.25 |
| 10-22 03:09 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.69 |
| 10-22 03:09 | +5 | NEAR | DOWN | 0.57 | 0.67 | 0.69 |
| 10-22 03:09 | +10 stop | SOL | DOWN | 0.58 | 0.35 | -2.64 |
| 10-22 03:09 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-22 03:08 | +5 | DOGE | DOWN | 0.69 | 0.83 | 1.11 |
| 10-22 03:08 | +10 stop | BNB | UP | 0.55 | 0.38 | -2.05 |
| 10-22 03:08 | +20 | BNB | UP | 0.55 | open |  |
| 10-22 03:08 | +15 | BNB | UP | 0.55 | open |  |
| 10-22 03:08 | +10 | BNB | UP | 0.55 | open |  |
| 10-22 03:08 | +5 | BNB | UP | 0.55 | open |  |
| 10-22 03:08 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 03:07 | +10 stop | SOL | UP | 0.62 | 0.39 | -2.64 |
| 10-22 03:07 | +20 | SOL | UP | 0.62 | open |  |
| 10-22 03:07 | +15 | SOL | UP | 0.62 | open |  |
| 10-22 03:07 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-22 03:07 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-22 03:07 | +10 stop | BTC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-22 03:07 | +10 stop | DOGE | UP | 0.53 | 0.35 | -2.14 |
| 10-22 03:07 | +15 | DOGE | UP | 0.53 | open |  |
| 10-22 03:07 | +10 | DOGE | UP | 0.53 | open |  |
| 10-22 03:07 | +5 | DOGE | UP | 0.53 | 0.62 | 0.55 |
| 10-22 03:07 | +5 | ETH | UP | 0.45 | 0.54 | 0.54 |
| 10-22 03:07 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-22 03:07 | +5 | NEAR | UP | 0.47 | 0.55 | 0.44 |
| 10-22 03:07 | +10 stop | ETH | UP | 0.58 | 0.37 | -2.45 |
| 10-22 03:07 | +10 | ETH | UP | 0.58 | open |  |
| 10-22 03:07 | +5 | ETH | UP | 0.58 | 0.67 | 0.56 |
| 10-22 03:05 | +10 stop | BNB | UP | 0.58 | 0.69 | 0.77 |
| 10-22 03:05 | +5 | BNB | UP | 0.57 | 0.69 | 0.87 |
| 10-22 03:05 | +10 stop | BTC | DOWN | 0.61 | 0.39 | -2.54 |
| 10-22 03:05 | +10 stop | XRP | DOWN | 0.62 | 0.40 | -2.54 |
| 10-22 03:05 | +10 stop | NEAR | UP | 0.55 | 0.39 | -1.95 |
| 10-22 03:05 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 10-22 03:05 | +20 | ETH | UP | 0.53 | open |  |
