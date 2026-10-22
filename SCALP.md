# Range-Scalp Bot

*Updated Thu Oct 22 12:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28745 | 25052 | 3693 (39) | 5 | $-8237.73 | -4.5% |
| **+10¢** | 21578 | 17304 | 4274 (55) | 6 | $-7324.10 | -5.4% |
| **+15¢** | 18059 | 13464 | 4595 (78) | 7 | $-6534.98 | -5.8% |
| **+20¢** | 15976 | 11157 | 4819 (100) | 8 | $-5886.24 | -5.9% |
| **+10¢ (15¢ stop)** | 35261 | 35202 | 59 (32) | 0 | $-13204.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 12:57 | +10 stop | ZEC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-22 12:57 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-22 12:55 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-22 12:54 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 10-22 12:53 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-22 12:53 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-22 12:53 | +10 stop | ETH | UP | 0.68 | 0.52 | -1.94 |
| 10-22 12:53 | +20 | ETH | UP | 0.68 | open |  |
| 10-22 12:53 | +15 | ETH | UP | 0.68 | open |  |
| 10-22 12:53 | +10 | ETH | UP | 0.68 | open |  |
| 10-22 12:53 | +5 | ETH | UP | 0.68 | open |  |
| 10-22 12:52 | +10 stop | BNB | UP | 0.38 | 0.55 | 1.35 |
| 10-22 12:52 | +15 | BNB | UP | 0.38 | 0.55 | 1.35 |
| 10-22 12:52 | +10 | BNB | UP | 0.38 | 0.55 | 1.35 |
| 10-22 12:52 | +5 | BNB | UP | 0.38 | 0.55 | 1.35 |
| 10-22 12:51 | +10 stop | NEAR | DOWN | 0.71 | 0.83 | 0.95 |
| 10-22 12:51 | +10 stop | BTC | UP | 0.65 | 0.36 | -3.23 |
| 10-22 12:51 | +15 | BTC | UP | 0.65 | open |  |
| 10-22 12:51 | +10 | BTC | UP | 0.65 | open |  |
| 10-22 12:51 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 10-22 12:51 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.00 |
| 10-22 12:50 | +10 stop | DOGE | UP | 0.47 | 0.29 | -2.13 |
| 10-22 12:50 | +10 stop | NEAR | UP | 0.58 | 0.39 | -2.25 |
| 10-22 12:49 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-22 12:49 | +10 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-22 12:49 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-22 12:49 | +10 | BTC | UP | 0.64 | 0.80 | 1.31 |
| 10-22 12:48 | +10 stop | NEAR | UP | 0.65 | 0.46 | -2.24 |
| 10-22 12:48 | +15 | NEAR | UP | 0.65 | open |  |
| 10-22 12:48 | +10 | NEAR | UP | 0.65 | open |  |
| 10-22 12:48 | +5 | NEAR | UP | 0.65 | open |  |
| 10-22 12:48 | +5 | XRP | UP | 0.62 | open |  |
| 10-22 12:48 | +10 stop | DOGE | UP | 0.58 | 0.41 | -2.05 |
| 10-22 12:48 | +10 | DOGE | UP | 0.58 | open |  |
| 10-22 12:48 | +5 | DOGE | UP | 0.58 | open |  |
| 10-22 12:48 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 10-22 12:47 | +5 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-22 12:47 | +10 stop | ZEC | UP | 0.54 | 0.38 | -1.95 |
| 10-22 12:47 | +20 | ZEC | UP | 0.54 | open |  |
| 10-22 12:47 | +15 | ZEC | UP | 0.54 | open |  |
