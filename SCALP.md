# Range-Scalp Bot

*Updated Thu Nov 26 13:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72753 | 63501 | 9252 (158) | 0 | $-19365.12 | -4.2% |
| **+10¢** | 54245 | 43441 | 10804 (203) | 1 | $-17968.89 | -5.3% |
| **+15¢** | 45422 | 33782 | 11640 (261) | 1 | $-16084.80 | -5.6% |
| **+20¢** | 40430 | 28173 | 12257 (327) | 1 | $-14480.92 | -5.7% |
| **+10¢ (15¢ stop)** | 88600 | 88391 | 209 (128) | 0 | $-32624.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 13:45 | +10 stop | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 11-26 13:45 | +20 | NEAR | DOWN | 0.54 | open |  |
| 11-26 13:45 | +15 | NEAR | DOWN | 0.54 | open |  |
| 11-26 13:45 | +10 | NEAR | DOWN | 0.55 | open |  |
| 11-26 13:45 | +5 | NEAR | DOWN | 0.55 | 0.64 | 0.55 |
| 11-26 13:43 | +10 stop | SOL | UP | 0.52 | 0.83 | 2.82 |
| 11-26 13:43 | +15 | SOL | UP | 0.52 | 0.83 | 2.82 |
| 11-26 13:43 | +10 | SOL | UP | 0.52 | 0.83 | 2.82 |
| 11-26 13:43 | +5 | SOL | UP | 0.52 | 0.59 | 0.35 |
| 11-26 13:42 | +10 stop | SOL | DOWN | 0.47 | 0.65 | 1.46 |
| 11-26 13:42 | +20 | SOL | DOWN | 0.47 | yes | -4.88 |
| 11-26 13:42 | +15 | SOL | DOWN | 0.47 | 0.65 | 1.46 |
| 11-26 13:42 | +10 | SOL | DOWN | 0.47 | 0.65 | 1.46 |
| 11-26 13:42 | +5 | SOL | DOWN | 0.47 | 0.65 | 1.46 |
| 11-26 13:41 | +10 stop | XRP | UP | 0.59 | 0.72 | 0.98 |
| 11-26 13:40 | +5 | BTC | DOWN | 0.59 | yes | -6.07 |
| 11-26 13:40 | +10 stop | BTC | DOWN | 0.62 | 0.40 | -2.54 |
| 11-26 13:40 | +5 | XRP | DOWN | 0.69 | yes | -7.05 |
| 11-26 13:39 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 11-26 13:39 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-26 13:39 | +5 | BNB | UP | 0.54 | 0.61 | 0.35 |
| 11-26 13:39 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 11-26 13:38 | +10 stop | BNB | UP | 0.61 | 0.77 | 1.30 |
| 11-26 13:38 | +15 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 11-26 13:38 | +10 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 11-26 13:38 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 11-26 13:38 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-26 13:37 | +10 stop | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 11-26 13:37 | +10 stop | BTC | UP | 0.68 | 0.51 | -2.04 |
| 11-26 13:37 | +10 stop | XRP | UP | 0.51 | 0.33 | -2.14 |
| 11-26 13:37 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-26 13:36 | +5 | BNB | UP | 0.71 | 0.79 | 0.53 |
| 11-26 13:36 | +10 stop | XRP | DOWN | 0.55 | 0.38 | -2.05 |
| 11-26 13:35 | +10 stop | ETH | DOWN | 0.66 | 0.51 | -1.84 |
| 11-26 13:35 | +10 stop | SOL | DOWN | 0.65 | 0.41 | -2.77 |
| 11-26 13:35 | +5 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 11-26 13:33 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 11-26 13:32 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-26 13:32 | +10 stop | BTC | UP | 0.55 | 0.69 | 1.07 |
| 11-26 13:32 | +10 stop | ETH | UP | 0.47 | 0.32 | -1.84 |
