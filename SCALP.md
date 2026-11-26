# Range-Scalp Bot

*Updated Thu Nov 26 12:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72639 | 63413 | 9226 (158) | 0 | $-19250.93 | -4.2% |
| **+10¢** | 54171 | 43397 | 10774 (203) | 2 | $-17831.33 | -5.2% |
| **+15¢** | 45357 | 33749 | 11608 (261) | 3 | $-15938.70 | -5.6% |
| **+20¢** | 40371 | 28148 | 12223 (327) | 3 | $-14322.09 | -5.7% |
| **+10¢ (15¢ stop)** | 88443 | 88234 | 209 (128) | 0 | $-32477.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 12:12 | +10 stop | SOL | UP | 0.60 | 0.45 | -1.85 |
| 11-26 12:12 | +10 | SOL | UP | 0.58 | open |  |
| 11-26 12:12 | +5 | SOL | UP | 0.58 | 0.63 | 0.15 |
| 11-26 12:12 | +20 | SOL | UP | 0.71 | open |  |
| 11-26 12:12 | +15 | SOL | UP | 0.70 | open |  |
| 11-26 12:11 | +10 stop | DOGE | UP | 0.58 | 0.42 | -1.96 |
| 11-26 12:11 | +20 | DOGE | UP | 0.58 | open |  |
| 11-26 12:11 | +15 | DOGE | UP | 0.58 | open |  |
| 11-26 12:11 | +10 | DOGE | UP | 0.58 | open |  |
| 11-26 12:11 | +5 | DOGE | UP | 0.58 | 0.63 | 0.15 |
| 11-26 12:09 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-26 12:09 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-26 12:09 | +5 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-26 12:08 | +10 stop | HYPE | UP | 0.51 | 0.62 | 0.73 |
| 11-26 12:08 | +20 | HYPE | UP | 0.51 | open |  |
| 11-26 12:08 | +15 | HYPE | UP | 0.51 | open |  |
| 11-26 12:08 | +10 | HYPE | UP | 0.51 | 0.62 | 0.73 |
| 11-26 12:08 | +5 | HYPE | UP | 0.51 | 0.62 | 0.73 |
| 11-26 11:58 | +5 | NEAR | DOWN | 0.41 | 0.62 | 1.76 |
| 11-26 11:58 | +10 stop | BNB | DOWN | 0.54 | 0.84 | 2.72 |
| 11-26 11:58 | +15 | BNB | DOWN | 0.59 | 0.84 | 2.23 |
| 11-26 11:58 | +10 | BNB | DOWN | 0.59 | 0.84 | 2.23 |
| 11-26 11:58 | +5 | BNB | DOWN | 0.58 | 0.84 | 2.32 |
| 11-26 11:57 | +10 stop | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 11-26 11:57 | +10 | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 11-26 11:57 | +5 | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 11-26 11:57 | +10 stop | NEAR | DOWN | 0.60 | 0.24 | -3.90 |
| 11-26 11:57 | +5 | NEAR | DOWN | 0.60 | 0.68 | 0.47 |
| 11-26 11:57 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 11-26 11:57 | +20 | ETH | DOWN | 0.62 | 0.88 | 2.35 |
| 11-26 11:57 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-26 11:57 | +10 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-26 11:57 | +5 | ETH | DOWN | 0.61 | 0.79 | 1.51 |
| 11-26 11:56 | +10 stop | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 11-26 11:56 | +10 | DOGE | DOWN | 0.47 | 0.62 | 1.15 |
| 11-26 11:56 | +5 | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 11-26 11:55 | +10 stop | BNB | DOWN | 0.54 | 0.76 | 1.89 |
| 11-26 11:54 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.71 |
| 11-26 11:54 | +10 stop | DOGE | UP | 0.54 | 0.30 | -2.73 |
| 11-26 11:54 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
