# Range-Scalp Bot

*Updated Sat Oct 24 14:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32102 | 27987 | 4115 (40) | 5 | $-9187.82 | -4.5% |
| **+10¢** | 24025 | 19265 | 4760 (58) | 6 | $-8206.32 | -5.4% |
| **+15¢** | 20113 | 14993 | 5120 (81) | 6 | $-7355.11 | -5.8% |
| **+20¢** | 17818 | 12458 | 5360 (103) | 7 | $-6533.22 | -5.8% |
| **+10¢ (15¢ stop)** | 39449 | 39390 | 59 (32) | 3 | $-15105.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 14:09 | +10 stop | HYPE | DOWN | 0.38 | 0.52 | 1.05 |
| 10-24 14:09 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 10-24 14:09 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 10-24 14:09 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-24 14:09 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-24 14:08 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.85 |
| 10-24 14:08 | +20 | BNB | UP | 0.64 | open |  |
| 10-24 14:08 | +15 | BNB | UP | 0.64 | open |  |
| 10-24 14:08 | +10 | BNB | UP | 0.64 | open |  |
| 10-24 14:08 | +5 | BNB | UP | 0.64 | open |  |
| 10-24 14:08 | +10 stop | ZEC | UP | 0.50 | 0.28 | -2.53 |
| 10-24 14:08 | +20 | ZEC | UP | 0.47 | open |  |
| 10-24 14:08 | +15 | ZEC | UP | 0.47 | open |  |
| 10-24 14:08 | +10 | ZEC | UP | 0.47 | open |  |
| 10-24 14:08 | +5 | ZEC | UP | 0.47 | 0.55 | 0.44 |
| 10-24 14:07 | +5 | HYPE | UP | 0.63 | 0.71 | 0.48 |
| 10-24 14:06 | +10 stop | SOL | UP | 0.65 | 0.50 | -1.84 |
| 10-24 14:06 | +15 | SOL | UP | 0.64 | open |  |
| 10-24 14:06 | +10 | SOL | UP | 0.64 | open |  |
| 10-24 14:06 | +5 | SOL | UP | 0.64 | open |  |
| 10-24 14:06 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 10-24 14:06 | +15 | ETH | UP | 0.68 | open |  |
| 10-24 14:06 | +10 | ETH | UP | 0.68 | open |  |
| 10-24 14:06 | +5 | ETH | UP | 0.68 | open |  |
| 10-24 14:06 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-24 14:03 | +5 | NEAR | UP | 0.67 | open |  |
| 10-24 14:01 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.28 |
| 10-24 14:01 | +20 | HYPE | UP | 0.66 | open |  |
| 10-24 14:01 | +15 | HYPE | UP | 0.66 | open |  |
| 10-24 14:01 | +10 | HYPE | UP | 0.66 | open |  |
| 10-24 14:01 | +5 | HYPE | UP | 0.66 | 0.72 | 0.25 |
| 10-24 14:01 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-24 14:01 | +20 | XRP | UP | 0.70 | 0.92 | 1.94 |
| 10-24 14:01 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.89 |
| 10-24 14:01 | +20 | SOL | UP | 0.63 | open |  |
| 10-24 14:01 | +15 | SOL | UP | 0.63 | 0.79 | 1.31 |
| 10-24 14:01 | +10 | SOL | UP | 0.63 | 0.75 | 0.89 |
| 10-24 14:01 | +5 | SOL | UP | 0.63 | 0.72 | 0.58 |
| 10-24 14:01 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-24 14:01 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
