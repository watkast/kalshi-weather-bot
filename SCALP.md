# Range-Scalp Bot

*Updated Wed Nov 18 06:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63734 | 55588 | 8146 (118) | 4 | $-17421.44 | -4.3% |
| **+10¢** | 47617 | 38080 | 9537 (159) | 2 | $-16356.31 | -5.5% |
| **+15¢** | 39922 | 29638 | 10284 (204) | 2 | $-14835.51 | -5.9% |
| **+20¢** | 35554 | 24760 | 10794 (259) | 3 | $-13121.39 | -5.9% |
| **+10¢ (15¢ stop)** | 77547 | 77389 | 158 (93) | 1 | $-28512.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 06:27 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-18 06:27 | +10 stop | NEAR | UP | 0.64 | 0.46 | -2.15 |
| 11-18 06:27 | +10 | NEAR | UP | 0.65 | open |  |
| 11-18 06:27 | +5 | NEAR | UP | 0.65 | open |  |
| 11-18 06:25 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 11-18 06:25 | +20 | NEAR | UP | 0.61 | open |  |
| 11-18 06:25 | +15 | NEAR | UP | 0.61 | open |  |
| 11-18 06:25 | +10 | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 11-18 06:25 | +5 | NEAR | UP | 0.61 | 0.67 | 0.27 |
| 11-18 06:25 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.73 |
| 11-18 06:25 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.36 |
| 11-18 06:25 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.73 |
| 11-18 06:25 | +10 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 11-18 06:25 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 11-18 06:24 | +10 stop | BTC | DOWN | 0.69 | 0.40 | -3.22 |
| 11-18 06:23 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 06:23 | +10 stop | SOL | UP | 0.48 | 0.28 | -2.33 |
| 11-18 06:23 | +5 | SOL | UP | 0.53 | open |  |
| 11-18 06:23 | +5 | SOL | DOWN | 0.45 | 0.54 | 0.54 |
| 11-18 06:23 | +10 stop | BTC | UP | 0.69 | 0.38 | -3.42 |
| 11-18 06:22 | +10 stop | ETH | DOWN | 0.61 | 0.42 | -2.25 |
| 11-18 06:22 | +10 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 11-18 06:22 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 11-18 06:22 | +10 stop | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-18 06:22 | +5 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-18 06:22 | +10 stop | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 11-18 06:22 | +15 | DOGE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-18 06:22 | +10 | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-18 06:22 | +10 stop | SOL | DOWN | 0.55 | 0.39 | -1.95 |
| 11-18 06:22 | +5 | SOL | DOWN | 0.55 | 0.61 | 0.25 |
| 11-18 06:22 | +10 stop | BTC | DOWN | 0.48 | 0.60 | 0.85 |
| 11-18 06:20 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 11-18 06:20 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.93 |
| 11-18 06:20 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 11-18 06:20 | +5 | DOGE | UP | 0.56 | open |  |
| 11-18 06:20 | +10 stop | SOL | UP | 0.57 | 0.29 | -3.13 |
| 11-18 06:19 | +10 stop | BNB | UP | 0.51 | 0.34 | -2.04 |
| 11-18 06:19 | +5 | BNB | UP | 0.51 | 0.56 | 0.14 |
| 11-18 06:19 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.69 |
| 11-18 06:19 | +10 stop | BTC | UP | 0.62 | 0.38 | -2.74 |
