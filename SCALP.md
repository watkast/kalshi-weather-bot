# Range-Scalp Bot

*Updated Sun Nov 08 16:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52508 | 45774 | 6734 (83) | 3 | $-14584.49 | -4.4% |
| **+10¢** | 39197 | 31352 | 7845 (108) | 3 | $-13555.63 | -5.5% |
| **+15¢** | 32837 | 24382 | 8455 (138) | 4 | $-12426.76 | -6.0% |
| **+20¢** | 29209 | 20349 | 8860 (182) | 4 | $-10925.91 | -6.0% |
| **+10¢ (15¢ stop)** | 63954 | 63848 | 106 (63) | 0 | $-23704.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 16:25 | +5 | HYPE | UP | 0.61 | 0.78 | 1.40 |
| 11-08 16:25 | +10 stop | HYPE | UP | 0.61 | 0.78 | 1.37 |
| 11-08 16:25 | +10 stop | HYPE | DOWN | 0.44 | 0.64 | 1.65 |
| 11-08 16:24 | +10 stop | BNB | UP | 0.66 | 0.50 | -1.89 |
| 11-08 16:24 | +10 stop | ETH | UP | 0.63 | 0.77 | 1.10 |
| 11-08 16:24 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 11-08 16:23 | +10 stop | BNB | DOWN | 0.69 | 0.51 | -2.13 |
| 11-08 16:23 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-08 16:23 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-08 16:23 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-08 16:23 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-08 16:23 | +10 stop | NEAR | DOWN | 0.69 | 0.51 | -2.13 |
| 11-08 16:22 | +15 | ETH | DOWN | 0.65 | open |  |
| 11-08 16:21 | +10 stop | DOGE | DOWN | 0.64 | 0.29 | -3.82 |
| 11-08 16:21 | +10 stop | BTC | DOWN | 0.62 | 0.27 | -3.81 |
| 11-08 16:21 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-08 16:21 | +10 stop | ETH | DOWN | 0.64 | 0.39 | -2.84 |
| 11-08 16:20 | +5 | ZEC | DOWN | 0.70 | 0.90 | 1.82 |
| 11-08 16:20 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 11-08 16:20 | +5 | ETH | UP | 0.54 | 0.60 | 0.25 |
| 11-08 16:19 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-08 16:19 | +10 stop | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-08 16:18 | +10 stop | ZEC | DOWN | 0.53 | 0.63 | 0.65 |
| 11-08 16:18 | +5 | ZEC | DOWN | 0.53 | 0.62 | 0.55 |
| 11-08 16:17 | +10 stop | BTC | UP | 0.57 | 0.36 | -2.45 |
| 11-08 16:17 | +20 | BTC | UP | 0.57 | 0.86 | 2.63 |
| 11-08 16:17 | +15 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 11-08 16:17 | +10 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 11-08 16:17 | +5 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 11-08 16:17 | +10 stop | BNB | UP | 0.54 | 0.30 | -2.68 |
| 11-08 16:17 | +10 stop | HYPE | UP | 0.53 | 0.30 | -2.63 |
| 11-08 16:17 | +20 | HYPE | UP | 0.53 | 0.78 | 2.19 |
| 11-08 16:17 | +15 | HYPE | UP | 0.53 | 0.78 | 2.19 |
| 11-08 16:17 | +10 | HYPE | UP | 0.53 | 0.78 | 2.19 |
| 11-08 16:17 | +5 | HYPE | UP | 0.53 | 0.60 | 0.35 |
| 11-08 16:17 | +10 stop | ETH | UP | 0.60 | 0.41 | -2.24 |
| 11-08 16:17 | +10 | ETH | UP | 0.60 | 0.77 | 1.40 |
| 11-08 16:17 | +5 | ETH | UP | 0.60 | 0.66 | 0.27 |
| 11-08 16:17 | +10 stop | DOGE | UP | 0.55 | 0.39 | -1.95 |
| 11-08 16:17 | +20 | DOGE | UP | 0.55 | 0.78 | 1.99 |
