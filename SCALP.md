# Range-Scalp Bot

*Updated Mon Oct 26 16:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35061 | 30605 | 4456 (43) | 0 | $-9766.85 | -4.4% |
| **+10¢** | 26241 | 21090 | 5151 (65) | 0 | $-8560.56 | -5.2% |
| **+15¢** | 21957 | 16411 | 5546 (89) | 0 | $-7671.64 | -5.6% |
| **+20¢** | 19464 | 13650 | 5814 (112) | 0 | $-6755.04 | -5.5% |
| **+10¢ (15¢ stop)** | 42926 | 42864 | 62 (33) | 0 | $-16256.56 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 15:52 | +10 stop | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-26 15:51 | +5 | ZEC | UP | 0.55 | no | -5.68 |
| 10-26 15:51 | +10 stop | BNB | DOWN | 0.58 | 0.72 | 1.07 |
| 10-26 15:51 | +10 | BNB | DOWN | 0.58 | 0.72 | 1.07 |
| 10-26 15:51 | +5 | BNB | DOWN | 0.58 | 0.72 | 1.07 |
| 10-26 15:50 | +10 stop | ZEC | UP | 0.56 | 0.32 | -2.74 |
| 10-26 15:50 | +20 | ZEC | UP | 0.56 | no | -5.78 |
| 10-26 15:50 | +15 | ZEC | UP | 0.56 | no | -5.78 |
| 10-26 15:50 | +10 | ZEC | UP | 0.56 | no | -5.78 |
| 10-26 15:50 | +5 | ZEC | UP | 0.56 | 0.62 | 0.25 |
| 10-26 15:50 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 10-26 15:50 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 10-26 15:50 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-26 15:50 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 15:49 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-26 15:49 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-26 15:48 | +10 stop | BNB | UP | 0.54 | 0.33 | -2.48 |
| 10-26 15:48 | +10 stop | HYPE | UP | 0.61 | 0.37 | -2.74 |
| 10-26 15:48 | +10 stop | HYPE | UP | 0.55 | 0.66 | 0.76 |
| 10-26 15:47 | +10 stop | NEAR | UP | 0.59 | 0.42 | -2.05 |
| 10-26 15:47 | +10 stop | XRP | UP | 0.60 | 0.36 | -2.74 |
| 10-26 15:47 | +10 stop | ETH | UP | 0.61 | 0.41 | -2.34 |
| 10-26 15:47 | +10 | ETH | UP | 0.61 | no | -6.27 |
| 10-26 15:47 | +5 | ETH | UP | 0.61 | no | -6.27 |
| 10-26 15:47 | +10 stop | BTC | UP | 0.61 | 0.44 | -2.05 |
| 10-26 15:47 | +10 stop | SOL | UP | 0.60 | 0.43 | -2.05 |
| 10-26 15:46 | +10 stop | ETH | DOWN | 0.48 | 0.61 | 0.95 |
| 10-26 15:46 | +20 | ETH | DOWN | 0.48 | 0.75 | 2.38 |
| 10-26 15:46 | +15 | ETH | DOWN | 0.48 | 0.63 | 1.15 |
| 10-26 15:46 | +10 | ETH | DOWN | 0.48 | 0.61 | 0.95 |
| 10-26 15:46 | +5 | ETH | DOWN | 0.47 | 0.61 | 1.05 |
| 10-26 15:46 | +10 stop | HYPE | DOWN | 0.66 | 0.49 | -2.08 |
| 10-26 15:46 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.82 |
| 10-26 15:46 | +15 | HYPE | DOWN | 0.67 | 0.85 | 1.51 |
| 10-26 15:46 | +10 | HYPE | DOWN | 0.67 | 0.80 | 0.98 |
| 10-26 15:46 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.36 |
| 10-26 15:46 | +10 stop | NEAR | DOWN | 0.55 | 0.40 | -1.85 |
| 10-26 15:46 | +20 | NEAR | DOWN | 0.53 | 0.75 | 1.88 |
| 10-26 15:46 | +15 | NEAR | DOWN | 0.53 | 0.70 | 1.37 |
| 10-26 15:46 | +10 | NEAR | DOWN | 0.53 | 0.70 | 1.37 |
