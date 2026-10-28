# Range-Scalp Bot

*Updated Wed Oct 28 23:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38611 | 33689 | 4922 (48) | 4 | $-10881.76 | -4.5% |
| **+10¢** | 28799 | 23114 | 5685 (70) | 4 | $-9658.44 | -5.3% |
| **+15¢** | 24091 | 17983 | 6108 (96) | 4 | $-8627.41 | -5.7% |
| **+20¢** | 21374 | 14977 | 6397 (124) | 4 | $-7537.88 | -5.6% |
| **+10¢ (15¢ stop)** | 47230 | 47163 | 67 (35) | 0 | $-17914.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 23:11 | +5 | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 10-28 23:10 | +5 | SOL | DOWN | 0.57 | 0.62 | 0.15 |
| 10-28 23:09 | +10 stop | XRP | DOWN | 0.61 | 0.75 | 1.09 |
| 10-28 23:09 | +20 | XRP | DOWN | 0.61 | 0.89 | 2.56 |
| 10-28 23:09 | +15 | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 10-28 23:09 | +10 | XRP | DOWN | 0.61 | 0.75 | 1.09 |
| 10-28 23:09 | +5 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-28 23:09 | +10 stop | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 23:09 | +10 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 23:09 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-28 23:08 | +10 stop | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-28 23:08 | +10 stop | ETH | UP | 0.55 | 0.71 | 1.27 |
| 10-28 23:08 | +10 stop | DOGE | UP | 0.60 | 0.80 | 1.73 |
| 10-28 23:08 | +5 | NEAR | UP | 0.65 | 0.74 | 0.60 |
| 10-28 23:07 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-28 23:06 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 10-28 23:05 | +10 stop | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-28 23:05 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-28 23:05 | +15 | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-28 23:05 | +10 | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-28 23:05 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-28 23:05 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 10-28 23:05 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-28 23:05 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-28 23:05 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-28 23:05 | +5 | BNB | DOWN | 0.60 | open |  |
| 10-28 23:05 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-28 23:05 | +20 | SOL | DOWN | 0.62 | 0.86 | 2.14 |
| 10-28 23:05 | +15 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 23:05 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 23:05 | +5 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 23:05 | +10 stop | NEAR | UP | 0.61 | 0.74 | 0.99 |
| 10-28 23:05 | +20 | NEAR | UP | 0.61 | 0.84 | 2.03 |
| 10-28 23:05 | +15 | NEAR | UP | 0.61 | 0.78 | 1.40 |
| 10-28 23:05 | +10 | NEAR | UP | 0.61 | 0.74 | 0.99 |
| 10-28 23:05 | +5 | NEAR | UP | 0.61 | 0.66 | 0.17 |
| 10-28 23:05 | +10 stop | DOGE | DOWN | 0.59 | 0.42 | -2.05 |
| 10-28 23:05 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-28 23:05 | +15 | DOGE | DOWN | 0.59 | open |  |
| 10-28 23:05 | +10 | DOGE | DOWN | 0.59 | open |  |
