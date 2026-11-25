# Range-Scalp Bot

*Updated Wed Nov 25 16:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71729 | 62597 | 9132 (158) | 5 | $-19178.11 | -4.2% |
| **+10¢** | 53506 | 42844 | 10662 (203) | 4 | $-17773.26 | -5.3% |
| **+15¢** | 44816 | 33336 | 11480 (260) | 4 | $-15825.04 | -5.6% |
| **+20¢** | 39900 | 27812 | 12088 (326) | 6 | $-14213.31 | -5.7% |
| **+10¢ (15¢ stop)** | 87376 | 87167 | 209 (128) | 0 | $-32139.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 16:11 | +10 stop | SOL | UP | 0.43 | 0.62 | 1.55 |
| 11-25 16:10 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-25 16:10 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-25 16:10 | +10 stop | BNB | DOWN | 0.55 | 0.27 | -3.12 |
| 11-25 16:10 | +10 stop | NEAR | DOWN | 0.46 | 0.30 | -1.93 |
| 11-25 16:09 | +10 stop | ZEC | DOWN | 0.71 | 0.46 | -2.83 |
| 11-25 16:09 | +10 stop | DOGE | DOWN | 0.71 | 0.50 | -2.43 |
| 11-25 16:09 | +10 stop | SOL | DOWN | 0.68 | 0.50 | -2.14 |
| 11-25 16:08 | +10 stop | NEAR | DOWN | 0.41 | 0.54 | 0.95 |
| 11-25 16:08 | +10 stop | SOL | DOWN | 0.50 | 0.68 | 1.46 |
| 11-25 16:08 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-25 16:08 | +10 stop | BNB | DOWN | 0.66 | 0.48 | -2.13 |
| 11-25 16:08 | +10 stop | ETH | DOWN | 0.68 | 0.48 | -2.34 |
| 11-25 16:08 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.76 |
| 11-25 16:08 | +5 | ZEC | DOWN | 0.69 | 0.81 | 0.93 |
| 11-25 16:07 | +10 stop | ETH | UP | 0.36 | 0.54 | 1.45 |
| 11-25 16:07 | +10 stop | NEAR | UP | 0.41 | 0.61 | 1.66 |
| 11-25 16:07 | +10 stop | SOL | UP | 0.53 | 0.32 | -2.44 |
| 11-25 16:06 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-25 16:06 | +10 stop | BNB | DOWN | 0.51 | 0.61 | 0.70 |
| 11-25 16:06 | +10 stop | DOGE | DOWN | 0.49 | 0.64 | 1.15 |
| 11-25 16:04 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-25 16:04 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
| 11-25 16:04 | +10 stop | XRP | DOWN | 0.67 | 0.47 | -2.34 |
| 11-25 16:04 | +10 stop | SOL | UP | 0.48 | 0.65 | 1.36 |
| 11-25 16:03 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-25 16:03 | +10 stop | BTC | DOWN | 0.58 | 0.36 | -2.55 |
| 11-25 16:03 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 11-25 16:03 | +10 stop | NEAR | DOWN | 0.52 | 0.37 | -1.85 |
| 11-25 16:03 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.72 |
| 11-25 16:03 | +15 | ZEC | DOWN | 0.60 | 0.81 | 1.86 |
| 11-25 16:03 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.72 |
| 11-25 16:03 | +5 | ZEC | DOWN | 0.60 | 0.69 | 0.60 |
| 11-25 16:02 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-25 16:02 | +10 stop | XRP | DOWN | 0.62 | 0.45 | -2.05 |
| 11-25 16:02 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 11-25 16:02 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-25 16:02 | +10 stop | BNB | UP | 0.59 | 0.43 | -1.95 |
| 11-25 16:02 | +20 | BNB | UP | 0.59 | 0.93 | 3.18 |
| 11-25 16:02 | +15 | BNB | UP | 0.59 | 0.93 | 3.18 |
