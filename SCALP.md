# Range-Scalp Bot

*Updated Fri Oct 09 07:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8691 | 7511 | 1180 (13) | 2 | $-2903.44 | -5.3% |
| **+10¢** | 6579 | 5190 | 1389 (25) | 4 | $-2827.62 | -6.8% |
| **+15¢** | 5554 | 4093 | 1461 (37) | 4 | $-2295.09 | -6.6% |
| **+20¢** | 4944 | 3429 | 1515 (45) | 4 | $-1892.05 | -6.1% |
| **+10¢ (15¢ stop)** | 10611 | 10581 | 30 (19) | 1 | $-3973.80 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 07:02 | +10 stop | NEAR | DOWN | 0.53 | open |  |
| 10-09 07:02 | +20 | NEAR | DOWN | 0.53 | open |  |
| 10-09 07:02 | +15 | NEAR | DOWN | 0.53 | open |  |
| 10-09 07:02 | +10 | NEAR | DOWN | 0.53 | open |  |
| 10-09 07:02 | +5 | NEAR | DOWN | 0.53 | 0.61 | 0.45 |
| 10-09 07:01 | +10 stop | ZEC | DOWN | 0.66 | 0.44 | -2.51 |
| 10-09 07:01 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-09 07:01 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-09 07:01 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-09 07:01 | +5 | ZEC | DOWN | 0.66 | open |  |
| 10-09 07:01 | +10 stop | XRP | DOWN | 0.67 | 0.51 | -1.94 |
| 10-09 07:01 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-09 07:01 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-09 07:01 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-09 07:01 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-09 07:01 | +10 stop | ETH | DOWN | 0.63 | 0.44 | -2.25 |
| 10-09 07:01 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-09 07:01 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-09 07:01 | +10 | ETH | DOWN | 0.63 | open |  |
| 10-09 07:01 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-09 06:58 | +10 stop | BNB | DOWN | 0.57 | 0.10 | -4.92 |
| 10-09 06:58 | +5 | BNB | DOWN | 0.57 | 0.63 | 0.28 |
| 10-09 06:57 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-09 06:57 | +10 stop | SOL | DOWN | 0.67 | 0.96 | 2.73 |
| 10-09 06:57 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 10-09 06:56 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-09 06:55 | +10 stop | NEAR | DOWN | 0.58 | 0.73 | 1.16 |
| 10-09 06:55 | +10 stop | HYPE | DOWN | 0.47 | 0.60 | 0.95 |
| 10-09 06:55 | +10 stop | BTC | DOWN | 0.69 | 0.46 | -2.63 |
| 10-09 06:55 | +10 stop | BNB | DOWN | 0.62 | 0.26 | -3.91 |
| 10-09 06:55 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-09 06:55 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 10-09 06:54 | +10 stop | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 10-09 06:53 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-09 06:53 | +10 stop | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-09 06:52 | +10 stop | HYPE | UP | 0.36 | 0.55 | 1.51 |
| 10-09 06:51 | +5 | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 10-09 06:50 | +10 stop | HYPE | DOWN | 0.68 | 0.44 | -2.74 |
| 10-09 06:50 | +5 | ETH | DOWN | 0.53 | 0.58 | 0.14 |
| 10-09 06:49 | +10 stop | ETH | DOWN | 0.58 | 0.78 | 1.69 |
