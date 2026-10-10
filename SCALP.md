# Range-Scalp Bot

*Updated Sat Oct 10 18:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10705 | 9227 | 1478 (22) | 4 | $-3663.05 | -5.4% |
| **+10¢** | 8107 | 6385 | 1722 (36) | 4 | $-3494.88 | -6.8% |
| **+15¢** | 6837 | 5015 | 1822 (52) | 6 | $-2955.27 | -6.9% |
| **+20¢** | 6079 | 4180 | 1899 (66) | 7 | $-2525.21 | -6.6% |
| **+10¢ (15¢ stop)** | 13154 | 13113 | 41 (25) | 3 | $-5225.84 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 18:08 | +5 | HYPE | UP | 0.61 | 0.66 | 0.17 |
| 10-10 18:08 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-10 18:08 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-10 18:07 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-10 18:07 | +10 | DOGE | UP | 0.69 | open |  |
| 10-10 18:07 | +5 | DOGE | UP | 0.69 | open |  |
| 10-10 18:07 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 10-10 18:07 | +10 | NEAR | UP | 0.66 | open |  |
| 10-10 18:07 | +5 | NEAR | UP | 0.66 | open |  |
| 10-10 18:07 | +5 | BTC | UP | 0.45 | 0.60 | 1.15 |
| 10-10 18:06 | +10 stop | SOL | UP | 0.53 | 0.36 | -2.05 |
| 10-10 18:06 | +10 stop | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-10 18:06 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-10 18:06 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-10 18:06 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-10 18:06 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 10-10 18:06 | +5 | SOL | UP | 0.55 | open |  |
| 10-10 18:06 | +5 | SOL | DOWN | 0.44 | 0.52 | 0.44 |
| 10-10 18:06 | +10 stop | BTC | DOWN | 0.57 | 0.39 | -2.15 |
| 10-10 18:06 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-10 18:06 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 10-10 18:05 | +10 stop | SOL | DOWN | 0.58 | 0.42 | -1.96 |
| 10-10 18:05 | +10 | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-10 18:05 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-10 18:05 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-10 18:05 | +10 | HYPE | UP | 0.70 | open |  |
| 10-10 18:05 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 10-10 18:05 | +10 stop | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 10-10 18:05 | +15 | NEAR | UP | 0.63 | open |  |
| 10-10 18:05 | +10 | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 10-10 18:05 | +5 | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 10-10 18:05 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-10 18:05 | +15 | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 10-10 18:05 | +10 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-10 18:05 | +5 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-10 18:04 | +20 | DOGE | UP | 0.68 | open |  |
| 10-10 18:04 | +15 | DOGE | UP | 0.68 | open |  |
| 10-10 18:04 | +5 | DOGE | UP | 0.68 | 0.73 | 0.20 |
| 10-10 18:03 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 10-10 18:03 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
