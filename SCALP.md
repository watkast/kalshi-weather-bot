# Range-Scalp Bot

*Updated Tue Nov 10 15:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54643 | 47665 | 6978 (91) | 0 | $-14868.80 | -4.3% |
| **+10¢** | 40831 | 32687 | 8144 (121) | 0 | $-13802.96 | -5.4% |
| **+15¢** | 34229 | 25449 | 8780 (155) | 0 | $-12559.88 | -5.8% |
| **+20¢** | 30477 | 21265 | 9212 (204) | 0 | $-10982.07 | -5.7% |
| **+10¢ (15¢ stop)** | 66570 | 66456 | 114 (70) | 0 | $-24580.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 14:59 | +10 stop | DOGE | DOWN | 0.14 | 0.67 | 5.05 |
| 11-10 14:59 | +20 | DOGE | DOWN | 0.15 | 0.67 | 4.95 |
| 11-10 14:59 | +15 | DOGE | DOWN | 0.16 | 0.67 | 4.84 |
| 11-10 14:59 | +10 | DOGE | DOWN | 0.20 | 0.67 | 4.46 |
| 11-10 14:59 | +5 | DOGE | DOWN | 0.16 | 0.67 | 4.84 |
| 11-10 14:59 | +10 stop | ETH | UP | 0.51 | 0.92 | 3.91 |
| 11-10 14:59 | +10 | ETH | UP | 0.63 | 0.92 | 2.75 |
| 11-10 14:59 | +5 | ETH | UP | 0.63 | 0.92 | 2.69 |
| 11-10 14:58 | +10 stop | BTC | DOWN | 0.40 | 0.61 | 1.79 |
| 11-10 14:57 | +10 stop | ETH | DOWN | 0.70 | 0.49 | -2.43 |
| 11-10 14:57 | +10 stop | ZEC | UP | 0.38 | 0.57 | 1.55 |
| 11-10 14:57 | +15 | HYPE | DOWN | 0.40 | 0.60 | 1.66 |
| 11-10 14:57 | +10 | HYPE | DOWN | 0.40 | 0.60 | 1.66 |
| 11-10 14:57 | +5 | HYPE | DOWN | 0.40 | 0.60 | 1.66 |
| 11-10 14:56 | +10 stop | HYPE | DOWN | 0.41 | 0.60 | 1.56 |
| 11-10 14:56 | +10 stop | BTC | DOWN | 0.68 | 0.50 | -2.14 |
| 11-10 14:56 | +10 | BTC | DOWN | 0.63 | yes | -6.47 |
| 11-10 14:56 | +5 | BTC | DOWN | 0.63 | yes | -6.47 |
| 11-10 14:56 | +10 stop | ETH | DOWN | 0.65 | 0.45 | -2.34 |
| 11-10 14:56 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 11-10 14:56 | +10 | BNB | UP | 0.60 | 0.70 | 0.68 |
| 11-10 14:56 | +10 stop | HYPE | UP | 0.34 | 0.58 | 2.06 |
| 11-10 14:56 | +10 stop | BTC | UP | 0.48 | 0.62 | 1.05 |
| 11-10 14:56 | +20 | BTC | UP | 0.48 | 0.85 | 3.43 |
| 11-10 14:56 | +15 | BTC | UP | 0.48 | 0.85 | 3.43 |
| 11-10 14:56 | +10 | BTC | UP | 0.49 | 0.62 | 0.95 |
| 11-10 14:56 | +5 | BTC | UP | 0.50 | 0.62 | 0.85 |
| 11-10 14:56 | +10 stop | ZEC | UP | 0.62 | 0.40 | -2.54 |
| 11-10 14:56 | +10 | ZEC | UP | 0.62 | no | -6.37 |
| 11-10 14:56 | +5 | ZEC | UP | 0.62 | no | -6.37 |
| 11-10 14:55 | +10 stop | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 14:55 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 14:55 | +15 | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 14:55 | +10 | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 14:55 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 14:55 | +10 stop | XRP | DOWN | 0.45 | 0.57 | 0.84 |
| 11-10 14:55 | +20 | XRP | DOWN | 0.46 | 0.77 | 2.79 |
| 11-10 14:55 | +15 | XRP | DOWN | 0.47 | 0.62 | 1.15 |
| 11-10 14:55 | +10 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-10 14:55 | +5 | XRP | DOWN | 0.46 | 0.57 | 0.74 |
