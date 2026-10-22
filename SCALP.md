# Range-Scalp Bot

*Updated Thu Oct 22 05:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28360 | 24709 | 3651 (39) | 0 | $-8176.65 | -4.6% |
| **+10¢** | 21286 | 17061 | 4225 (55) | 0 | $-7282.73 | -5.4% |
| **+15¢** | 17833 | 13288 | 4545 (78) | 0 | $-6509.89 | -5.8% |
| **+20¢** | 15777 | 11011 | 4766 (98) | 0 | $-5888.31 | -5.9% |
| **+10¢ (15¢ stop)** | 34797 | 34738 | 59 (32) | 0 | $-13066.20 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 05:24 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 10-22 05:24 | +10 stop | DOGE | DOWN | 0.67 | 0.48 | -2.24 |
| 10-22 05:23 | +10 stop | ZEC | DOWN | 0.64 | 0.38 | -2.94 |
| 10-22 05:23 | +10 stop | ETH | DOWN | 0.53 | 0.33 | -2.34 |
| 10-22 05:23 | +10 stop | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 10-22 05:23 | +10 stop | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-22 05:22 | +10 stop | SOL | UP | 0.63 | 0.45 | -2.15 |
| 10-22 05:22 | +10 stop | DOGE | UP | 0.55 | 0.37 | -2.15 |
| 10-22 05:22 | +5 | DOGE | UP | 0.55 | 0.74 | 1.58 |
| 10-22 05:22 | +10 stop | ETH | UP | 0.68 | 0.43 | -2.84 |
| 10-22 05:21 | +10 stop | ZEC | UP | 0.71 | 0.38 | -3.62 |
| 10-22 05:20 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-22 05:20 | +10 stop | ETH | UP | 0.53 | 0.68 | 1.16 |
| 10-22 05:20 | +10 stop | XRP | UP | 0.57 | 0.78 | 1.79 |
| 10-22 05:19 | +10 stop | ZEC | DOWN | 0.55 | 0.35 | -2.38 |
| 10-22 05:19 | +10 | ZEC | DOWN | 0.55 | yes | -5.72 |
| 10-22 05:19 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.41 |
| 10-22 05:19 | +10 stop | DOGE | UP | 0.66 | 0.80 | 1.12 |
| 10-22 05:19 | +5 | DOGE | UP | 0.66 | 0.73 | 0.40 |
| 10-22 05:19 | +5 | SOL | DOWN | 0.69 | yes | -7.05 |
| 10-22 05:18 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.99 |
| 10-22 05:18 | +10 | HYPE | DOWN | 0.64 | yes | -6.61 |
| 10-22 05:18 | +5 | HYPE | DOWN | 0.64 | yes | -6.61 |
| 10-22 05:18 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 10-22 05:18 | +5 | DOGE | DOWN | 0.51 | 0.61 | 0.65 |
| 10-22 05:17 | +5 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-22 05:17 | +10 stop | NEAR | UP | 0.58 | 0.72 | 1.07 |
| 10-22 05:17 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-22 05:17 | +20 | BTC | UP | 0.60 | 0.84 | 2.13 |
| 10-22 05:17 | +15 | BTC | UP | 0.60 | 0.76 | 1.30 |
| 10-22 05:17 | +10 | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-22 05:17 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 10-22 05:16 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
| 10-22 05:16 | +10 stop | ETH | DOWN | 0.67 | 0.44 | -2.64 |
| 10-22 05:16 | +20 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-22 05:16 | +15 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-22 05:16 | +10 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-22 05:16 | +5 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-22 05:16 | +10 stop | NEAR | DOWN | 0.56 | 0.38 | -2.14 |
| 10-22 05:16 | +20 | NEAR | DOWN | 0.56 | yes | -5.77 |
