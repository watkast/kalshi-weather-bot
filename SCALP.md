# Range-Scalp Bot

*Updated Sun Nov 08 21:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52870 | 46096 | 6774 (83) | 2 | $-14634.74 | -4.4% |
| **+10¢** | 39475 | 31579 | 7896 (108) | 3 | $-13617.65 | -5.5% |
| **+15¢** | 33070 | 24564 | 8506 (139) | 4 | $-12434.15 | -6.0% |
| **+20¢** | 29414 | 20497 | 8917 (184) | 6 | $-10940.23 | -5.9% |
| **+10¢ (15¢ stop)** | 64393 | 64287 | 106 (63) | 0 | $-23824.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 21:40 | +10 stop | BTC | UP | 0.38 | 0.58 | 1.65 |
| 11-08 21:39 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-08 21:38 | +10 stop | BNB | DOWN | 0.66 | 0.83 | 1.42 |
| 11-08 21:38 | +10 | BNB | DOWN | 0.66 | 0.83 | 1.42 |
| 11-08 21:38 | +5 | BNB | DOWN | 0.66 | 0.76 | 0.69 |
| 11-08 21:38 | +10 stop | DOGE | UP | 0.60 | 0.36 | -2.74 |
| 11-08 21:38 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 21:38 | +20 | ZEC | DOWN | 0.65 | 0.91 | 2.40 |
| 11-08 21:38 | +15 | ZEC | DOWN | 0.67 | 0.91 | 2.20 |
| 11-08 21:38 | +10 | ZEC | DOWN | 0.67 | 0.91 | 2.20 |
| 11-08 21:38 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-08 21:38 | +5 | HYPE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-08 21:38 | +5 | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-08 21:37 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 11-08 21:37 | +10 stop | DOGE | DOWN | 0.50 | 0.60 | 0.65 |
| 11-08 21:36 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-08 21:36 | +10 | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-08 21:36 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 11-08 21:36 | +10 stop | ETH | UP | 0.65 | 0.79 | 1.12 |
| 11-08 21:35 | +10 stop | ETH | UP | 0.71 | 0.55 | -1.93 |
| 11-08 21:35 | +20 | ETH | UP | 0.71 | open |  |
| 11-08 21:35 | +15 | ETH | UP | 0.71 | 0.86 | 1.26 |
| 11-08 21:35 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-08 21:35 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 11-08 21:35 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-08 21:35 | +10 stop | DOGE | DOWN | 0.61 | 0.36 | -2.81 |
| 11-08 21:35 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-08 21:35 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-08 21:35 | +10 stop | SOL | UP | 0.60 | 0.70 | 0.68 |
| 11-08 21:35 | +20 | SOL | UP | 0.60 | 0.85 | 2.24 |
| 11-08 21:35 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-08 21:35 | +10 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 11-08 21:35 | +5 | SOL | UP | 0.62 | 0.70 | 0.48 |
| 11-08 21:35 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 11-08 21:35 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-08 21:35 | +10 stop | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 11-08 21:35 | +10 | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 11-08 21:35 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-08 21:34 | +10 stop | BTC | UP | 0.44 | 0.60 | 1.25 |
| 11-08 21:34 | +10 stop | DOGE | UP | 0.52 | 0.37 | -1.85 |
