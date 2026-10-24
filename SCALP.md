# Range-Scalp Bot

*Updated Sat Oct 24 13:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32059 | 27946 | 4113 (40) | 1 | $-9200.21 | -4.6% |
| **+10¢** | 23991 | 19235 | 4756 (58) | 2 | $-8215.03 | -5.4% |
| **+15¢** | 20085 | 14969 | 5116 (81) | 2 | $-7368.92 | -5.8% |
| **+20¢** | 17792 | 12436 | 5356 (103) | 2 | $-6554.80 | -5.9% |
| **+10¢ (15¢ stop)** | 39388 | 39329 | 59 (32) | 0 | $-15081.16 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 13:18 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 13:18 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 13:18 | +5 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 13:17 | +10 stop | ZEC | UP | 0.52 | 0.23 | -3.21 |
| 10-24 13:17 | +20 | ZEC | UP | 0.52 | open |  |
| 10-24 13:17 | +15 | ZEC | UP | 0.52 | open |  |
| 10-24 13:17 | +10 | ZEC | UP | 0.52 | open |  |
| 10-24 13:17 | +5 | ZEC | UP | 0.52 | 0.58 | 0.24 |
| 10-24 13:17 | +10 stop | NEAR | UP | 0.58 | 0.26 | -3.52 |
| 10-24 13:16 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-24 13:16 | +20 | ETH | DOWN | 0.57 | 0.85 | 2.53 |
| 10-24 13:16 | +15 | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-24 13:16 | +10 | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-24 13:16 | +5 | ETH | DOWN | 0.58 | 0.69 | 0.78 |
| 10-24 13:16 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.16 |
| 10-24 13:16 | +20 | DOGE | DOWN | 0.65 | 0.87 | 2.00 |
| 10-24 13:16 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 13:16 | +10 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 13:16 | +5 | DOGE | DOWN | 0.64 | 0.72 | 0.48 |
| 10-24 13:16 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 10-24 13:16 | +10 stop | BNB | DOWN | 0.61 | 0.90 | 2.69 |
| 10-24 13:16 | +20 | BNB | DOWN | 0.61 | 0.90 | 2.69 |
| 10-24 13:16 | +15 | BNB | DOWN | 0.61 | 0.90 | 2.69 |
| 10-24 13:16 | +10 | BNB | DOWN | 0.61 | 0.90 | 2.69 |
| 10-24 13:16 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-24 13:16 | +10 stop | BTC | UP | 0.59 | 0.29 | -3.32 |
| 10-24 13:16 | +20 | BTC | UP | 0.59 | open |  |
| 10-24 13:16 | +15 | BTC | UP | 0.58 | open |  |
| 10-24 13:16 | +10 | BTC | UP | 0.58 | open |  |
| 10-24 13:16 | +5 | BTC | UP | 0.58 | open |  |
| 10-24 13:16 | +10 stop | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-24 13:16 | +20 | SOL | DOWN | 0.54 | 0.80 | 2.30 |
| 10-24 13:16 | +15 | SOL | DOWN | 0.54 | 0.73 | 1.58 |
| 10-24 13:16 | +10 | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-24 13:16 | +5 | SOL | DOWN | 0.54 | 0.61 | 0.35 |
| 10-24 13:15 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 10-24 13:15 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-24 13:15 | +15 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-24 13:15 | +10 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-24 13:15 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
