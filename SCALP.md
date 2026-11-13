# Range-Scalp Bot

*Updated Fri Nov 13 19:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58527 | 51073 | 7454 (105) | 5 | $-15746.68 | -4.3% |
| **+10¢** | 43725 | 35006 | 8719 (139) | 6 | $-14717.81 | -5.4% |
| **+15¢** | 36647 | 27255 | 9392 (174) | 5 | $-13302.23 | -5.8% |
| **+20¢** | 32645 | 22785 | 9860 (225) | 7 | $-11684.80 | -5.7% |
| **+10¢ (15¢ stop)** | 71264 | 71130 | 134 (82) | 3 | $-26212.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 19:20 | +10 stop | SOL | UP | 0.46 | 0.57 | 0.74 |
| 11-13 19:20 | +10 stop | DOGE | UP | 0.49 | open |  |
| 11-13 19:20 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-13 19:19 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-13 19:18 | +10 stop | BNB | UP | 0.70 | 0.48 | -2.53 |
| 11-13 19:18 | +10 | BNB | UP | 0.70 | open |  |
| 11-13 19:18 | +5 | BNB | UP | 0.70 | open |  |
| 11-13 19:18 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 11-13 19:18 | +10 | ETH | UP | 0.69 | open |  |
| 11-13 19:17 | +5 | XRP | UP | 0.70 | 0.75 | 0.25 |
| 11-13 19:17 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 11-13 19:17 | +10 stop | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-13 19:17 | +20 | ZEC | UP | 0.65 | 0.93 | 2.57 |
| 11-13 19:17 | +15 | ZEC | UP | 0.65 | 0.93 | 2.57 |
| 11-13 19:17 | +10 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-13 19:17 | +5 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-13 19:17 | +10 stop | ETH | UP | 0.54 | 0.64 | 0.65 |
| 11-13 19:17 | +20 | ETH | UP | 0.54 | open |  |
| 11-13 19:17 | +15 | ETH | UP | 0.54 | 0.69 | 1.17 |
| 11-13 19:17 | +10 | ETH | UP | 0.54 | 0.64 | 0.65 |
| 11-13 19:17 | +5 | ETH | UP | 0.54 | 0.62 | 0.45 |
| 11-13 19:16 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-13 19:16 | +20 | BTC | UP | 0.69 | open |  |
| 11-13 19:16 | +15 | BTC | UP | 0.69 | open |  |
| 11-13 19:16 | +10 | BTC | UP | 0.69 | open |  |
| 11-13 19:16 | +5 | BTC | UP | 0.69 | open |  |
| 11-13 19:16 | +10 stop | DOGE | UP | 0.64 | 0.43 | -2.45 |
| 11-13 19:16 | +20 | DOGE | UP | 0.64 | open |  |
| 11-13 19:16 | +15 | DOGE | UP | 0.69 | open |  |
| 11-13 19:16 | +10 | DOGE | UP | 0.69 | open |  |
| 11-13 19:16 | +5 | DOGE | UP | 0.69 | open |  |
| 11-13 19:16 | +10 stop | SOL | UP | 0.63 | 0.40 | -2.64 |
| 11-13 19:16 | +20 | SOL | UP | 0.63 | open |  |
| 11-13 19:16 | +15 | SOL | UP | 0.63 | open |  |
| 11-13 19:16 | +10 | SOL | UP | 0.63 | open |  |
| 11-13 19:16 | +5 | SOL | UP | 0.63 | open |  |
| 11-13 19:16 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 11-13 19:16 | +20 | BNB | UP | 0.62 | open |  |
| 11-13 19:16 | +15 | BNB | UP | 0.62 | open |  |
| 11-13 19:16 | +10 | BNB | UP | 0.62 | 0.72 | 0.68 |
