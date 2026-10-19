# Range-Scalp Bot

*Updated Mon Oct 19 08:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23731 | 20631 | 3100 (31) | 1 | $-7096.83 | -4.7% |
| **+10¢** | 17853 | 14284 | 3569 (45) | 2 | $-6307.42 | -5.6% |
| **+15¢** | 14957 | 11114 | 3843 (67) | 3 | $-5712.97 | -6.1% |
| **+20¢** | 13240 | 9219 | 4021 (86) | 3 | $-5078.34 | -6.1% |
| **+10¢ (15¢ stop)** | 29203 | 29152 | 51 (30) | 0 | $-11021.36 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 08:17 | +5 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-19 08:16 | +10 stop | BNB | UP | 0.64 | 0.84 | 1.73 |
| 10-19 08:16 | +10 | BNB | UP | 0.64 | 0.84 | 1.73 |
| 10-19 08:16 | +5 | BNB | UP | 0.64 | 0.72 | 0.48 |
| 10-19 08:16 | +10 stop | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-19 08:16 | +20 | HYPE | UP | 0.58 | 0.80 | 1.90 |
| 10-19 08:16 | +15 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-19 08:16 | +10 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-19 08:16 | +5 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-19 08:16 | +10 stop | ETH | UP | 0.71 | 0.86 | 1.26 |
| 10-19 08:16 | +20 | ETH | UP | 0.71 | 0.91 | 1.79 |
| 10-19 08:16 | +15 | ETH | UP | 0.71 | 0.86 | 1.26 |
| 10-19 08:16 | +10 | ETH | UP | 0.71 | 0.86 | 1.26 |
| 10-19 08:16 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 10-19 08:16 | +10 stop | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-19 08:16 | +20 | DOGE | UP | 0.68 | 0.91 | 2.09 |
| 10-19 08:16 | +15 | DOGE | UP | 0.68 | 0.86 | 1.55 |
| 10-19 08:16 | +10 | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-19 08:16 | +5 | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 10-19 08:16 | +10 stop | BNB | DOWN | 0.42 | 0.55 | 0.95 |
| 10-19 08:16 | +20 | BNB | DOWN | 0.42 | open |  |
| 10-19 08:16 | +15 | BNB | DOWN | 0.42 | open |  |
| 10-19 08:16 | +10 | BNB | DOWN | 0.42 | 0.55 | 0.95 |
| 10-19 08:16 | +5 | BNB | DOWN | 0.42 | 0.55 | 0.95 |
| 10-19 08:16 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-19 08:16 | +20 | SOL | UP | 0.63 | 0.85 | 1.94 |
| 10-19 08:16 | +15 | SOL | UP | 0.63 | 0.81 | 1.52 |
| 10-19 08:16 | +10 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-19 08:16 | +5 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-19 08:16 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-19 08:16 | +20 | BTC | UP | 0.65 | 0.89 | 2.17 |
| 10-19 08:16 | +15 | BTC | UP | 0.65 | 0.83 | 1.54 |
| 10-19 08:16 | +10 | BTC | UP | 0.65 | 0.79 | 1.12 |
| 10-19 08:16 | +5 | BTC | UP | 0.65 | 0.73 | 0.50 |
| 10-19 08:16 | +10 stop | NEAR | DOWN | 0.48 | 0.27 | -2.42 |
| 10-19 08:16 | +20 | NEAR | DOWN | 0.48 | open |  |
| 10-19 08:16 | +15 | NEAR | DOWN | 0.48 | open |  |
| 10-19 08:16 | +10 | NEAR | DOWN | 0.48 | open |  |
| 10-19 08:16 | +5 | NEAR | DOWN | 0.48 | 0.56 | 0.44 |
| 10-19 08:16 | +10 stop | ZEC | DOWN | 0.50 | 0.32 | -2.14 |
