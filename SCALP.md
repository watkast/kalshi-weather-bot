# Range-Scalp Bot

*Updated Mon Oct 19 14:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24127 | 20980 | 3147 (31) | 0 | $-7186.41 | -4.7% |
| **+10¢** | 18157 | 14526 | 3631 (46) | 0 | $-6411.59 | -5.6% |
| **+15¢** | 15215 | 11304 | 3911 (69) | 1 | $-5799.79 | -6.1% |
| **+20¢** | 13467 | 9375 | 4092 (87) | 1 | $-5176.60 | -6.1% |
| **+10¢ (15¢ stop)** | 29706 | 29654 | 52 (30) | 0 | $-11280.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 14:31 | +10 stop | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 10-19 14:31 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-19 14:31 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-19 14:31 | +10 | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 10-19 14:31 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-19 14:26 | +10 stop | NEAR | DOWN | 0.68 | 0.49 | -2.24 |
| 10-19 14:26 | +10 stop | HYPE | DOWN | 0.52 | 0.67 | 1.16 |
| 10-19 14:26 | +5 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-19 14:25 | +10 stop | NEAR | UP | 0.52 | 0.32 | -2.34 |
| 10-19 14:25 | +20 | NEAR | UP | 0.52 | no | -5.38 |
| 10-19 14:25 | +15 | NEAR | UP | 0.52 | no | -5.38 |
| 10-19 14:25 | +10 | NEAR | UP | 0.52 | no | -5.38 |
| 10-19 14:25 | +5 | NEAR | UP | 0.52 | 0.59 | 0.35 |
| 10-19 14:25 | +10 stop | BTC | DOWN | 0.65 | 0.86 | 1.85 |
| 10-19 14:25 | +10 stop | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 10-19 14:25 | +5 | BNB | UP | 0.51 | no | -5.28 |
| 10-19 14:24 | +10 stop | BNB | UP | 0.55 | 0.28 | -3.03 |
| 10-19 14:24 | +20 | BNB | UP | 0.55 | no | -5.68 |
| 10-19 14:24 | +15 | BNB | UP | 0.55 | no | -5.68 |
| 10-19 14:24 | +10 | BNB | UP | 0.55 | no | -5.68 |
| 10-19 14:24 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 10-19 14:24 | +10 stop | ZEC | UP | 0.59 | 0.44 | -1.85 |
| 10-19 14:24 | +20 | ZEC | UP | 0.60 | no | -6.14 |
| 10-19 14:24 | +15 | ZEC | UP | 0.60 | no | -6.17 |
| 10-19 14:24 | +10 | ZEC | UP | 0.60 | no | -6.17 |
| 10-19 14:24 | +5 | ZEC | UP | 0.58 | no | -5.97 |
| 10-19 14:24 | +10 stop | DOGE | DOWN | 0.71 | 0.91 | 1.83 |
| 10-19 14:24 | +10 stop | HYPE | UP | 0.60 | 0.38 | -2.56 |
| 10-19 14:23 | +10 stop | BTC | UP | 0.67 | 0.50 | -2.04 |
| 10-19 14:23 | +10 | BTC | UP | 0.67 | no | -6.86 |
| 10-19 14:23 | +5 | BTC | UP | 0.67 | no | -6.86 |
| 10-19 14:23 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 10-19 14:23 | +10 stop | ETH | DOWN | 0.59 | 0.78 | 1.60 |
| 10-19 14:23 | +10 stop | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 10-19 14:23 | +10 stop | BTC | UP | 0.59 | 0.72 | 0.98 |
| 10-19 14:23 | +20 | BTC | UP | 0.59 | no | -6.07 |
| 10-19 14:23 | +15 | BTC | UP | 0.59 | no | -6.07 |
| 10-19 14:23 | +10 | BTC | UP | 0.59 | 0.72 | 0.98 |
| 10-19 14:23 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 10-19 14:23 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
