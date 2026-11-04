# Range-Scalp Bot

*Updated Wed Nov 04 10:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47100 | 41014 | 6086 (72) | 7 | $-13566.58 | -4.6% |
| **+10¢** | 35191 | 28132 | 7059 (97) | 7 | $-12387.00 | -5.6% |
| **+15¢** | 29470 | 21869 | 7601 (125) | 7 | $-11364.83 | -6.1% |
| **+20¢** | 26180 | 18218 | 7962 (165) | 7 | $-10034.72 | -6.1% |
| **+10¢ (15¢ stop)** | 57406 | 57313 | 93 (56) | 3 | $-21384.47 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 10:35 | +10 stop | ETH | UP | 0.58 | open |  |
| 11-04 10:35 | +10 | ETH | UP | 0.58 | open |  |
| 11-04 10:35 | +5 | ETH | UP | 0.58 | open |  |
| 11-04 10:34 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-04 10:34 | +10 stop | ETH | UP | 0.62 | 0.75 | 0.99 |
| 11-04 10:34 | +15 | ETH | UP | 0.62 | open |  |
| 11-04 10:34 | +10 | ETH | UP | 0.62 | 0.75 | 0.99 |
| 11-04 10:34 | +5 | ETH | UP | 0.62 | 0.75 | 0.99 |
| 11-04 10:33 | +10 stop | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-04 10:33 | +10 stop | HYPE | UP | 0.63 | open |  |
| 11-04 10:33 | +10 stop | ETH | DOWN | 0.46 | 0.62 | 1.25 |
| 11-04 10:33 | +20 | ETH | DOWN | 0.46 | open |  |
| 11-04 10:33 | +15 | ETH | DOWN | 0.47 | 0.62 | 1.15 |
| 11-04 10:33 | +10 | ETH | DOWN | 0.47 | 0.62 | 1.15 |
| 11-04 10:33 | +5 | ETH | DOWN | 0.47 | 0.62 | 1.15 |
| 11-04 10:33 | +10 stop | ZEC | UP | 0.60 | 0.77 | 1.40 |
| 11-04 10:32 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-04 10:32 | +20 | NEAR | UP | 0.58 | 0.81 | 2.01 |
| 11-04 10:32 | +15 | NEAR | UP | 0.58 | 0.77 | 1.59 |
| 11-04 10:32 | +10 | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-04 10:32 | +5 | NEAR | UP | 0.58 | 0.67 | 0.56 |
| 11-04 10:32 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-04 10:31 | +10 stop | SOL | DOWN | 0.62 | 0.47 | -1.85 |
| 11-04 10:31 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-04 10:31 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-04 10:31 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-04 10:31 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-04 10:31 | +10 stop | ZEC | DOWN | 0.62 | 0.28 | -3.72 |
| 11-04 10:31 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-04 10:31 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-04 10:31 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-04 10:31 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-04 10:31 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 11-04 10:31 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-04 10:31 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-04 10:31 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-04 10:31 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-04 10:31 | +10 stop | XRP | UP | 0.66 | 0.81 | 1.23 |
| 11-04 10:31 | +20 | XRP | UP | 0.66 | 0.88 | 1.96 |
| 11-04 10:31 | +15 | XRP | UP | 0.66 | 0.81 | 1.23 |
