# Range-Scalp Bot

*Updated Thu Nov 26 21:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72930 | 63657 | 9273 (158) | 3 | $-19415.64 | -4.2% |
| **+10¢** | 54360 | 43534 | 10826 (203) | 7 | $-18010.91 | -5.3% |
| **+15¢** | 45523 | 33861 | 11662 (261) | 7 | $-16101.00 | -5.6% |
| **+20¢** | 40510 | 28232 | 12278 (327) | 8 | $-14486.78 | -5.7% |
| **+10¢ (15¢ stop)** | 88812 | 88603 | 209 (128) | 2 | $-32771.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 21:24 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-26 21:24 | +5 | SOL | DOWN | 0.63 | open |  |
| 11-26 21:23 | +10 stop | BNB | UP | 0.64 | 0.44 | -2.35 |
| 11-26 21:23 | +10 stop | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 11-26 21:23 | +20 | HYPE | DOWN | 0.59 | open |  |
| 11-26 21:23 | +15 | HYPE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-26 21:23 | +10 | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 11-26 21:23 | +5 | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 11-26 21:23 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 11-26 21:23 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-26 21:22 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-26 21:22 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 11-26 21:22 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-26 21:22 | +5 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-26 21:21 | +10 stop | NEAR | UP | 0.60 | 0.41 | -2.24 |
| 11-26 21:21 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 11-26 21:21 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-26 21:21 | +10 stop | XRP | UP | 0.67 | 0.31 | -3.91 |
| 11-26 21:20 | +10 stop | HYPE | DOWN | 0.64 | 0.75 | 0.80 |
| 11-26 21:20 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 11-26 21:20 | +10 stop | SOL | UP | 0.68 | 0.47 | -2.44 |
| 11-26 21:20 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 11-26 21:19 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-26 21:19 | +10 stop | DOGE | UP | 0.69 | 0.47 | -2.53 |
| 11-26 21:18 | +10 stop | HYPE | UP | 0.53 | 0.37 | -1.92 |
| 11-26 21:18 | +10 stop | XRP | UP | 0.54 | 0.38 | -1.95 |
| 11-26 21:18 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-26 21:17 | +5 | BTC | DOWN | 0.47 | 0.57 | 0.64 |
| 11-26 21:17 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 11-26 21:17 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 11-26 21:17 | +5 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-26 21:17 | +10 stop | HYPE | DOWN | 0.59 | 0.39 | -2.34 |
| 11-26 21:17 | +20 | HYPE | DOWN | 0.59 | 0.80 | 1.81 |
| 11-26 21:17 | +15 | HYPE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-26 21:17 | +10 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-26 21:17 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.27 |
| 11-26 21:17 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 11-26 21:17 | +20 | DOGE | DOWN | 0.66 | open |  |
| 11-26 21:17 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-26 21:17 | +10 | DOGE | DOWN | 0.66 | open |  |
