# Range-Scalp Bot

*Updated Tue Oct 06 00:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4393 | 3788 | 605 (6) | 1 | $-1480.69 | -5.3% |
| **+10¢** | 3384 | 2683 | 701 (9) | 1 | $-1355.12 | -6.4% |
| **+15¢** | 2840 | 2100 | 740 (12) | 1 | $-1168.91 | -6.6% |
| **+20¢** | 2542 | 1770 | 772 (17) | 1 | $-991.59 | -6.2% |
| **+10¢ (15¢ stop)** | 5386 | 5375 | 11 (6) | 0 | $-1917.55 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 00:25 | +10 stop | ETH | UP | 0.65 | 0.37 | -3.13 |
| 10-06 00:25 | +20 | ETH | UP | 0.65 | open |  |
| 10-06 00:25 | +15 | ETH | UP | 0.66 | open |  |
| 10-06 00:25 | +10 | ETH | UP | 0.66 | open |  |
| 10-06 00:25 | +5 | ETH | UP | 0.66 | open |  |
| 10-06 00:22 | +10 stop | DOGE | DOWN | 0.55 | 0.38 | -2.01 |
| 10-06 00:21 | +10 stop | ETH | UP | 0.65 | 0.77 | 0.91 |
| 10-06 00:21 | +10 stop | DOGE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-06 00:20 | +5 | SOL | UP | 0.44 | 0.54 | 0.64 |
| 10-06 00:19 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
| 10-06 00:19 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.81 |
| 10-06 00:19 | +10 stop | SOL | UP | 0.55 | 0.73 | 1.48 |
| 10-06 00:19 | +15 | SOL | UP | 0.55 | 0.73 | 1.48 |
| 10-06 00:19 | +10 | SOL | UP | 0.55 | 0.73 | 1.48 |
| 10-06 00:19 | +5 | SOL | UP | 0.55 | 0.62 | 0.35 |
| 10-06 00:19 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-06 00:19 | +20 | XRP | UP | 0.71 | 0.92 | 1.91 |
| 10-06 00:19 | +15 | XRP | UP | 0.71 | 0.88 | 1.47 |
| 10-06 00:19 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-06 00:19 | +5 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-06 00:18 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.00 |
| 10-06 00:18 | +20 | NEAR | UP | 0.66 | 0.87 | 1.86 |
| 10-06 00:18 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 10-06 00:18 | +10 | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-06 00:18 | +5 | NEAR | UP | 0.66 | 0.73 | 0.40 |
| 10-06 00:18 | +10 stop | HYPE | UP | 0.69 | 0.83 | 1.15 |
| 10-06 00:18 | +10 stop | DOGE | UP | 0.58 | 0.40 | -2.15 |
| 10-06 00:18 | +10 stop | BTC | UP | 0.68 | 0.81 | 1.03 |
| 10-06 00:18 | +10 | BTC | UP | 0.68 | 0.81 | 1.03 |
| 10-06 00:17 | +10 stop | ETH | UP | 0.63 | 0.38 | -2.83 |
| 10-06 00:17 | +20 | ETH | UP | 0.62 | 0.83 | 1.79 |
| 10-06 00:17 | +15 | ETH | UP | 0.62 | 0.77 | 1.20 |
| 10-06 00:17 | +10 | ETH | UP | 0.62 | 0.73 | 0.79 |
| 10-06 00:17 | +5 | ETH | UP | 0.62 | 0.71 | 0.58 |
| 10-06 00:16 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 10-06 00:16 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-06 00:16 | +20 | BNB | UP | 0.63 | 0.88 | 2.25 |
| 10-06 00:16 | +15 | BNB | UP | 0.63 | 0.81 | 1.52 |
| 10-06 00:16 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-06 00:16 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
