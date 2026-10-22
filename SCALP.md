# Range-Scalp Bot

*Updated Thu Oct 22 13:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28809 | 25104 | 3705 (39) | 3 | $-8279.60 | -4.6% |
| **+10¢** | 21625 | 17339 | 4286 (55) | 5 | $-7362.76 | -5.4% |
| **+15¢** | 18099 | 13490 | 4609 (78) | 5 | $-6582.06 | -5.8% |
| **+20¢** | 16013 | 11180 | 4833 (100) | 5 | $-5926.09 | -5.9% |
| **+10¢ (15¢ stop)** | 35344 | 35285 | 59 (32) | 0 | $-13245.25 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 13:58 | +10 stop | BTC | DOWN | 0.47 | 0.68 | 1.76 |
| 10-22 13:58 | +20 | BTC | DOWN | 0.47 | 0.68 | 1.76 |
| 10-22 13:58 | +15 | BTC | DOWN | 0.47 | 0.68 | 1.76 |
| 10-22 13:58 | +10 | BTC | DOWN | 0.47 | 0.68 | 1.76 |
| 10-22 13:58 | +5 | BTC | DOWN | 0.48 | 0.68 | 1.66 |
| 10-22 13:58 | +10 stop | XRP | DOWN | 0.21 | 0.60 | 3.61 |
| 10-22 13:58 | +15 | XRP | DOWN | 0.21 | 0.60 | 3.61 |
| 10-22 13:58 | +10 | XRP | DOWN | 0.22 | 0.60 | 3.50 |
| 10-22 13:58 | +5 | XRP | DOWN | 0.23 | 0.60 | 3.40 |
| 10-22 13:58 | +10 stop | XRP | UP | 0.47 | 0.63 | 1.25 |
| 10-22 13:58 | +20 | XRP | UP | 0.48 | 0.89 | 3.85 |
| 10-22 13:58 | +15 | XRP | UP | 0.48 | 0.63 | 1.15 |
| 10-22 13:58 | +10 | XRP | UP | 0.48 | 0.63 | 1.15 |
| 10-22 13:58 | +5 | XRP | UP | 0.47 | 0.63 | 1.25 |
| 10-22 13:56 | +10 stop | HYPE | DOWN | 0.46 | 0.57 | 0.74 |
| 10-22 13:55 | +10 stop | HYPE | DOWN | 0.57 | 0.30 | -3.03 |
| 10-22 13:55 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-22 13:55 | +15 | HYPE | DOWN | 0.55 | open |  |
| 10-22 13:55 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-22 13:55 | +5 | HYPE | DOWN | 0.56 | open |  |
| 10-22 13:55 | +10 stop | ETH | DOWN | 0.50 | 0.28 | -2.53 |
| 10-22 13:55 | +20 | ETH | DOWN | 0.50 | open |  |
| 10-22 13:55 | +15 | ETH | DOWN | 0.50 | open |  |
| 10-22 13:55 | +10 | ETH | DOWN | 0.50 | open |  |
| 10-22 13:55 | +5 | ETH | DOWN | 0.50 | 0.56 | 0.21 |
| 10-22 13:54 | +10 stop | DOGE | DOWN | 0.69 | 0.53 | -1.93 |
| 10-22 13:54 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-22 13:54 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-22 13:54 | +10 | DOGE | DOWN | 0.69 | open |  |
| 10-22 13:54 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-22 13:54 | +10 stop | ZEC | DOWN | 0.69 | 0.30 | -4.20 |
| 10-22 13:54 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-22 13:54 | +15 | ZEC | DOWN | 0.69 | open |  |
| 10-22 13:54 | +10 | ZEC | DOWN | 0.69 | open |  |
| 10-22 13:54 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-22 13:54 | +5 | NEAR | UP | 0.52 | 0.86 | 3.13 |
| 10-22 13:53 | +10 stop | NEAR | DOWN | 0.50 | 0.13 | -3.96 |
| 10-22 13:53 | +15 | NEAR | DOWN | 0.50 | open |  |
| 10-22 13:53 | +10 | NEAR | DOWN | 0.48 | open |  |
| 10-22 13:53 | +5 | NEAR | DOWN | 0.48 | 0.55 | 0.34 |
