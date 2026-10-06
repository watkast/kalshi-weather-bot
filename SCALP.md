# Range-Scalp Bot

*Updated Tue Oct 06 20:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5413 | 4689 | 724 (7) | 2 | $-1689.85 | -4.9% |
| **+10¢** | 4136 | 3287 | 849 (12) | 4 | $-1598.88 | -6.1% |
| **+15¢** | 3466 | 2569 | 897 (15) | 5 | $-1389.40 | -6.4% |
| **+20¢** | 3102 | 2170 | 932 (22) | 5 | $-1105.32 | -5.7% |
| **+10¢ (15¢ stop)** | 6607 | 6592 | 15 (9) | 4 | $-2381.42 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 20:18 | +5 | NEAR | UP | 0.70 | open |  |
| 10-06 20:17 | +10 stop | ZEC | UP | 0.66 | open |  |
| 10-06 20:17 | +20 | ZEC | UP | 0.66 | open |  |
| 10-06 20:17 | +15 | ZEC | UP | 0.66 | open |  |
| 10-06 20:17 | +10 | ZEC | UP | 0.66 | open |  |
| 10-06 20:17 | +5 | ZEC | UP | 0.66 | 0.71 | 0.19 |
| 10-06 20:16 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-06 20:16 | +20 | NEAR | UP | 0.65 | open |  |
| 10-06 20:16 | +15 | NEAR | UP | 0.65 | open |  |
| 10-06 20:16 | +10 | NEAR | UP | 0.65 | open |  |
| 10-06 20:16 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 10-06 20:16 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-06 20:16 | +20 | BTC | UP | 0.70 | open |  |
| 10-06 20:16 | +15 | BTC | UP | 0.70 | open |  |
| 10-06 20:16 | +10 | BTC | UP | 0.70 | open |  |
| 10-06 20:16 | +5 | BTC | UP | 0.70 | open |  |
| 10-06 20:16 | +10 stop | XRP | UP | 0.69 | 0.81 | 0.96 |
| 10-06 20:16 | +20 | XRP | UP | 0.69 | open |  |
| 10-06 20:16 | +15 | XRP | UP | 0.69 | open |  |
| 10-06 20:16 | +10 | XRP | UP | 0.69 | 0.81 | 0.96 |
| 10-06 20:16 | +5 | XRP | UP | 0.69 | 0.77 | 0.54 |
| 10-06 20:16 | +10 stop | BNB | UP | 0.67 | open |  |
| 10-06 20:16 | +20 | BNB | UP | 0.67 | open |  |
| 10-06 20:16 | +15 | BNB | UP | 0.67 | open |  |
| 10-06 20:16 | +10 | BNB | UP | 0.67 | open |  |
| 10-06 20:16 | +5 | BNB | UP | 0.67 | 0.75 | 0.50 |
| 10-06 20:14 | +10 stop | ETH | DOWN | 0.40 | 0.59 | 1.56 |
| 10-06 20:14 | +20 | ETH | DOWN | 0.40 | yes | -4.13 |
| 10-06 20:14 | +15 | ETH | DOWN | 0.40 | 0.59 | 1.60 |
| 10-06 20:14 | +10 | ETH | DOWN | 0.40 | 0.59 | 1.56 |
| 10-06 20:14 | +5 | ETH | DOWN | 0.40 | 0.59 | 1.56 |
| 10-06 20:11 | +5 | NEAR | UP | 0.57 | 0.94 | 3.46 |
| 10-06 20:10 | +10 stop | ETH | UP | 0.35 | 0.57 | 1.86 |
| 10-06 20:10 | +15 | BTC | DOWN | 0.71 | 0.90 | 1.69 |
| 10-06 20:10 | +10 stop | DOGE | UP | 0.66 | 0.47 | -2.24 |
| 10-06 20:10 | +10 | DOGE | UP | 0.66 | no | -6.76 |
| 10-06 20:09 | +10 stop | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-06 20:09 | +10 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-06 20:09 | +5 | XRP | DOWN | 0.66 | 0.75 | 0.60 |
| 10-06 20:09 | +5 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
