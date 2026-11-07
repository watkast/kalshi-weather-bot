# Range-Scalp Bot

*Updated Sat Nov 07 19:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51422 | 44836 | 6586 (79) | 2 | $-14285.51 | -4.4% |
| **+10¢** | 38372 | 30695 | 7677 (105) | 3 | $-13279.87 | -5.5% |
| **+15¢** | 32126 | 23851 | 8275 (134) | 2 | $-12197.73 | -6.1% |
| **+20¢** | 28575 | 19901 | 8674 (177) | 2 | $-10759.64 | -6.0% |
| **+10¢ (15¢ stop)** | 62624 | 62521 | 103 (61) | 0 | $-23170.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 19:38 | +10 stop | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 11-07 19:37 | +5 | BTC | DOWN | 0.69 | 0.77 | 0.52 |
| 11-07 19:37 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-07 19:37 | +10 stop | ETH | DOWN | 0.64 | 0.45 | -2.25 |
| 11-07 19:36 | +10 stop | BTC | DOWN | 0.68 | 0.85 | 1.45 |
| 11-07 19:36 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-07 19:35 | +10 stop | NEAR | UP | 0.51 | 0.28 | -2.63 |
| 11-07 19:35 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 19:35 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 19:35 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-07 19:35 | +10 stop | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 11-07 19:35 | +15 | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 11-07 19:35 | +10 | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 11-07 19:35 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 11-07 19:35 | +10 stop | XRP | UP | 0.54 | 0.34 | -2.34 |
| 11-07 19:35 | +10 | XRP | UP | 0.55 | open |  |
| 11-07 19:35 | +5 | XRP | UP | 0.55 | open |  |
| 11-07 19:34 | +5 | ETH | UP | 0.64 | open |  |
| 11-07 19:34 | +10 stop | BTC | DOWN | 0.54 | 0.71 | 1.37 |
| 11-07 19:34 | +5 | BTC | DOWN | 0.54 | 0.63 | 0.55 |
| 11-07 19:34 | +10 stop | ETH | UP | 0.56 | 0.32 | -2.74 |
| 11-07 19:34 | +10 | ETH | UP | 0.56 | open |  |
| 11-07 19:34 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 11-07 19:33 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
| 11-07 19:33 | +10 | NEAR | DOWN | 0.62 | 0.95 | 3.12 |
| 11-07 19:33 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
| 11-07 19:33 | +10 stop | BTC | DOWN | 0.55 | 0.39 | -1.95 |
| 11-07 19:33 | +10 stop | ETH | DOWN | 0.56 | 0.35 | -2.44 |
| 11-07 19:33 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.37 |
| 11-07 19:32 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 11-07 19:32 | +5 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 11-07 19:32 | +5 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-07 19:32 | +10 stop | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-07 19:32 | +20 | NEAR | DOWN | 0.54 | 0.95 | 3.91 |
| 11-07 19:32 | +15 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 11-07 19:32 | +10 | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-07 19:32 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 11-07 19:32 | +10 stop | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 11-07 19:32 | +20 | SOL | DOWN | 0.62 | 0.86 | 2.14 |
| 11-07 19:32 | +15 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
