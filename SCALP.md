# Range-Scalp Bot

*Updated Mon Oct 05 11:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3737 | 3217 | 520 (3) | 1 | $-1297.01 | -5.5% |
| **+10¢** | 2893 | 2295 | 598 (4) | 1 | $-1168.69 | -6.4% |
| **+15¢** | 2429 | 1800 | 629 (7) | 2 | $-1000.54 | -6.6% |
| **+20¢** | 2170 | 1515 | 655 (12) | 1 | $-829.23 | -6.1% |
| **+10¢ (15¢ stop)** | 4627 | 4626 | 1 (1) | 0 | $-1748.04 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 11:23 | +10 stop | NEAR | UP | 0.65 | 0.34 | -3.42 |
| 10-05 11:22 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-05 11:22 | +15 | BNB | UP | 0.70 | open |  |
| 10-05 11:22 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-05 11:22 | +5 | BNB | UP | 0.70 | 0.79 | 0.63 |
| 10-05 11:20 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 10-05 11:20 | +5 | HYPE | UP | 0.61 | 0.79 | 1.51 |
| 10-05 11:20 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-05 11:20 | +10 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-05 11:19 | +5 | BNB | UP | 0.64 | 0.70 | 0.28 |
| 10-05 11:18 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 10-05 11:18 | +20 | BNB | UP | 0.59 | 0.79 | 1.71 |
| 10-05 11:18 | +15 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-05 11:18 | +10 | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-05 11:18 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-05 11:17 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-05 11:17 | +10 stop | SOL | UP | 0.70 | 0.85 | 1.21 |
| 10-05 11:17 | +10 stop | HYPE | UP | 0.69 | 0.51 | -2.13 |
| 10-05 11:17 | +20 | HYPE | UP | 0.69 | 0.89 | 1.78 |
| 10-05 11:17 | +15 | HYPE | UP | 0.69 | 0.84 | 1.25 |
| 10-05 11:17 | +10 | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-05 11:17 | +5 | HYPE | UP | 0.69 | 0.77 | 0.52 |
| 10-05 11:16 | +10 stop | NEAR | DOWN | 0.71 | 0.51 | -2.32 |
| 10-05 11:16 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-05 11:16 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-05 11:16 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-05 11:16 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-05 11:16 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-05 11:16 | +20 | ETH | UP | 0.69 | 0.89 | 1.78 |
| 10-05 11:16 | +15 | ETH | UP | 0.69 | 0.87 | 1.57 |
| 10-05 11:16 | +10 | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-05 11:16 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-05 11:16 | +10 stop | XRP | UP | 0.66 | 0.77 | 0.81 |
| 10-05 11:16 | +20 | XRP | UP | 0.66 | 0.87 | 1.86 |
| 10-05 11:16 | +15 | XRP | UP | 0.66 | 0.84 | 1.54 |
| 10-05 11:16 | +10 | XRP | UP | 0.66 | 0.77 | 0.81 |
| 10-05 11:16 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-05 11:16 | +10 stop | BTC | UP | 0.64 | 0.76 | 0.90 |
| 10-05 11:16 | +20 | BTC | UP | 0.64 | 0.84 | 1.73 |
| 10-05 11:16 | +15 | BTC | UP | 0.64 | 0.80 | 1.31 |
