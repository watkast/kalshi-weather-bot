# Range-Scalp Bot

*Updated Sat Nov 07 18:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51312 | 44737 | 6575 (79) | 3 | $-14285.15 | -4.4% |
| **+10¢** | 38300 | 30636 | 7664 (105) | 3 | $-13271.57 | -5.5% |
| **+15¢** | 32061 | 23800 | 8261 (134) | 6 | $-12198.04 | -6.1% |
| **+20¢** | 28518 | 19859 | 8659 (177) | 5 | $-10762.32 | -6.0% |
| **+10¢ (15¢ stop)** | 62511 | 62408 | 103 (61) | 1 | $-23132.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 18:09 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-07 18:09 | +20 | ZEC | UP | 0.62 | open |  |
| 11-07 18:09 | +15 | ZEC | UP | 0.60 | open |  |
| 11-07 18:09 | +10 | ZEC | UP | 0.61 | 0.72 | 0.78 |
| 11-07 18:09 | +5 | ZEC | UP | 0.60 | 0.72 | 0.88 |
| 11-07 18:09 | +10 stop | BTC | UP | 0.68 | open |  |
| 11-07 18:08 | +10 stop | XRP | DOWN | 0.55 | 0.32 | -2.64 |
| 11-07 18:07 | +10 stop | DOGE | UP | 0.70 | 0.48 | -2.53 |
| 11-07 18:07 | +20 | DOGE | UP | 0.70 | 0.94 | 2.17 |
| 11-07 18:07 | +15 | DOGE | UP | 0.70 | 0.94 | 2.17 |
| 11-07 18:07 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 11-07 18:07 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 11-07 18:07 | +10 stop | ETH | DOWN | 0.43 | 0.57 | 1.04 |
| 11-07 18:07 | +10 | ETH | DOWN | 0.43 | 0.57 | 1.04 |
| 11-07 18:07 | +5 | ETH | DOWN | 0.43 | 0.57 | 1.04 |
| 11-07 18:07 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-07 18:07 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-07 18:06 | +10 stop | XRP | UP | 0.55 | 0.39 | -1.95 |
| 11-07 18:06 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-07 18:05 | +10 stop | SOL | UP | 0.70 | 0.48 | -2.53 |
| 11-07 18:05 | +10 | SOL | UP | 0.69 | 0.82 | 1.04 |
| 11-07 18:05 | +5 | SOL | UP | 0.69 | 0.82 | 1.04 |
| 11-07 18:05 | +10 stop | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-07 18:04 | +10 stop | XRP | DOWN | 0.70 | 0.47 | -2.63 |
| 11-07 18:03 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-07 18:03 | +10 stop | BTC | DOWN | 0.60 | 0.35 | -2.83 |
| 11-07 18:03 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-07 18:03 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-07 18:03 | +10 | BTC | DOWN | 0.60 | open |  |
| 11-07 18:03 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-07 18:03 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-07 18:03 | +10 | DOGE | UP | 0.67 | 0.79 | 0.96 |
| 11-07 18:03 | +5 | DOGE | UP | 0.67 | 0.76 | 0.65 |
| 11-07 18:03 | +10 stop | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 11-07 18:03 | +10 stop | XRP | UP | 0.67 | 0.48 | -2.24 |
| 11-07 18:03 | +15 | XRP | UP | 0.68 | open |  |
| 11-07 18:03 | +10 | XRP | UP | 0.68 | 0.79 | 0.87 |
| 11-07 18:03 | +5 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 11-07 18:03 | +5 | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 11-07 18:03 | +5 | ETH | DOWN | 0.60 | 0.73 | 0.99 |
