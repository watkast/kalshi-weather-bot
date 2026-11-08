# Range-Scalp Bot

*Updated Sun Nov 08 22:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52882 | 46106 | 6776 (83) | 1 | $-14642.50 | -4.4% |
| **+10¢** | 39484 | 31585 | 7899 (108) | 1 | $-13626.45 | -5.5% |
| **+15¢** | 33079 | 24568 | 8511 (139) | 1 | $-12458.91 | -6.0% |
| **+20¢** | 29425 | 20502 | 8923 (184) | 1 | $-10968.79 | -5.9% |
| **+10¢ (15¢ stop)** | 64403 | 64297 | 106 (63) | 1 | $-23829.72 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 22:01 | +10 stop | ETH | UP | 0.64 | open |  |
| 11-08 22:01 | +20 | ETH | UP | 0.64 | open |  |
| 11-08 22:01 | +15 | ETH | UP | 0.64 | open |  |
| 11-08 22:01 | +10 | ETH | UP | 0.64 | open |  |
| 11-08 22:01 | +5 | ETH | UP | 0.64 | open |  |
| 11-08 21:54 | +10 stop | ZEC | UP | 0.55 | 0.15 | -4.27 |
| 11-08 21:53 | +10 stop | ZEC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-08 21:51 | +10 stop | ZEC | UP | 0.59 | 0.44 | -1.85 |
| 11-08 21:51 | +5 | ZEC | UP | 0.60 | no | -6.22 |
| 11-08 21:49 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.20 |
| 11-08 21:49 | +10 stop | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-08 21:48 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 11-08 21:48 | +10 stop | NEAR | DOWN | 0.63 | 0.95 | 2.96 |
| 11-08 21:48 | +10 | NEAR | DOWN | 0.63 | 0.95 | 2.96 |
| 11-08 21:48 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 11-08 21:47 | +5 | ZEC | UP | 0.53 | 0.60 | 0.35 |
| 11-08 21:47 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-08 21:47 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 21:47 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-08 21:47 | +10 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-08 21:47 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-08 21:47 | +10 stop | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 11-08 21:47 | +20 | XRP | DOWN | 0.53 | 0.87 | 3.14 |
| 11-08 21:47 | +15 | XRP | DOWN | 0.54 | 0.87 | 3.04 |
| 11-08 21:47 | +10 | XRP | DOWN | 0.54 | 0.87 | 3.04 |
| 11-08 21:47 | +5 | XRP | DOWN | 0.54 | 0.63 | 0.55 |
| 11-08 21:46 | +10 stop | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-08 21:46 | +20 | NEAR | UP | 0.60 | no | -6.17 |
| 11-08 21:46 | +15 | NEAR | UP | 0.60 | no | -6.17 |
| 11-08 21:46 | +10 | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-08 21:46 | +5 | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-08 21:46 | +10 stop | ZEC | UP | 0.69 | 0.52 | -2.03 |
| 11-08 21:46 | +20 | ZEC | UP | 0.69 | no | -7.05 |
| 11-08 21:46 | +15 | ZEC | UP | 0.69 | no | -7.05 |
| 11-08 21:46 | +10 | ZEC | UP | 0.69 | no | -7.05 |
| 11-08 21:46 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 11-08 21:46 | +10 stop | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-08 21:46 | +20 | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-08 21:46 | +15 | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-08 21:46 | +10 | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
