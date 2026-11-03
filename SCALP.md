# Range-Scalp Bot

*Updated Tue Nov 03 04:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45566 | 39675 | 5891 (69) | 3 | $-13151.16 | -4.6% |
| **+10¢** | 34008 | 27180 | 6828 (91) | 7 | $-12056.57 | -5.6% |
| **+15¢** | 28456 | 21110 | 7346 (119) | 7 | $-11062.35 | -6.2% |
| **+20¢** | 25273 | 17576 | 7697 (154) | 7 | $-9847.08 | -6.2% |
| **+10¢ (15¢ stop)** | 55595 | 55506 | 89 (53) | 0 | $-20954.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 04:21 | +10 stop | SOL | DOWN | 0.67 | 0.48 | -2.24 |
| 11-03 04:21 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-03 04:21 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-03 04:21 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-03 04:21 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-03 04:21 | +10 stop | HYPE | UP | 0.52 | 0.71 | 1.57 |
| 11-03 04:20 | +5 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-03 04:20 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.27 |
| 11-03 04:20 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-03 04:19 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-03 04:19 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-03 04:18 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-03 04:18 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-03 04:18 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-03 04:18 | +10 stop | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 11-03 04:18 | +20 | NEAR | UP | 0.68 | 0.89 | 1.87 |
| 11-03 04:18 | +15 | NEAR | UP | 0.68 | 0.89 | 1.87 |
| 11-03 04:18 | +10 | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 11-03 04:18 | +5 | NEAR | UP | 0.68 | 0.76 | 0.51 |
| 11-03 04:18 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-03 04:18 | +5 | HYPE | UP | 0.65 | 0.71 | 0.29 |
| 11-03 04:18 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-03 04:18 | +10 stop | ETH | UP | 0.55 | 0.33 | -2.54 |
| 11-03 04:18 | +20 | ETH | UP | 0.55 | open |  |
| 11-03 04:18 | +15 | ETH | UP | 0.55 | open |  |
| 11-03 04:18 | +10 | ETH | UP | 0.55 | open |  |
| 11-03 04:18 | +5 | ETH | UP | 0.55 | open |  |
| 11-03 04:18 | +5 | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-03 04:16 | +10 stop | ZEC | UP | 0.58 | 0.37 | -2.45 |
| 11-03 04:16 | +20 | ZEC | UP | 0.58 | open |  |
| 11-03 04:16 | +15 | ZEC | UP | 0.58 | open |  |
| 11-03 04:16 | +10 | ZEC | UP | 0.58 | open |  |
| 11-03 04:16 | +5 | ZEC | UP | 0.58 | 0.66 | 0.46 |
| 11-03 04:16 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-03 04:16 | +20 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 11-03 04:16 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-03 04:16 | +10 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-03 04:16 | +5 | XRP | UP | 0.68 | 0.76 | 0.51 |
| 11-03 04:16 | +10 stop | DOGE | UP | 0.67 | 0.49 | -2.14 |
| 11-03 04:16 | +20 | DOGE | UP | 0.67 | open |  |
