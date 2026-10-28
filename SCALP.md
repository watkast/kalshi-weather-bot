# Range-Scalp Bot

*Updated Wed Oct 28 17:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38283 | 33406 | 4877 (46) | 3 | $-10776.70 | -4.5% |
| **+10¢** | 28555 | 22920 | 5635 (68) | 3 | $-9568.59 | -5.3% |
| **+15¢** | 23894 | 17845 | 6049 (93) | 3 | $-8494.26 | -5.7% |
| **+20¢** | 21198 | 14863 | 6335 (118) | 4 | $-7441.51 | -5.6% |
| **+10¢ (15¢ stop)** | 46841 | 46774 | 67 (35) | 1 | $-17761.07 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 17:52 | +10 stop | HYPE | UP | 0.66 | open |  |
| 10-28 17:49 | +20 | NEAR | UP | 0.71 | open |  |
| 10-28 17:49 | +5 | NEAR | UP | 0.71 | 0.78 | 0.42 |
| 10-28 17:48 | +10 stop | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 10-28 17:48 | +15 | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 10-28 17:48 | +10 | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 10-28 17:48 | +10 stop | DOGE | UP | 0.69 | 0.81 | 0.94 |
| 10-28 17:48 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-28 17:48 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
| 10-28 17:47 | +10 stop | HYPE | DOWN | 0.55 | 0.32 | -2.64 |
| 10-28 17:47 | +5 | NEAR | DOWN | 0.44 | 0.58 | 1.04 |
| 10-28 17:47 | +10 stop | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-28 17:47 | +20 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 10-28 17:47 | +15 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-28 17:47 | +10 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-28 17:47 | +5 | ZEC | UP | 0.63 | 0.70 | 0.38 |
| 10-28 17:46 | +10 stop | BTC | DOWN | 0.54 | 0.35 | -2.24 |
| 10-28 17:46 | +10 stop | ETH | DOWN | 0.65 | 0.50 | -1.84 |
| 10-28 17:46 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-28 17:46 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-28 17:46 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-28 17:46 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-28 17:46 | +10 stop | DOGE | DOWN | 0.67 | 0.40 | -3.03 |
| 10-28 17:46 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-28 17:46 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-28 17:46 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-28 17:46 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-28 17:46 | +10 stop | XRP | UP | 0.58 | 0.73 | 1.18 |
| 10-28 17:46 | +20 | XRP | UP | 0.58 | 0.79 | 1.80 |
| 10-28 17:46 | +15 | XRP | UP | 0.58 | 0.73 | 1.18 |
| 10-28 17:46 | +10 | XRP | UP | 0.58 | 0.73 | 1.18 |
| 10-28 17:46 | +5 | XRP | UP | 0.58 | 0.73 | 1.18 |
| 10-28 17:46 | +10 stop | NEAR | UP | 0.47 | 0.63 | 1.25 |
| 10-28 17:46 | +20 | NEAR | UP | 0.47 | 0.71 | 2.07 |
| 10-28 17:46 | +15 | NEAR | UP | 0.47 | 0.63 | 1.25 |
| 10-28 17:46 | +10 | NEAR | UP | 0.47 | 0.63 | 1.25 |
| 10-28 17:46 | +5 | NEAR | UP | 0.47 | 0.56 | 0.54 |
| 10-28 17:46 | +10 stop | BNB | UP | 0.58 | 0.76 | 1.49 |
| 10-28 17:46 | +20 | BNB | UP | 0.59 | 0.80 | 1.77 |
| 10-28 17:46 | +15 | BNB | UP | 0.60 | 0.76 | 1.30 |
