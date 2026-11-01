# Range-Scalp Bot

*Updated Sun Nov 01 04:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43219 | 37674 | 5545 (62) | 6 | $-12281.61 | -4.5% |
| **+10¢** | 32230 | 25822 | 6408 (84) | 6 | $-11004.55 | -5.4% |
| **+15¢** | 26966 | 20060 | 6906 (112) | 6 | $-10069.39 | -5.9% |
| **+20¢** | 23948 | 16713 | 7235 (146) | 6 | $-8892.34 | -5.9% |
| **+10¢ (15¢ stop)** | 52691 | 52608 | 83 (48) | 3 | $-19910.85 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 04:53 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 11-01 04:53 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-01 04:53 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-01 04:53 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 11-01 04:53 | +10 stop | BTC | UP | 0.61 | open |  |
| 11-01 04:51 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-01 04:49 | +10 stop | DOGE | UP | 0.65 | 0.88 | 2.06 |
| 11-01 04:49 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-01 04:49 | +10 stop | ETH | DOWN | 0.52 | open |  |
| 11-01 04:49 | +10 | ETH | DOWN | 0.52 | open |  |
| 11-01 04:49 | +5 | ETH | DOWN | 0.52 | 0.58 | 0.24 |
| 11-01 04:49 | +10 stop | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-01 04:49 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 11-01 04:49 | +10 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-01 04:49 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-01 04:49 | +10 stop | BTC | DOWN | 0.60 | 0.41 | -2.24 |
| 11-01 04:49 | +10 stop | SOL | DOWN | 0.61 | 0.38 | -2.64 |
| 11-01 04:49 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-01 04:49 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-01 04:48 | +5 | HYPE | UP | 0.66 | 0.77 | 0.77 |
| 11-01 04:48 | +10 stop | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-01 04:48 | +20 | ZEC | UP | 0.67 | 0.93 | 2.40 |
| 11-01 04:48 | +15 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 11-01 04:48 | +10 | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-01 04:48 | +5 | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-01 04:47 | +10 stop | DOGE | DOWN | 0.65 | 0.46 | -2.24 |
| 11-01 04:47 | +10 | DOGE | DOWN | 0.65 | open |  |
| 11-01 04:47 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-01 04:47 | +10 stop | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 11-01 04:47 | +20 | NEAR | UP | 0.55 | 0.78 | 1.99 |
| 11-01 04:47 | +15 | NEAR | UP | 0.57 | 0.74 | 1.38 |
| 11-01 04:47 | +10 | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 11-01 04:47 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 11-01 04:46 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 11-01 04:46 | +10 stop | HYPE | UP | 0.52 | 0.67 | 1.16 |
| 11-01 04:46 | +20 | HYPE | UP | 0.52 | 0.77 | 2.19 |
| 11-01 04:46 | +15 | HYPE | UP | 0.52 | 0.67 | 1.16 |
| 11-01 04:46 | +10 | HYPE | UP | 0.52 | 0.67 | 1.16 |
| 11-01 04:46 | +5 | HYPE | UP | 0.52 | 0.57 | 0.14 |
| 11-01 04:46 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
