# Range-Scalp Bot

*Updated Sun Oct 11 21:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12523 | 10808 | 1715 (25) | 0 | $-4145.00 | -5.2% |
| **+10¢** | 9505 | 7518 | 1987 (37) | 0 | $-3901.17 | -6.5% |
| **+15¢** | 8004 | 5891 | 2113 (55) | 0 | $-3349.22 | -6.7% |
| **+20¢** | 7136 | 4934 | 2202 (69) | 0 | $-2837.53 | -6.3% |
| **+10¢ (15¢ stop)** | 15425 | 15384 | 41 (25) | 0 | $-6047.14 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 21:12 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-11 21:12 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-11 21:12 | +15 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-11 21:12 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-11 21:12 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
| 10-11 21:12 | +10 stop | NEAR | UP | 0.35 | 0.64 | 2.57 |
| 10-11 21:12 | +20 | NEAR | UP | 0.35 | 0.64 | 2.56 |
| 10-11 21:12 | +15 | NEAR | UP | 0.35 | 0.64 | 2.57 |
| 10-11 21:12 | +10 | NEAR | UP | 0.35 | 0.64 | 2.57 |
| 10-11 21:12 | +5 | NEAR | UP | 0.35 | 0.64 | 2.57 |
| 10-11 21:11 | +10 stop | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-11 21:11 | +10 | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-11 21:10 | +5 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-11 21:09 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-11 21:09 | +20 | BTC | DOWN | 0.59 | 0.85 | 2.34 |
| 10-11 21:09 | +15 | BTC | DOWN | 0.59 | 0.85 | 2.34 |
| 10-11 21:09 | +10 | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-11 21:09 | +5 | BTC | DOWN | 0.58 | 0.66 | 0.46 |
| 10-11 21:05 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 10-11 21:04 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-11 21:04 | +10 stop | BTC | UP | 0.50 | 0.30 | -2.33 |
| 10-11 21:04 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 10-11 21:03 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-11 21:03 | +5 | ZEC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-11 21:02 | +10 stop | NEAR | UP | 0.60 | 0.45 | -1.85 |
| 10-11 21:02 | +20 | NEAR | UP | 0.60 | 0.84 | 2.13 |
| 10-11 21:02 | +15 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-11 21:02 | +10 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-11 21:02 | +5 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-11 21:02 | +5 | XRP | DOWN | 0.54 | 0.61 | 0.35 |
| 10-11 21:02 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 21:02 | +20 | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 10-11 21:02 | +15 | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 10-11 21:02 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 21:02 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 21:02 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 10-11 21:01 | +10 stop | BTC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-11 21:01 | +20 | BTC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 21:01 | +15 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-11 21:01 | +10 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
