# Range-Scalp Bot

*Updated Tue Oct 06 21:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5499 | 4766 | 733 (9) | 0 | $-1690.06 | -4.9% |
| **+10¢** | 4200 | 3339 | 861 (14) | 1 | $-1603.54 | -6.1% |
| **+15¢** | 3517 | 2604 | 913 (18) | 5 | $-1407.99 | -6.4% |
| **+20¢** | 3143 | 2195 | 948 (25) | 7 | $-1125.92 | -5.7% |
| **+10¢ (15¢ stop)** | 6698 | 6683 | 15 (9) | 1 | $-2395.88 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 21:32 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-06 21:31 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 10-06 21:31 | +20 | BNB | UP | 0.66 | open |  |
| 10-06 21:31 | +15 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-06 21:31 | +10 | BNB | UP | 0.66 | 0.77 | 0.81 |
| 10-06 21:31 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 10-06 21:31 | +10 stop | ETH | UP | 0.68 | open |  |
| 10-06 21:31 | +20 | ETH | UP | 0.68 | open |  |
| 10-06 21:31 | +15 | ETH | UP | 0.68 | open |  |
| 10-06 21:31 | +10 | ETH | UP | 0.68 | open |  |
| 10-06 21:31 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 10-06 21:31 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 10-06 21:31 | +20 | DOGE | UP | 0.69 | open |  |
| 10-06 21:31 | +15 | DOGE | UP | 0.69 | open |  |
| 10-06 21:31 | +10 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 10-06 21:31 | +5 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 10-06 21:31 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-06 21:31 | +20 | BTC | UP | 0.62 | open |  |
| 10-06 21:31 | +15 | BTC | UP | 0.62 | open |  |
| 10-06 21:31 | +10 | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-06 21:31 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 10-06 21:31 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-06 21:31 | +20 | HYPE | UP | 0.66 | open |  |
| 10-06 21:31 | +15 | HYPE | UP | 0.66 | open |  |
| 10-06 21:31 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-06 21:31 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 10-06 21:30 | +10 stop | XRP | UP | 0.60 | 0.75 | 1.19 |
| 10-06 21:30 | +20 | XRP | UP | 0.60 | open |  |
| 10-06 21:30 | +15 | XRP | UP | 0.60 | 0.75 | 1.19 |
| 10-06 21:30 | +10 | XRP | UP | 0.60 | 0.75 | 1.19 |
| 10-06 21:30 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-06 21:30 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.94 |
| 10-06 21:30 | +20 | NEAR | UP | 0.68 | open |  |
| 10-06 21:30 | +15 | NEAR | UP | 0.68 | open |  |
| 10-06 21:30 | +10 | NEAR | UP | 0.68 | 0.80 | 0.94 |
| 10-06 21:30 | +5 | NEAR | UP | 0.68 | 0.74 | 0.32 |
| 10-06 21:29 | +10 stop | BTC | UP | 0.62 | 0.80 | 1.51 |
| 10-06 21:28 | +10 stop | BNB | UP | 0.67 | 0.95 | 2.60 |
| 10-06 21:27 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.05 |
| 10-06 21:26 | +10 stop | BTC | DOWN | 0.69 | 0.36 | -3.62 |
