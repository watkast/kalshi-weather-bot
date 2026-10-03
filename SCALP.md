# Range-Scalp Bot

*Updated Sat Oct 03 10:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 603 | 520 | 83 (1) | 3 | $-210.39 | -5.5% |
| **+10¢** | 461 | 368 | 93 (2) | 3 | $-168.52 | -5.8% |
| **+15¢** | 389 | 289 | 100 (3) | 4 | $-161.38 | -6.6% |
| **+20¢** | 340 | 236 | 104 (3) | 3 | $-154.30 | -7.2% |
| **+10¢ (15¢ stop)** | 789 | 788 | 1 (1) | 1 | $-419.41 | -8.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 10:28 | +10 stop | ETH | DOWN | 0.55 | open |  |
| 10-03 10:28 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-03 10:28 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-03 10:28 | +10 | ETH | DOWN | 0.50 | open |  |
| 10-03 10:28 | +5 | ETH | DOWN | 0.49 | open |  |
| 10-03 10:27 | +10 stop | SOL | UP | 0.56 | 0.78 | 1.90 |
| 10-03 10:27 | +10 stop | BTC | DOWN | 0.70 | 0.42 | -3.13 |
| 10-03 10:27 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-03 10:27 | +5 | ZEC | DOWN | 0.45 | 0.60 | 1.15 |
| 10-03 10:26 | +10 stop | BNB | UP | 0.70 | 0.86 | 1.36 |
| 10-03 10:26 | +5 | BNB | UP | 0.70 | 0.79 | 0.63 |
| 10-03 10:26 | +10 stop | ZEC | DOWN | 0.56 | 0.35 | -2.44 |
| 10-03 10:26 | +15 | ZEC | DOWN | 0.56 | open |  |
| 10-03 10:26 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-03 10:26 | +5 | ZEC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-03 10:26 | +10 stop | SOL | UP | 0.49 | 0.59 | 0.65 |
| 10-03 10:26 | +10 stop | BTC | UP | 0.69 | 0.27 | -4.49 |
| 10-03 10:26 | +20 | BTC | UP | 0.69 | open |  |
| 10-03 10:26 | +15 | BTC | UP | 0.69 | open |  |
| 10-03 10:26 | +10 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-03 10:26 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-03 10:25 | +10 stop | ZEC | DOWN | 0.47 | 0.67 | 1.66 |
| 10-03 10:25 | +15 | ZEC | DOWN | 0.47 | 0.67 | 1.66 |
| 10-03 10:25 | +10 | ZEC | DOWN | 0.47 | 0.67 | 1.66 |
| 10-03 10:25 | +5 | ZEC | DOWN | 0.47 | 0.53 | 0.24 |
| 10-03 10:24 | +10 stop | SOL | DOWN | 0.59 | 0.37 | -2.54 |
| 10-03 10:24 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-03 10:24 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-03 10:24 | +10 | SOL | DOWN | 0.59 | open |  |
| 10-03 10:24 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-03 10:24 | +10 stop | ZEC | UP | 0.41 | 0.62 | 1.76 |
| 10-03 10:24 | +15 | ZEC | UP | 0.41 | 0.62 | 1.76 |
| 10-03 10:24 | +10 | ZEC | UP | 0.41 | 0.62 | 1.76 |
| 10-03 10:24 | +5 | ZEC | UP | 0.46 | 0.62 | 1.25 |
| 10-03 10:22 | +10 stop | ZEC | UP | 0.48 | 0.64 | 1.25 |
| 10-03 10:22 | +15 | ZEC | UP | 0.48 | 0.64 | 1.25 |
| 10-03 10:22 | +10 | ZEC | UP | 0.48 | 0.64 | 1.20 |
| 10-03 10:22 | +5 | ZEC | UP | 0.48 | 0.55 | 0.29 |
| 10-03 10:22 | +10 stop | BNB | UP | 0.62 | 0.46 | -1.92 |
| 10-03 10:22 | +5 | BNB | UP | 0.62 | 0.72 | 0.71 |
