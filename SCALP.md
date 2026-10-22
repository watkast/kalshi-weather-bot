# Range-Scalp Bot

*Updated Thu Oct 22 21:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29288 | 25494 | 3794 (39) | 7 | $-8625.98 | -4.7% |
| **+10¢** | 21971 | 17580 | 4391 (55) | 7 | $-7758.03 | -5.6% |
| **+15¢** | 18395 | 13678 | 4717 (78) | 7 | $-6950.75 | -6.0% |
| **+20¢** | 16284 | 11338 | 4946 (100) | 7 | $-6291.06 | -6.2% |
| **+10¢ (15¢ stop)** | 35957 | 35898 | 59 (32) | 1 | $-13560.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 21:42 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 10-22 21:40 | +10 stop | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-22 21:40 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-22 21:33 | +10 stop | ETH | DOWN | 0.50 | 0.65 | 1.16 |
| 10-22 21:33 | +10 stop | BTC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-22 21:32 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 10-22 21:32 | +10 stop | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 10-22 21:32 | +20 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 10-22 21:32 | +15 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 10-22 21:32 | +10 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 10-22 21:32 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 10-22 21:31 | +10 stop | HYPE | DOWN | 0.67 | 0.84 | 1.41 |
| 10-22 21:31 | +20 | HYPE | DOWN | 0.67 | 0.91 | 2.13 |
| 10-22 21:31 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.41 |
| 10-22 21:31 | +10 | HYPE | DOWN | 0.67 | 0.84 | 1.41 |
| 10-22 21:31 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.37 |
| 10-22 21:31 | +10 stop | ZEC | UP | 0.62 | 0.41 | -2.44 |
| 10-22 21:31 | +20 | ZEC | UP | 0.62 | open |  |
| 10-22 21:31 | +15 | ZEC | UP | 0.62 | open |  |
| 10-22 21:31 | +10 | ZEC | UP | 0.62 | open |  |
| 10-22 21:31 | +5 | ZEC | UP | 0.62 | open |  |
| 10-22 21:31 | +10 stop | NEAR | UP | 0.56 | 0.35 | -2.44 |
| 10-22 21:31 | +20 | NEAR | UP | 0.56 | open |  |
| 10-22 21:31 | +15 | NEAR | UP | 0.56 | open |  |
| 10-22 21:31 | +10 | NEAR | UP | 0.56 | open |  |
| 10-22 21:31 | +5 | NEAR | UP | 0.56 | open |  |
| 10-22 21:31 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 10-22 21:31 | +20 | DOGE | UP | 0.62 | open |  |
| 10-22 21:31 | +15 | DOGE | UP | 0.62 | open |  |
| 10-22 21:31 | +10 | DOGE | UP | 0.62 | open |  |
| 10-22 21:31 | +5 | DOGE | UP | 0.62 | open |  |
| 10-22 21:31 | +10 stop | BNB | UP | 0.59 | 0.31 | -3.12 |
| 10-22 21:31 | +20 | BNB | UP | 0.59 | open |  |
| 10-22 21:31 | +15 | BNB | UP | 0.59 | open |  |
| 10-22 21:31 | +10 | BNB | UP | 0.59 | open |  |
| 10-22 21:31 | +5 | BNB | UP | 0.59 | open |  |
| 10-22 21:31 | +10 stop | SOL | UP | 0.58 | 0.32 | -2.94 |
| 10-22 21:31 | +20 | SOL | UP | 0.58 | open |  |
| 10-22 21:31 | +15 | SOL | UP | 0.58 | open |  |
| 10-22 21:31 | +10 | SOL | UP | 0.58 | open |  |
