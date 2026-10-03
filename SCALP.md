# Range-Scalp Bot

*Updated Sat Oct 03 04:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 199 | 170 | 29 (1) | 1 | $-76.09 | -6.0% |
| **+10¢** | 164 | 134 | 30 (1) | 2 | $-36.93 | -3.5% |
| **+15¢** | 135 | 105 | 30 (1) | 4 | $-22.79 | -2.7% |
| **+20¢** | 338 | 241 | 97 (2) | 6 | $-82.92 | -3.9% |
| **+10¢ (15¢ stop)** | 272 | 272 | 0 (0) | 2 | $-125.22 | -7.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 04:47 | +10 stop | ZEC | UP | 0.70 | open |  |
| 10-03 04:47 | +20 | ZEC | UP | 0.70 | open |  |
| 10-03 04:47 | +15 | ZEC | UP | 0.70 | open |  |
| 10-03 04:47 | +10 | ZEC | UP | 0.70 | open |  |
| 10-03 04:47 | +5 | ZEC | UP | 0.70 | open |  |
| 10-03 04:46 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.85 |
| 10-03 04:46 | +20 | NEAR | UP | 0.70 | open |  |
| 10-03 04:46 | +15 | NEAR | UP | 0.70 | open |  |
| 10-03 04:46 | +10 | NEAR | UP | 0.70 | 0.81 | 0.85 |
| 10-03 04:46 | +5 | NEAR | UP | 0.70 | 0.78 | 0.53 |
| 10-03 04:46 | +10 stop | XRP | UP | 0.60 | 0.74 | 1.09 |
| 10-03 04:46 | +20 | XRP | UP | 0.60 | 0.82 | 1.92 |
| 10-03 04:46 | +15 | XRP | UP | 0.60 | 0.77 | 1.40 |
| 10-03 04:46 | +10 | XRP | UP | 0.60 | 0.74 | 1.09 |
| 10-03 04:46 | +5 | XRP | UP | 0.60 | 0.68 | 0.47 |
| 10-03 04:46 | +10 stop | BTC | UP | 0.68 | open |  |
| 10-03 04:46 | +20 | BTC | UP | 0.68 | open |  |
| 10-03 04:46 | +15 | BTC | UP | 0.68 | open |  |
| 10-03 04:46 | +10 | BTC | UP | 0.68 | open |  |
| 10-03 04:46 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 10-03 04:46 | +10 stop | DOGE | UP | 0.67 | 0.81 | 1.13 |
| 10-03 04:46 | +20 | DOGE | UP | 0.67 | open |  |
| 10-03 04:46 | +15 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 10-03 04:46 | +10 | DOGE | UP | 0.67 | 0.81 | 1.13 |
| 10-03 04:46 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 10-03 04:46 | +10 stop | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-03 04:46 | +20 | ETH | UP | 0.61 | open |  |
| 10-03 04:46 | +15 | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-03 04:46 | +10 | ETH | UP | 0.62 | 0.76 | 1.10 |
| 10-03 04:46 | +5 | ETH | UP | 0.61 | 0.69 | 0.48 |
| 10-03 04:46 | +10 stop | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 10-03 04:46 | +20 | HYPE | UP | 0.65 | open |  |
| 10-03 04:46 | +15 | HYPE | UP | 0.65 | open |  |
| 10-03 04:46 | +10 | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 10-03 04:46 | +5 | HYPE | UP | 0.66 | 0.72 | 0.30 |
| 10-03 04:42 | +10 stop | ZEC | UP | 0.53 | 0.64 | 0.80 |
| 10-03 04:42 | +10 | ZEC | UP | 0.53 | 0.64 | 0.80 |
| 10-03 04:42 | +5 | ZEC | UP | 0.60 | 0.79 | 1.61 |
| 10-03 04:42 | +10 stop | SOL | DOWN | 0.71 | 0.15 | -5.84 |
| 10-03 04:42 | +10 stop | ZEC | UP | 0.47 | 0.59 | 0.90 |
