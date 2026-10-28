# Range-Scalp Bot

*Updated Wed Oct 28 14:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38204 | 33335 | 4869 (46) | 3 | $-10762.85 | -4.5% |
| **+10¢** | 28497 | 22867 | 5630 (68) | 1 | $-9593.32 | -5.3% |
| **+15¢** | 23844 | 17800 | 6044 (93) | 1 | $-8529.35 | -5.7% |
| **+20¢** | 21152 | 14822 | 6330 (118) | 1 | $-7492.53 | -5.6% |
| **+10¢ (15¢ stop)** | 46769 | 46702 | 67 (35) | 0 | $-17768.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 14:13 | +10 stop | HYPE | DOWN | 0.70 | 0.97 | 2.52 |
| 10-28 14:13 | +20 | HYPE | DOWN | 0.70 | 0.97 | 2.52 |
| 10-28 14:13 | +15 | HYPE | DOWN | 0.70 | 0.97 | 2.52 |
| 10-28 14:13 | +10 | HYPE | DOWN | 0.70 | 0.97 | 2.52 |
| 10-28 14:13 | +5 | HYPE | DOWN | 0.70 | 0.97 | 2.52 |
| 10-28 14:09 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-28 14:09 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-28 14:08 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-28 14:08 | +10 stop | ZEC | DOWN | 0.70 | 0.53 | -2.03 |
| 10-28 14:08 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-28 14:08 | +10 stop | NEAR | DOWN | 0.58 | 0.75 | 1.38 |
| 10-28 14:08 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-28 14:08 | +10 stop | DOGE | UP | 0.68 | 0.45 | -2.64 |
| 10-28 14:08 | +20 | DOGE | UP | 0.68 | open |  |
| 10-28 14:08 | +15 | DOGE | UP | 0.68 | open |  |
| 10-28 14:08 | +10 | DOGE | UP | 0.68 | open |  |
| 10-28 14:08 | +5 | DOGE | UP | 0.68 | open |  |
| 10-28 14:08 | +10 stop | BTC | UP | 0.65 | 0.50 | -1.84 |
| 10-28 14:07 | +10 stop | ZEC | UP | 0.46 | 0.65 | 1.56 |
| 10-28 14:06 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.12 |
| 10-28 14:06 | +10 stop | XRP | UP | 0.61 | 0.46 | -1.85 |
| 10-28 14:06 | +5 | SOL | UP | 0.69 | open |  |
| 10-28 14:05 | +10 stop | SOL | UP | 0.64 | 0.46 | -2.15 |
| 10-28 14:04 | +10 stop | NEAR | UP | 0.71 | 0.55 | -1.93 |
| 10-28 14:04 | +5 | NEAR | UP | 0.71 | open |  |
| 10-28 14:04 | +5 | SOL | UP | 0.66 | 0.73 | 0.40 |
| 10-28 14:04 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-28 14:04 | +5 | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-28 14:03 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-28 14:03 | +10 stop | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-28 14:03 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 10-28 14:03 | +10 stop | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-28 14:03 | +20 | DOGE | UP | 0.56 | 0.77 | 1.80 |
| 10-28 14:03 | +15 | DOGE | UP | 0.55 | 0.70 | 1.17 |
| 10-28 14:03 | +10 | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-28 14:03 | +5 | DOGE | UP | 0.57 | 0.63 | 0.28 |
| 10-28 14:03 | +10 stop | BNB | UP | 0.59 | 0.76 | 1.40 |
| 10-28 14:03 | +5 | NEAR | UP | 0.53 | 0.61 | 0.45 |
| 10-28 14:03 | +10 stop | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-28 14:03 | +20 | HYPE | UP | 0.63 | 0.83 | 1.73 |
