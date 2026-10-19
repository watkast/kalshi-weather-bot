# Range-Scalp Bot

*Updated Mon Oct 19 09:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23770 | 20665 | 3105 (31) | 0 | $-7105.27 | -4.7% |
| **+10¢** | 17887 | 14311 | 3576 (45) | 0 | $-6319.03 | -5.6% |
| **+15¢** | 14982 | 11132 | 3850 (67) | 0 | $-5721.05 | -6.1% |
| **+20¢** | 13264 | 9237 | 4027 (86) | 0 | $-5072.08 | -6.1% |
| **+10¢ (15¢ stop)** | 29248 | 29197 | 51 (30) | 0 | $-11035.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 08:56 | +10 stop | HYPE | DOWN | 0.49 | 0.59 | 0.65 |
| 10-19 08:56 | +10 stop | ZEC | UP | 0.53 | 0.24 | -3.22 |
| 10-19 08:56 | +10 stop | BTC | UP | 0.62 | 0.78 | 1.30 |
| 10-19 08:56 | +10 stop | HYPE | UP | 0.49 | 0.60 | 0.75 |
| 10-19 08:55 | +10 stop | BTC | DOWN | 0.61 | 0.36 | -2.84 |
| 10-19 08:55 | +20 | BTC | DOWN | 0.61 | 0.91 | 2.80 |
| 10-19 08:55 | +15 | BTC | DOWN | 0.61 | 0.91 | 2.80 |
| 10-19 08:55 | +10 | BTC | DOWN | 0.61 | 0.91 | 2.80 |
| 10-19 08:55 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-19 08:55 | +10 stop | ZEC | DOWN | 0.58 | 0.35 | -2.64 |
| 10-19 08:55 | +10 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 10-19 08:55 | +5 | ZEC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-19 08:51 | +5 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-19 08:50 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-19 08:48 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-19 08:48 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-19 08:48 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-19 08:47 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-19 08:47 | +5 | DOGE | DOWN | 0.56 | 0.64 | 0.45 |
| 10-19 08:47 | +10 stop | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-19 08:47 | +20 | BTC | DOWN | 0.56 | 0.79 | 2.00 |
| 10-19 08:47 | +15 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-19 08:47 | +10 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-19 08:47 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 10-19 08:46 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.28 |
| 10-19 08:46 | +20 | HYPE | UP | 0.66 | no | -6.80 |
| 10-19 08:46 | +15 | HYPE | UP | 0.66 | no | -6.80 |
| 10-19 08:46 | +10 | HYPE | UP | 0.66 | no | -6.80 |
| 10-19 08:46 | +5 | HYPE | UP | 0.66 | no | -6.80 |
| 10-19 08:46 | +10 stop | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-19 08:46 | +20 | ETH | DOWN | 0.54 | 0.80 | 2.30 |
| 10-19 08:46 | +15 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-19 08:46 | +10 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-19 08:46 | +5 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-19 08:46 | +10 stop | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-19 08:46 | +20 | NEAR | DOWN | 0.63 | 0.89 | 2.36 |
| 10-19 08:46 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-19 08:46 | +10 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-19 08:46 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.32 |
| 10-19 08:46 | +10 stop | XRP | DOWN | 0.58 | 0.74 | 1.28 |
