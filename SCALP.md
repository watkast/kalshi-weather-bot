# Range-Scalp Bot

*Updated Thu Nov 26 02:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72254 | 63069 | 9185 (158) | 2 | $-19208.92 | -4.2% |
| **+10¢** | 53895 | 43169 | 10726 (203) | 2 | $-17800.79 | -5.3% |
| **+15¢** | 45122 | 33569 | 11553 (260) | 2 | $-15895.28 | -5.6% |
| **+20¢** | 40176 | 28008 | 12168 (326) | 2 | $-14291.58 | -5.7% |
| **+10¢ (15¢ stop)** | 87971 | 87762 | 209 (128) | 0 | $-32272.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 02:53 | +5 | DOGE | DOWN | 0.59 | 0.87 | 2.55 |
| 11-26 02:53 | +10 stop | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 11-26 02:51 | +10 stop | SOL | DOWN | 0.68 | 0.83 | 1.27 |
| 11-26 02:51 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.37 |
| 11-26 02:50 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.02 |
| 11-26 02:50 | +10 stop | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-26 02:50 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-26 02:50 | +5 | XRP | UP | 0.61 | open |  |
| 11-26 02:49 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.96 |
| 11-26 02:49 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 11-26 02:49 | +10 stop | ETH | UP | 0.61 | 0.45 | -1.95 |
| 11-26 02:48 | +5 | XRP | UP | 0.58 | 0.64 | 0.25 |
| 11-26 02:48 | +5 | SOL | UP | 0.64 | open |  |
| 11-26 02:47 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-26 02:47 | +10 stop | BTC | UP | 0.62 | 0.45 | -2.05 |
| 11-26 02:47 | +10 stop | BNB | UP | 0.65 | 0.47 | -2.14 |
| 11-26 02:47 | +10 stop | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 11-26 02:46 | +10 stop | XRP | UP | 0.66 | 0.49 | -2.04 |
| 11-26 02:46 | +20 | XRP | UP | 0.66 | open |  |
| 11-26 02:46 | +15 | XRP | UP | 0.66 | open |  |
| 11-26 02:46 | +10 | XRP | UP | 0.66 | open |  |
| 11-26 02:46 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 11-26 02:46 | +10 stop | SOL | UP | 0.66 | 0.40 | -2.93 |
| 11-26 02:46 | +20 | SOL | UP | 0.66 | open |  |
| 11-26 02:46 | +15 | SOL | UP | 0.66 | open |  |
| 11-26 02:46 | +10 | SOL | UP | 0.66 | open |  |
| 11-26 02:46 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 11-26 02:46 | +10 stop | DOGE | DOWN | 0.59 | 0.43 | -1.95 |
| 11-26 02:46 | +20 | DOGE | DOWN | 0.59 | 0.87 | 2.55 |
| 11-26 02:46 | +15 | DOGE | DOWN | 0.59 | 0.87 | 2.55 |
| 11-26 02:46 | +10 | DOGE | DOWN | 0.59 | 0.87 | 2.55 |
| 11-26 02:46 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-26 02:46 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-26 02:46 | +20 | ZEC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-26 02:46 | +15 | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-26 02:46 | +10 | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-26 02:46 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-26 02:46 | +10 stop | BNB | DOWN | 0.67 | 0.48 | -2.24 |
| 11-26 02:46 | +20 | BNB | DOWN | 0.66 | 0.94 | 2.58 |
| 11-26 02:46 | +15 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
