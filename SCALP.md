# Range-Scalp Bot

*Updated Sun Oct 04 17:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2534 | 2183 | 351 (3) | 4 | $-844.53 | -5.3% |
| **+10¢** | 1984 | 1592 | 392 (4) | 6 | $-655.02 | -5.2% |
| **+15¢** | 1662 | 1250 | 412 (5) | 6 | $-536.16 | -5.1% |
| **+20¢** | 1477 | 1045 | 432 (9) | 8 | $-449.00 | -4.8% |
| **+10¢ (15¢ stop)** | 3149 | 3148 | 1 (1) | 0 | $-1165.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 17:10 | +10 stop | NEAR | DOWN | 0.66 | 0.44 | -2.54 |
| 10-04 17:10 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-04 17:10 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-04 17:10 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-04 17:10 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-04 17:09 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 10-04 17:09 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-04 17:09 | +5 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-04 17:08 | +10 stop | HYPE | DOWN | 0.67 | 0.83 | 1.30 |
| 10-04 17:08 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.44 |
| 10-04 17:08 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-04 17:08 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 10-04 17:08 | +10 stop | NEAR | UP | 0.38 | 0.56 | 1.45 |
| 10-04 17:08 | +20 | NEAR | UP | 0.40 | 0.79 | 3.66 |
| 10-04 17:08 | +15 | NEAR | UP | 0.40 | 0.56 | 1.30 |
| 10-04 17:08 | +10 | NEAR | UP | 0.40 | 0.56 | 1.30 |
| 10-04 17:08 | +5 | NEAR | UP | 0.40 | 0.56 | 1.30 |
| 10-04 17:07 | +5 | HYPE | UP | 0.44 | 0.54 | 0.64 |
| 10-04 17:06 | +10 stop | ZEC | UP | 0.60 | 0.37 | -2.63 |
| 10-04 17:06 | +20 | ZEC | UP | 0.60 | open |  |
| 10-04 17:06 | +15 | ZEC | UP | 0.60 | open |  |
| 10-04 17:06 | +10 | ZEC | UP | 0.60 | open |  |
| 10-04 17:06 | +5 | ZEC | UP | 0.60 | open |  |
| 10-04 17:06 | +10 stop | ETH | UP | 0.62 | 0.31 | -3.42 |
| 10-04 17:06 | +10 stop | HYPE | UP | 0.63 | 0.45 | -2.17 |
| 10-04 17:06 | +10 | HYPE | UP | 0.63 | open |  |
| 10-04 17:06 | +5 | HYPE | UP | 0.63 | 0.70 | 0.36 |
| 10-04 17:05 | +10 stop | SOL | UP | 0.58 | 0.22 | -3.91 |
| 10-04 17:05 | +20 | SOL | UP | 0.58 | open |  |
| 10-04 17:05 | +15 | SOL | UP | 0.59 | open |  |
| 10-04 17:05 | +10 | SOL | UP | 0.59 | open |  |
| 10-04 17:05 | +5 | SOL | UP | 0.59 | open |  |
| 10-04 17:05 | +10 stop | XRP | UP | 0.69 | 0.38 | -3.42 |
| 10-04 17:05 | +20 | XRP | UP | 0.69 | open |  |
| 10-04 17:05 | +15 | XRP | UP | 0.69 | open |  |
| 10-04 17:05 | +10 | XRP | UP | 0.69 | open |  |
| 10-04 17:05 | +5 | XRP | UP | 0.69 | open |  |
| 10-04 17:04 | +5 | DOGE | UP | 0.68 | 0.86 | 1.55 |
| 10-04 17:04 | +10 stop | BNB | UP | 0.64 | 0.79 | 1.21 |
| 10-04 17:04 | +20 | BNB | UP | 0.64 | open |  |
