# Range-Scalp Bot

*Updated Thu Oct 22 15:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28873 | 25154 | 3719 (39) | 1 | $-8341.13 | -4.6% |
| **+10¢** | 21671 | 17370 | 4301 (55) | 1 | $-7423.44 | -5.4% |
| **+15¢** | 18141 | 13516 | 4625 (78) | 1 | $-6639.26 | -5.8% |
| **+20¢** | 16054 | 11204 | 4850 (100) | 0 | $-5982.49 | -5.9% |
| **+10¢ (15¢ stop)** | 35427 | 35368 | 59 (32) | 0 | $-13295.01 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 14:55 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-22 14:55 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.93 |
| 10-22 14:55 | +15 | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 10-22 14:55 | +10 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-22 14:55 | +5 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-22 14:53 | +10 stop | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 10-22 14:53 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-22 14:52 | +5 | BNB | UP | 0.49 | open |  |
| 10-22 14:52 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-22 14:52 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-22 14:52 | +10 stop | BNB | UP | 0.51 | 0.32 | -2.28 |
| 10-22 14:52 | +15 | BNB | UP | 0.51 | open |  |
| 10-22 14:52 | +10 | BNB | UP | 0.51 | open |  |
| 10-22 14:52 | +5 | BNB | UP | 0.51 | 0.60 | 0.51 |
| 10-22 14:52 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-22 14:52 | +20 | HYPE | DOWN | 0.68 | 0.94 | 2.37 |
| 10-22 14:52 | +15 | HYPE | DOWN | 0.68 | 0.86 | 1.51 |
| 10-22 14:52 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-22 14:52 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.47 |
| 10-22 14:52 | +10 stop | BTC | DOWN | 0.50 | 0.70 | 1.67 |
| 10-22 14:52 | +20 | BTC | DOWN | 0.50 | 0.70 | 1.67 |
| 10-22 14:52 | +15 | BTC | DOWN | 0.50 | 0.70 | 1.67 |
| 10-22 14:52 | +10 | BTC | DOWN | 0.50 | 0.70 | 1.67 |
| 10-22 14:52 | +5 | BTC | DOWN | 0.49 | 0.58 | 0.54 |
| 10-22 14:47 | +10 stop | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 14:47 | +20 | BNB | DOWN | 0.68 | 0.90 | 1.97 |
| 10-22 14:47 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 10-22 14:47 | +10 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 14:47 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-22 14:41 | +10 stop | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 14:41 | +20 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-22 14:41 | +15 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 14:41 | +10 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 14:41 | +5 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-22 14:41 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-22 14:41 | +15 | NEAR | UP | 0.66 | 0.91 | 2.22 |
| 10-22 14:40 | +10 stop | NEAR | UP | 0.48 | 0.59 | 0.75 |
| 10-22 14:39 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-22 14:39 | +10 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-22 14:39 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.02 |
