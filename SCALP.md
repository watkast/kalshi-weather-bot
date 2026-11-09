# Range-Scalp Bot

*Updated Mon Nov 09 15:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53834 | 46958 | 6876 (86) | 0 | $-14723.30 | -4.3% |
| **+10¢** | 40207 | 32183 | 8024 (112) | 0 | $-13721.62 | -5.4% |
| **+15¢** | 33693 | 25046 | 8647 (143) | 2 | $-12498.34 | -5.9% |
| **+20¢** | 29987 | 20916 | 9071 (189) | 5 | $-10970.09 | -5.8% |
| **+10¢ (15¢ stop)** | 65583 | 65477 | 106 (63) | 0 | $-24286.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 15:07 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 15:06 | +10 stop | DOGE | DOWN | 0.70 | 0.52 | -2.13 |
| 11-09 15:06 | +10 stop | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 11-09 15:06 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-09 15:06 | +10 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-09 15:06 | +5 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-09 15:05 | +10 stop | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-09 15:05 | +15 | ZEC | DOWN | 0.51 | 0.70 | 1.57 |
| 11-09 15:05 | +10 | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-09 15:05 | +5 | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-09 15:05 | +10 stop | NEAR | DOWN | 0.65 | 0.81 | 1.31 |
| 11-09 15:04 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-09 15:03 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-09 15:03 | +10 stop | ZEC | UP | 0.55 | 0.71 | 1.27 |
| 11-09 15:03 | +20 | ZEC | UP | 0.55 | open |  |
| 11-09 15:03 | +15 | ZEC | UP | 0.55 | 0.71 | 1.27 |
| 11-09 15:03 | +10 | ZEC | UP | 0.55 | 0.71 | 1.27 |
| 11-09 15:03 | +5 | ZEC | UP | 0.55 | 0.71 | 1.27 |
| 11-09 15:03 | +10 stop | BTC | DOWN | 0.61 | 0.79 | 1.51 |
| 11-09 15:03 | +10 stop | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 11-09 15:03 | +10 stop | NEAR | UP | 0.57 | 0.42 | -1.86 |
| 11-09 15:03 | +10 stop | DOGE | UP | 0.58 | 0.40 | -2.15 |
| 11-09 15:03 | +10 stop | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 15:03 | +10 | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 15:03 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 11-09 15:02 | +5 | BTC | DOWN | 0.56 | 0.62 | 0.25 |
| 11-09 15:02 | +5 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 15:02 | +10 stop | NEAR | DOWN | 0.69 | 0.47 | -2.53 |
| 11-09 15:02 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-09 15:02 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-09 15:02 | +10 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 15:02 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 11-09 15:02 | +10 stop | ETH | DOWN | 0.68 | 0.52 | -1.94 |
| 11-09 15:02 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-09 15:02 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 11-09 15:02 | +20 | SOL | DOWN | 0.68 | 0.91 | 2.09 |
| 11-09 15:02 | +15 | SOL | DOWN | 0.68 | 0.87 | 1.66 |
| 11-09 15:02 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 15:02 | +5 | SOL | DOWN | 0.68 | 0.76 | 0.51 |
| 11-09 15:02 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
