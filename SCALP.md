# Range-Scalp Bot

*Updated Fri Nov 27 23:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74002 | 64591 | 9411 (171) | 1 | $-19636.47 | -4.2% |
| **+10¢** | 55140 | 44149 | 10991 (216) | 1 | $-18253.06 | -5.3% |
| **+15¢** | 46171 | 34334 | 11837 (274) | 1 | $-16308.78 | -5.6% |
| **+20¢** | 41090 | 28622 | 12468 (341) | 1 | $-14722.03 | -5.7% |
| **+10¢ (15¢ stop)** | 90097 | 89878 | 219 (135) | 1 | $-33316.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 23:09 | +10 stop | DOGE | UP | 0.66 | open |  |
| 11-27 23:09 | +15 | DOGE | UP | 0.66 | open |  |
| 11-27 23:09 | +10 | DOGE | UP | 0.66 | open |  |
| 11-27 23:09 | +5 | DOGE | UP | 0.66 | open |  |
| 11-27 23:05 | +10 stop | XRP | UP | 0.65 | 0.81 | 1.33 |
| 11-27 23:05 | +20 | XRP | UP | 0.65 | 0.87 | 1.96 |
| 11-27 23:05 | +15 | XRP | UP | 0.65 | 0.81 | 1.33 |
| 11-27 23:05 | +10 | XRP | UP | 0.65 | 0.81 | 1.33 |
| 11-27 23:05 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 11-27 23:02 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-27 23:02 | +20 | DOGE | UP | 0.67 | open |  |
| 11-27 23:02 | +15 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-27 23:02 | +10 | DOGE | UP | 0.67 | 0.78 | 0.82 |
| 11-27 23:02 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 11-27 19:50 | +10 stop | HYPE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-27 19:49 | +10 stop | ZEC | DOWN | 0.47 | 0.65 | 1.46 |
| 11-27 19:48 | +10 stop | HYPE | UP | 0.59 | 0.40 | -2.24 |
| 11-27 19:48 | +5 | HYPE | UP | 0.59 | no | -6.07 |
| 11-27 19:47 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.97 |
| 11-27 19:47 | +5 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-27 19:46 | +5 | HYPE | DOWN | 0.55 | 0.60 | 0.15 |
| 11-27 19:46 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 11-27 19:46 | +20 | BNB | DOWN | 0.69 | 0.92 | 2.09 |
| 11-27 19:46 | +15 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-27 19:46 | +10 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-27 19:46 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-27 19:46 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-27 19:46 | +20 | ETH | DOWN | 0.68 | 0.95 | 2.47 |
| 11-27 19:46 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-27 19:46 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-27 19:46 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 11-27 19:46 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-27 19:46 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.81 |
| 11-27 19:46 | +15 | NEAR | DOWN | 0.71 | 0.88 | 1.47 |
| 11-27 19:46 | +10 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-27 19:46 | +5 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-27 19:46 | +10 stop | HYPE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-27 19:46 | +20 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-27 19:46 | +15 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-27 19:46 | +10 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
