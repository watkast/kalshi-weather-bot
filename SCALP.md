# Range-Scalp Bot

*Updated Mon Oct 26 18:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35187 | 30719 | 4468 (43) | 0 | $-9766.45 | -4.4% |
| **+10¢** | 26332 | 21169 | 5163 (65) | 0 | $-8547.38 | -5.2% |
| **+15¢** | 22034 | 16476 | 5558 (89) | 0 | $-7637.31 | -5.5% |
| **+20¢** | 19538 | 13714 | 5824 (112) | 0 | $-6681.51 | -5.4% |
| **+10¢ (15¢ stop)** | 43109 | 43047 | 62 (33) | 0 | $-16362.34 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 17:58 | +10 stop | ZEC | DOWN | 0.68 | 0.90 | 1.99 |
| 10-26 17:58 | +10 stop | NEAR | UP | 0.54 | 0.65 | 0.76 |
| 10-26 17:58 | +20 | NEAR | UP | 0.54 | 0.74 | 1.68 |
| 10-26 17:58 | +15 | NEAR | UP | 0.54 | 0.74 | 1.68 |
| 10-26 17:58 | +10 | NEAR | UP | 0.53 | 0.65 | 0.86 |
| 10-26 17:58 | +5 | NEAR | UP | 0.54 | 0.65 | 0.76 |
| 10-26 17:57 | +10 stop | NEAR | DOWN | 0.40 | 0.67 | 2.37 |
| 10-26 17:57 | +20 | NEAR | DOWN | 0.40 | 0.67 | 2.37 |
| 10-26 17:57 | +15 | NEAR | DOWN | 0.40 | 0.67 | 2.37 |
| 10-26 17:57 | +10 | NEAR | DOWN | 0.40 | 0.67 | 2.37 |
| 10-26 17:57 | +5 | NEAR | DOWN | 0.42 | 0.67 | 2.16 |
| 10-26 17:56 | +10 stop | ZEC | DOWN | 0.58 | 0.39 | -2.25 |
| 10-26 17:56 | +10 stop | NEAR | UP | 0.48 | 0.58 | 0.64 |
| 10-26 17:56 | +20 | NEAR | UP | 0.48 | 0.71 | 1.97 |
| 10-26 17:56 | +15 | NEAR | UP | 0.48 | 0.71 | 1.97 |
| 10-26 17:56 | +10 | NEAR | UP | 0.48 | 0.58 | 0.64 |
| 10-26 17:56 | +5 | NEAR | UP | 0.48 | 0.58 | 0.64 |
| 10-26 17:55 | +5 | ZEC | UP | 0.67 | no | -6.86 |
| 10-26 17:55 | +10 stop | ZEC | UP | 0.71 | 0.56 | -1.83 |
| 10-26 17:55 | +20 | ZEC | UP | 0.71 | no | -7.25 |
| 10-26 17:55 | +15 | ZEC | UP | 0.71 | no | -7.25 |
| 10-26 17:55 | +10 | ZEC | UP | 0.71 | no | -7.25 |
| 10-26 17:54 | +10 stop | NEAR | DOWN | 0.58 | 0.32 | -2.94 |
| 10-26 17:54 | +10 stop | BNB | DOWN | 0.62 | 0.14 | -5.06 |
| 10-26 17:54 | +10 stop | DOGE | DOWN | 0.51 | 0.30 | -2.43 |
| 10-26 17:54 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-26 17:53 | +20 | HYPE | UP | 0.62 | 0.86 | 2.14 |
| 10-26 17:53 | +15 | HYPE | UP | 0.62 | 0.81 | 1.62 |
| 10-26 17:53 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 10-26 17:53 | +10 stop | BTC | DOWN | 0.60 | 0.25 | -3.81 |
| 10-26 17:53 | +10 stop | ETH | DOWN | 0.71 | 0.37 | -3.72 |
| 10-26 17:53 | +10 stop | SOL | DOWN | 0.62 | 0.47 | -1.85 |
| 10-26 17:53 | +10 stop | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-26 17:53 | +10 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-26 17:53 | +5 | HYPE | UP | 0.67 | 0.75 | 0.50 |
| 10-26 17:52 | +10 stop | DOGE | DOWN | 0.70 | 0.44 | -2.93 |
| 10-26 17:51 | +10 stop | HYPE | DOWN | 0.56 | 0.41 | -1.86 |
| 10-26 17:51 | +5 | HYPE | DOWN | 0.53 | 0.60 | 0.31 |
| 10-26 17:48 | +10 stop | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-26 17:47 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
