# Range-Scalp Bot

*Updated Sat Nov 21 00:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66773 | 58273 | 8500 (128) | 1 | $-17964.18 | -4.3% |
| **+10¢** | 49865 | 39932 | 9933 (170) | 1 | $-16690.52 | -5.3% |
| **+15¢** | 41819 | 31110 | 10709 (217) | 2 | $-14992.20 | -5.7% |
| **+20¢** | 37223 | 25975 | 11248 (273) | 3 | $-13294.93 | -5.7% |
| **+10¢ (15¢ stop)** | 81314 | 81148 | 166 (100) | 0 | $-30007.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 00:43 | +10 | ZEC | DOWN | 0.32 | 0.65 | 2.98 |
| 11-21 00:43 | +10 stop | ZEC | DOWN | 0.36 | 0.65 | 2.57 |
| 11-21 00:43 | +5 | ZEC | DOWN | 0.25 | 0.65 | 3.70 |
| 11-21 00:42 | +10 stop | BNB | DOWN | 0.66 | 0.95 | 2.74 |
| 11-21 00:42 | +15 | BNB | DOWN | 0.66 | 0.95 | 2.74 |
| 11-21 00:42 | +10 | BNB | DOWN | 0.66 | 0.95 | 2.74 |
| 11-21 00:42 | +5 | BNB | DOWN | 0.66 | 0.95 | 2.74 |
| 11-21 00:41 | +10 stop | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 11-21 00:41 | +5 | ZEC | UP | 0.68 | 0.77 | 0.61 |
| 11-21 00:40 | +10 stop | ZEC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-21 00:40 | +10 | ZEC | DOWN | 0.52 | 0.63 | 0.75 |
| 11-21 00:40 | +5 | ZEC | DOWN | 0.52 | 0.61 | 0.55 |
| 11-21 00:39 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
| 11-21 00:39 | +15 | SOL | DOWN | 0.56 | 0.73 | 1.38 |
| 11-21 00:39 | +10 | SOL | DOWN | 0.56 | 0.73 | 1.38 |
| 11-21 00:39 | +5 | SOL | DOWN | 0.56 | 0.64 | 0.45 |
| 11-21 00:39 | +10 stop | ZEC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-21 00:38 | +10 stop | HYPE | DOWN | 0.70 | 0.49 | -2.40 |
| 11-21 00:38 | +10 stop | NEAR | DOWN | 0.69 | 0.34 | -3.81 |
| 11-21 00:38 | +10 stop | BTC | UP | 0.61 | 0.84 | 2.03 |
| 11-21 00:38 | +20 | BTC | UP | 0.60 | 0.84 | 2.13 |
| 11-21 00:38 | +15 | BTC | UP | 0.60 | 0.84 | 2.13 |
| 11-21 00:38 | +10 | BTC | UP | 0.60 | 0.84 | 2.13 |
| 11-21 00:38 | +5 | BTC | UP | 0.60 | 0.84 | 2.13 |
| 11-21 00:38 | +10 stop | ETH | UP | 0.60 | 0.74 | 1.09 |
| 11-21 00:38 | +20 | ETH | UP | 0.60 | 0.87 | 2.45 |
| 11-21 00:38 | +15 | ETH | UP | 0.60 | 0.76 | 1.30 |
| 11-21 00:38 | +10 | ETH | UP | 0.60 | 0.74 | 1.09 |
| 11-21 00:38 | +5 | ETH | UP | 0.60 | 0.74 | 1.09 |
| 11-21 00:38 | +10 stop | HYPE | UP | 0.71 | 0.39 | -3.52 |
| 11-21 00:38 | +10 | HYPE | UP | 0.71 | open |  |
| 11-21 00:38 | +5 | HYPE | UP | 0.71 | open |  |
| 11-21 00:38 | +10 stop | NEAR | UP | 0.65 | 0.38 | -3.03 |
| 11-21 00:38 | +20 | NEAR | UP | 0.65 | 0.91 | 2.32 |
| 11-21 00:38 | +15 | NEAR | UP | 0.65 | 0.91 | 2.32 |
| 11-21 00:38 | +10 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 11-21 00:38 | +5 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 11-21 00:36 | +10 stop | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 11-21 00:34 | +10 stop | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 11-21 00:34 | +10 stop | HYPE | UP | 0.62 | 0.47 | -1.85 |
