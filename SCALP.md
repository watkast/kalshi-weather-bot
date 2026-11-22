# Range-Scalp Bot

*Updated Sun Nov 22 02:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68118 | 59451 | 8667 (138) | 6 | $-18259.37 | -4.3% |
| **+10¢** | 50854 | 40732 | 10122 (181) | 7 | $-16911.80 | -5.3% |
| **+15¢** | 42631 | 31718 | 10913 (230) | 6 | $-15173.27 | -5.7% |
| **+20¢** | 37949 | 26479 | 11470 (288) | 7 | $-13505.82 | -5.7% |
| **+10¢ (15¢ stop)** | 82929 | 82751 | 178 (110) | 4 | $-30432.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 02:09 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-22 02:09 | +10 stop | ETH | UP | 0.60 | open |  |
| 11-22 02:09 | +5 | ETH | UP | 0.60 | open |  |
| 11-22 02:09 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-22 02:09 | +10 stop | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-22 02:08 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 11-22 02:08 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-22 02:08 | +10 stop | ETH | DOWN | 0.41 | 0.55 | 1.05 |
| 11-22 02:08 | +5 | ETH | DOWN | 0.41 | 0.55 | 1.05 |
| 11-22 02:07 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.71 |
| 11-22 02:07 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 02:06 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-22 02:06 | +10 stop | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-22 02:06 | +15 | NEAR | UP | 0.63 | 0.88 | 2.25 |
| 11-22 02:06 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-22 02:06 | +5 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-22 02:06 | +5 | BTC | UP | 0.63 | 0.72 | 0.58 |
| 11-22 02:06 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
| 11-22 02:06 | +10 | ETH | UP | 0.66 | open |  |
| 11-22 02:06 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 11-22 02:05 | +5 | BNB | UP | 0.61 | open |  |
| 11-22 02:05 | +10 stop | SOL | DOWN | 0.57 | 0.75 | 1.48 |
| 11-22 02:05 | +5 | BNB | UP | 0.52 | 0.58 | 0.24 |
| 11-22 02:04 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 11-22 02:04 | +10 stop | BTC | UP | 0.68 | 0.30 | -4.11 |
| 11-22 02:04 | +10 stop | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-22 02:04 | +10 stop | XRP | UP | 0.59 | 0.42 | -2.01 |
| 11-22 02:04 | +10 | XRP | UP | 0.59 | open |  |
| 11-22 02:04 | +5 | XRP | UP | 0.58 | open |  |
| 11-22 02:04 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-22 02:04 | +20 | ETH | UP | 0.65 | open |  |
| 11-22 02:04 | +15 | ETH | UP | 0.65 | open |  |
| 11-22 02:04 | +10 | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-22 02:04 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-22 02:03 | +10 stop | BNB | DOWN | 0.48 | 0.67 | 1.56 |
| 11-22 02:03 | +5 | BNB | DOWN | 0.48 | 0.56 | 0.44 |
| 11-22 02:03 | +10 stop | HYPE | DOWN | 0.53 | 0.68 | 1.19 |
| 11-22 02:03 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 11-22 02:03 | +10 stop | SOL | DOWN | 0.69 | 0.53 | -1.93 |
| 11-22 02:03 | +10 | SOL | DOWN | 0.67 | open |  |
