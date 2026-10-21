# Range-Scalp Bot

*Updated Wed Oct 21 00:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26454 | 23041 | 3413 (33) | 3 | $-7710.29 | -4.6% |
| **+10¢** | 19902 | 15962 | 3940 (48) | 3 | $-6793.72 | -5.4% |
| **+15¢** | 16657 | 12418 | 4239 (72) | 4 | $-6050.04 | -5.8% |
| **+20¢** | 14740 | 10294 | 4446 (91) | 5 | $-5449.01 | -5.9% |
| **+10¢ (15¢ stop)** | 32398 | 32345 | 53 (30) | 2 | $-11828.70 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 00:37 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 10-21 00:37 | +15 | DOGE | UP | 0.61 | open |  |
| 10-21 00:37 | +10 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 10-21 00:37 | +5 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 10-21 00:37 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 10-21 00:36 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-21 00:36 | +10 stop | XRP | DOWN | 0.69 | 0.53 | -1.93 |
| 10-21 00:36 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-21 00:36 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-21 00:36 | +10 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-21 00:36 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 10-21 00:35 | +5 | DOGE | UP | 0.65 | 0.71 | 0.29 |
| 10-21 00:35 | +10 stop | BTC | UP | 0.53 | 0.37 | -1.95 |
| 10-21 00:35 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-21 00:35 | +10 stop | SOL | UP | 0.62 | open |  |
| 10-21 00:35 | +5 | SOL | UP | 0.62 | open |  |
| 10-21 00:34 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-21 00:34 | +5 | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-21 00:34 | +10 stop | ETH | DOWN | 0.67 | 0.48 | -2.24 |
| 10-21 00:34 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-21 00:34 | +15 | ETH | DOWN | 0.67 | open |  |
| 10-21 00:34 | +10 | ETH | DOWN | 0.67 | open |  |
| 10-21 00:34 | +5 | ETH | DOWN | 0.67 | open |  |
| 10-21 00:33 | +10 stop | NEAR | UP | 0.47 | 0.59 | 0.85 |
| 10-21 00:33 | +20 | NEAR | UP | 0.47 | 0.72 | 2.17 |
| 10-21 00:33 | +15 | NEAR | UP | 0.47 | 0.72 | 2.17 |
| 10-21 00:33 | +10 | NEAR | UP | 0.47 | 0.59 | 0.85 |
| 10-21 00:33 | +5 | NEAR | UP | 0.47 | 0.56 | 0.54 |
| 10-21 00:33 | +5 | BNB | UP | 0.47 | 0.64 | 1.35 |
| 10-21 00:33 | +5 | SOL | UP | 0.31 | 0.58 | 2.37 |
| 10-21 00:33 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 10-21 00:32 | +10 stop | SOL | UP | 0.54 | 0.31 | -2.63 |
| 10-21 00:32 | +20 | SOL | UP | 0.54 | open |  |
| 10-21 00:32 | +15 | SOL | UP | 0.53 | open |  |
| 10-21 00:32 | +10 | SOL | UP | 0.54 | open |  |
| 10-21 00:32 | +5 | SOL | UP | 0.54 | 0.61 | 0.35 |
| 10-21 00:32 | +5 | ZEC | UP | 0.60 | 0.76 | 1.30 |
| 10-21 00:32 | +10 stop | DOGE | UP | 0.60 | 0.30 | -3.32 |
| 10-21 00:32 | +20 | DOGE | UP | 0.60 | open |  |
| 10-21 00:32 | +15 | DOGE | UP | 0.60 | 0.77 | 1.40 |
