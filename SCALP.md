# Range-Scalp Bot

*Updated Sun Nov 22 15:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68868 | 60106 | 8762 (142) | 4 | $-18453.10 | -4.3% |
| **+10¢** | 51389 | 41153 | 10236 (186) | 5 | $-17106.46 | -5.3% |
| **+15¢** | 43064 | 32027 | 11037 (237) | 5 | $-15372.51 | -5.7% |
| **+20¢** | 38339 | 26741 | 11598 (295) | 7 | $-13691.86 | -5.7% |
| **+10¢ (15¢ stop)** | 83841 | 83656 | 185 (116) | 3 | $-30863.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 15:07 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-22 15:07 | +5 | DOGE | DOWN | 0.67 | open |  |
| 11-22 15:07 | +10 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-22 15:07 | +5 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-22 15:06 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 11-22 15:06 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 11-22 15:06 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-22 15:06 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 11-22 15:06 | +10 stop | ETH | UP | 0.56 | 0.39 | -2.05 |
| 11-22 15:05 | +10 stop | SOL | UP | 0.56 | 0.40 | -1.95 |
| 11-22 15:05 | +5 | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-22 15:05 | +10 stop | BNB | UP | 0.59 | 0.35 | -2.73 |
| 11-22 15:05 | +5 | ZEC | DOWN | 0.65 | 0.78 | 1.03 |
| 11-22 15:05 | +10 stop | DOGE | UP | 0.68 | 0.51 | -2.04 |
| 11-22 15:05 | +10 stop | NEAR | UP | 0.68 | 0.51 | -2.04 |
| 11-22 15:04 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.05 |
| 11-22 15:04 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
| 11-22 15:04 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-22 15:04 | +10 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-22 15:04 | +5 | XRP | DOWN | 0.59 | 0.68 | 0.57 |
| 11-22 15:04 | +10 stop | BTC | UP | 0.62 | 0.75 | 0.99 |
| 11-22 15:04 | +10 stop | ETH | UP | 0.47 | 0.59 | 0.85 |
| 11-22 15:03 | +10 stop | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 11-22 15:03 | +10 | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 11-22 15:03 | +10 stop | DOGE | UP | 0.50 | 0.70 | 1.67 |
| 11-22 15:03 | +10 stop | BTC | UP | 0.50 | 0.60 | 0.65 |
| 11-22 15:01 | +10 stop | NEAR | DOWN | 0.62 | 0.45 | -2.05 |
| 11-22 15:01 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-22 15:01 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-22 15:01 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-22 15:01 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-22 15:01 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 11-22 15:01 | +10 stop | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 11-22 15:01 | +20 | XRP | DOWN | 0.51 | 0.71 | 1.67 |
| 11-22 15:01 | +15 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 11-22 15:01 | +10 | XRP | DOWN | 0.51 | 0.63 | 0.85 |
| 11-22 15:01 | +5 | XRP | DOWN | 0.51 | 0.58 | 0.34 |
| 11-22 15:01 | +10 stop | DOGE | DOWN | 0.54 | 0.39 | -1.85 |
| 11-22 15:01 | +20 | DOGE | DOWN | 0.54 | open |  |
| 11-22 15:01 | +15 | DOGE | DOWN | 0.54 | open |  |
