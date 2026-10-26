# Range-Scalp Bot

*Updated Mon Oct 26 05:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34333 | 29977 | 4356 (43) | 6 | $-9483.24 | -4.4% |
| **+10¢** | 25696 | 20656 | 5040 (65) | 6 | $-8329.23 | -5.2% |
| **+15¢** | 21490 | 16064 | 5426 (89) | 4 | $-7448.73 | -5.5% |
| **+20¢** | 19046 | 13361 | 5685 (112) | 5 | $-6543.16 | -5.5% |
| **+10¢ (15¢ stop)** | 42064 | 42002 | 62 (33) | 0 | $-16029.86 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 05:44 | +10 stop | ETH | UP | 0.60 | 0.23 | -4.01 |
| 10-26 05:42 | +10 stop | SOL | UP | 0.70 | 0.89 | 1.68 |
| 10-26 05:42 | +15 | SOL | UP | 0.70 | 0.89 | 1.68 |
| 10-26 05:42 | +10 | SOL | UP | 0.70 | 0.89 | 1.68 |
| 10-26 05:42 | +10 stop | ETH | DOWN | 0.47 | 0.59 | 0.85 |
| 10-26 05:41 | +10 stop | BTC | DOWN | 0.53 | 0.33 | -2.34 |
| 10-26 05:40 | +10 stop | ETH | DOWN | 0.69 | 0.40 | -3.22 |
| 10-26 05:40 | +10 stop | DOGE | UP | 0.52 | 0.74 | 1.88 |
| 10-26 05:40 | +10 stop | ETH | UP | 0.50 | 0.66 | 1.26 |
| 10-26 05:39 | +10 stop | XRP | UP | 0.57 | 0.35 | -2.54 |
| 10-26 05:39 | +10 | XRP | UP | 0.57 | open |  |
| 10-26 05:39 | +5 | XRP | UP | 0.59 | open |  |
| 10-26 05:39 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 10-26 05:39 | +5 | BNB | UP | 0.63 | open |  |
| 10-26 05:39 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-26 05:39 | +15 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-26 05:39 | +10 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-26 05:39 | +5 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-26 05:39 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-26 05:39 | +15 | XRP | UP | 0.55 | open |  |
| 10-26 05:39 | +10 | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-26 05:39 | +5 | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-26 05:39 | +10 stop | NEAR | UP | 0.67 | 0.43 | -2.74 |
| 10-26 05:39 | +10 | NEAR | UP | 0.67 | open |  |
| 10-26 05:39 | +5 | NEAR | UP | 0.67 | open |  |
| 10-26 05:38 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-26 05:38 | +10 stop | SOL | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +15 | SOL | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +10 | SOL | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +5 | SOL | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +10 stop | XRP | DOWN | 0.45 | 0.61 | 1.25 |
| 10-26 05:38 | +20 | XRP | DOWN | 0.46 | 0.67 | 1.76 |
| 10-26 05:38 | +15 | XRP | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +10 | XRP | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +5 | XRP | DOWN | 0.46 | 0.61 | 1.15 |
| 10-26 05:38 | +10 stop | NEAR | DOWN | 0.44 | 0.57 | 0.94 |
| 10-26 05:38 | +20 | NEAR | DOWN | 0.44 | 0.66 | 1.86 |
| 10-26 05:38 | +15 | NEAR | DOWN | 0.44 | 0.66 | 1.86 |
| 10-26 05:38 | +10 | NEAR | DOWN | 0.44 | 0.57 | 0.94 |
| 10-26 05:38 | +5 | NEAR | DOWN | 0.45 | 0.57 | 0.84 |
