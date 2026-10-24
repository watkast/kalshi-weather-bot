# Range-Scalp Bot

*Updated Sat Oct 24 13:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32042 | 27931 | 4111 (40) | 4 | $-9197.63 | -4.6% |
| **+10¢** | 23975 | 19224 | 4751 (58) | 6 | $-8196.07 | -5.4% |
| **+15¢** | 20071 | 14962 | 5109 (81) | 6 | $-7334.62 | -5.8% |
| **+20¢** | 17777 | 12428 | 5349 (103) | 7 | $-6525.04 | -5.8% |
| **+10¢ (15¢ stop)** | 39367 | 39308 | 59 (32) | 3 | $-15062.16 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 13:09 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-24 13:09 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-24 13:09 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 10-24 13:09 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 10-24 13:09 | +5 | ETH | DOWN | 0.58 | open |  |
| 10-24 13:08 | +10 stop | BNB | UP | 0.61 | 0.46 | -1.85 |
| 10-24 13:08 | +20 | BNB | UP | 0.61 | open |  |
| 10-24 13:08 | +15 | BNB | UP | 0.61 | open |  |
| 10-24 13:08 | +10 | BNB | UP | 0.61 | open |  |
| 10-24 13:08 | +5 | BNB | UP | 0.61 | open |  |
| 10-24 13:08 | +10 stop | ZEC | UP | 0.61 | 0.41 | -2.30 |
| 10-24 13:08 | +20 | ZEC | UP | 0.61 | open |  |
| 10-24 13:08 | +15 | ZEC | UP | 0.61 | open |  |
| 10-24 13:08 | +10 | ZEC | UP | 0.61 | open |  |
| 10-24 13:08 | +5 | ZEC | UP | 0.61 | open |  |
| 10-24 13:07 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-24 13:07 | +10 | ETH | UP | 0.62 | open |  |
| 10-24 13:07 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 10-24 13:07 | +10 stop | SOL | UP | 0.61 | 0.39 | -2.54 |
| 10-24 13:07 | +15 | SOL | UP | 0.61 | open |  |
| 10-24 13:07 | +10 | SOL | UP | 0.61 | open |  |
| 10-24 13:07 | +5 | SOL | UP | 0.61 | 0.69 | 0.51 |
| 10-24 13:04 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-24 13:04 | +20 | ETH | UP | 0.68 | open |  |
| 10-24 13:04 | +15 | ETH | UP | 0.68 | open |  |
| 10-24 13:04 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-24 13:04 | +5 | ETH | UP | 0.68 | 0.77 | 0.61 |
| 10-24 13:04 | +5 | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-24 13:04 | +10 stop | NEAR | UP | 0.63 | 0.40 | -2.64 |
| 10-24 13:04 | +15 | NEAR | UP | 0.63 | open |  |
| 10-24 13:04 | +10 | NEAR | UP | 0.63 | open |  |
| 10-24 13:04 | +5 | NEAR | UP | 0.63 | open |  |
| 10-24 13:01 | +10 stop | BTC | UP | 0.68 | 0.53 | -1.84 |
| 10-24 13:01 | +20 | BTC | UP | 0.68 | open |  |
| 10-24 13:01 | +15 | BTC | UP | 0.68 | open |  |
| 10-24 13:01 | +10 | BTC | UP | 0.68 | open |  |
| 10-24 13:01 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-24 13:01 | +10 stop | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 10-24 13:01 | +20 | NEAR | UP | 0.60 | open |  |
| 10-24 13:01 | +15 | NEAR | UP | 0.60 | 0.76 | 1.30 |
