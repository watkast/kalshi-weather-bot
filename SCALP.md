# Range-Scalp Bot

*Updated Thu Oct 08 21:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8007 | 6936 | 1071 (13) | 4 | $-2530.99 | -5.0% |
| **+10¢** | 6067 | 4797 | 1270 (25) | 4 | $-2507.30 | -6.6% |
| **+15¢** | 5105 | 3769 | 1336 (37) | 3 | $-2023.61 | -6.3% |
| **+20¢** | 4558 | 3173 | 1385 (45) | 4 | $-1599.08 | -5.6% |
| **+10¢ (15¢ stop)** | 9737 | 9707 | 30 (19) | 0 | $-3591.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 21:27 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-08 21:26 | +10 stop | SOL | UP | 0.52 | 0.85 | 3.03 |
| 10-08 21:26 | +10 stop | ETH | UP | 0.55 | 0.69 | 1.07 |
| 10-08 21:26 | +20 | ETH | UP | 0.55 | 0.83 | 2.52 |
| 10-08 21:26 | +15 | ETH | UP | 0.55 | 0.83 | 2.52 |
| 10-08 21:26 | +10 | ETH | UP | 0.55 | 0.69 | 1.07 |
| 10-08 21:26 | +5 | ETH | UP | 0.55 | 0.69 | 1.07 |
| 10-08 21:26 | +10 stop | XRP | UP | 0.49 | 0.63 | 1.05 |
| 10-08 21:26 | +20 | XRP | UP | 0.49 | 0.79 | 2.70 |
| 10-08 21:26 | +15 | XRP | UP | 0.49 | 0.79 | 2.70 |
| 10-08 21:26 | +10 | XRP | UP | 0.49 | 0.63 | 1.05 |
| 10-08 21:26 | +5 | XRP | UP | 0.48 | 0.63 | 1.13 |
| 10-08 21:26 | +10 stop | ZEC | DOWN | 0.59 | 0.22 | -4.00 |
| 10-08 21:26 | +10 | ZEC | DOWN | 0.59 | open |  |
| 10-08 21:26 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-08 21:26 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 10-08 21:25 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-08 21:25 | +10 stop | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-08 21:25 | +10 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-08 21:25 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-08 21:24 | +10 stop | BTC | UP | 0.38 | 0.54 | 1.25 |
| 10-08 21:23 | +10 stop | ZEC | DOWN | 0.54 | 0.37 | -2.05 |
| 10-08 21:23 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 10-08 21:23 | +10 stop | BNB | UP | 0.71 | 0.37 | -3.72 |
| 10-08 21:23 | +15 | BNB | UP | 0.71 | open |  |
| 10-08 21:23 | +10 | BNB | UP | 0.71 | open |  |
| 10-08 21:23 | +5 | BNB | UP | 0.71 | open |  |
| 10-08 21:23 | +10 stop | DOGE | UP | 0.64 | 0.42 | -2.51 |
| 10-08 21:23 | +20 | DOGE | UP | 0.64 | open |  |
| 10-08 21:23 | +15 | DOGE | UP | 0.64 | 0.79 | 1.26 |
| 10-08 21:23 | +10 | DOGE | UP | 0.64 | 0.79 | 1.26 |
| 10-08 21:23 | +5 | DOGE | UP | 0.64 | 0.72 | 0.53 |
| 10-08 21:22 | +10 stop | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 10-08 21:22 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-08 21:22 | +20 | ETH | UP | 0.62 | 0.91 | 2.71 |
| 10-08 21:22 | +15 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 10-08 21:22 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-08 21:22 | +5 | ETH | UP | 0.62 | 0.70 | 0.48 |
| 10-08 21:22 | +10 stop | ZEC | UP | 0.66 | 0.50 | -1.94 |
| 10-08 21:22 | +20 | ZEC | UP | 0.66 | 0.93 | 2.46 |
