# Range-Scalp Bot

*Updated Sun Nov 22 23:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69212 | 60389 | 8823 (145) | 7 | $-18652.08 | -4.3% |
| **+10¢** | 51651 | 41350 | 10301 (188) | 9 | $-17301.02 | -5.3% |
| **+15¢** | 43286 | 32183 | 11103 (241) | 9 | $-15510.35 | -5.7% |
| **+20¢** | 38550 | 26882 | 11668 (300) | 9 | $-13792.97 | -5.7% |
| **+10¢ (15¢ stop)** | 84301 | 84112 | 189 (117) | 5 | $-31038.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 23:12 | +10 stop | HYPE | UP | 0.66 | open |  |
| 11-22 23:12 | +15 | HYPE | UP | 0.66 | open |  |
| 11-22 23:12 | +10 | HYPE | UP | 0.70 | open |  |
| 11-22 23:12 | +5 | HYPE | UP | 0.70 | open |  |
| 11-22 23:12 | +10 stop | SOL | UP | 0.52 | open |  |
| 11-22 23:12 | +10 stop | ETH | DOWN | 0.67 | open |  |
| 11-22 23:11 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-22 23:11 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-22 23:11 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.48 |
| 11-22 23:11 | +10 stop | NEAR | DOWN | 0.60 | 0.79 | 1.62 |
| 11-22 23:11 | +10 stop | BNB | DOWN | 0.56 | open |  |
| 11-22 23:11 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-22 23:11 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-22 23:11 | +10 stop | XRP | UP | 0.64 | open |  |
| 11-22 23:11 | +20 | XRP | UP | 0.64 | open |  |
| 11-22 23:11 | +15 | XRP | UP | 0.64 | open |  |
| 11-22 23:11 | +10 | XRP | UP | 0.63 | open |  |
| 11-22 23:11 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 11-22 23:11 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.92 |
| 11-22 23:11 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-22 23:10 | +5 | SOL | DOWN | 0.52 | open |  |
| 11-22 23:10 | +5 | HYPE | UP | 0.69 | 0.76 | 0.42 |
| 11-22 23:10 | +10 stop | XRP | UP | 0.42 | 0.65 | 1.96 |
| 11-22 23:10 | +20 | XRP | UP | 0.42 | 0.65 | 1.96 |
| 11-22 23:10 | +15 | XRP | UP | 0.44 | 0.65 | 1.76 |
| 11-22 23:10 | +10 | XRP | UP | 0.45 | 0.65 | 1.66 |
| 11-22 23:10 | +5 | XRP | UP | 0.46 | 0.65 | 1.56 |
| 11-22 23:09 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 11-22 23:09 | +10 stop | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 11-22 23:09 | +10 stop | SOL | DOWN | 0.50 | 0.63 | 0.95 |
| 11-22 23:09 | +20 | SOL | DOWN | 0.50 | open |  |
| 11-22 23:09 | +15 | SOL | DOWN | 0.50 | open |  |
| 11-22 23:09 | +10 | SOL | DOWN | 0.50 | 0.63 | 0.95 |
| 11-22 23:09 | +5 | SOL | DOWN | 0.51 | 0.58 | 0.34 |
| 11-22 23:09 | +10 stop | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 11-22 23:09 | +20 | HYPE | UP | 0.66 | open |  |
| 11-22 23:09 | +15 | HYPE | UP | 0.66 | 0.82 | 1.33 |
| 11-22 23:09 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 11-22 23:09 | +5 | HYPE | UP | 0.66 | 0.73 | 0.40 |
| 11-22 23:08 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
