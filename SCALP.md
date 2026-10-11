# Range-Scalp Bot

*Updated Sun Oct 11 05:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11397 | 9828 | 1569 (24) | 3 | $-3857.03 | -5.4% |
| **+10¢** | 8633 | 6808 | 1825 (37) | 4 | $-3676.39 | -6.8% |
| **+15¢** | 7278 | 5348 | 1930 (53) | 4 | $-3099.07 | -6.8% |
| **+20¢** | 6484 | 4476 | 2008 (67) | 5 | $-2589.74 | -6.4% |
| **+10¢ (15¢ stop)** | 14038 | 13997 | 41 (25) | 2 | $-5637.53 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 05:11 | +5 | BNB | DOWN | 0.58 | open |  |
| 10-11 05:11 | +10 stop | ETH | UP | 0.71 | open |  |
| 10-11 05:11 | +20 | ETH | UP | 0.71 | open |  |
| 10-11 05:11 | +15 | ETH | UP | 0.71 | open |  |
| 10-11 05:11 | +10 | ETH | UP | 0.71 | open |  |
| 10-11 05:11 | +5 | ETH | UP | 0.71 | open |  |
| 10-11 05:10 | +10 stop | BNB | DOWN | 0.50 | open |  |
| 10-11 05:10 | +10 | BNB | DOWN | 0.50 | open |  |
| 10-11 05:10 | +5 | BNB | DOWN | 0.50 | 0.56 | 0.24 |
| 10-11 05:09 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.81 |
| 10-11 05:09 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-11 05:09 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-11 05:09 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.81 |
| 10-11 05:09 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.50 |
| 10-11 05:09 | +10 stop | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-11 05:09 | +20 | BTC | UP | 0.71 | 0.93 | 2.02 |
| 10-11 05:09 | +15 | BTC | UP | 0.71 | 0.88 | 1.47 |
| 10-11 05:09 | +10 | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-11 05:09 | +5 | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-11 05:08 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.75 |
| 10-11 05:08 | +10 stop | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-11 05:08 | +5 | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-11 05:07 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 05:07 | +10 stop | HYPE | UP | 0.64 | 0.43 | -2.45 |
| 10-11 05:07 | +10 stop | SOL | UP | 0.57 | 0.34 | -2.64 |
| 10-11 05:06 | +10 stop | SOL | UP | 0.53 | 0.67 | 1.06 |
| 10-11 05:06 | +10 stop | DOGE | UP | 0.57 | 0.71 | 1.07 |
| 10-11 05:06 | +10 stop | XRP | UP | 0.66 | 0.48 | -2.14 |
| 10-11 05:06 | +20 | XRP | UP | 0.66 | open |  |
| 10-11 05:06 | +15 | XRP | UP | 0.66 | open |  |
| 10-11 05:06 | +10 | XRP | UP | 0.65 | open |  |
| 10-11 05:06 | +5 | XRP | UP | 0.65 | open |  |
| 10-11 05:06 | +10 stop | ZEC | UP | 0.51 | 0.34 | -2.04 |
| 10-11 05:06 | +15 | ZEC | UP | 0.51 | open |  |
| 10-11 05:06 | +10 | ZEC | UP | 0.51 | open |  |
| 10-11 05:06 | +5 | ZEC | UP | 0.51 | 0.58 | 0.34 |
| 10-11 05:03 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 10-11 05:03 | +20 | NEAR | DOWN | 0.68 | 0.90 | 2.00 |
| 10-11 05:03 | +15 | NEAR | DOWN | 0.68 | 0.85 | 1.45 |
| 10-11 05:03 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
