# Range-Scalp Bot

*Updated Fri Oct 16 14:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19345 | 16812 | 2533 (29) | 3 | $-5813.26 | -4.8% |
| **+10¢** | 14585 | 11656 | 2929 (41) | 3 | $-5237.54 | -5.7% |
| **+15¢** | 12207 | 9053 | 3154 (60) | 3 | $-4765.29 | -6.2% |
| **+20¢** | 10828 | 7522 | 3306 (79) | 3 | $-4245.35 | -6.2% |
| **+10¢ (15¢ stop)** | 23796 | 23746 | 50 (29) | 0 | $-9142.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 14:12 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-16 14:12 | +10 stop | SOL | UP | 0.65 | 0.89 | 2.17 |
| 10-16 14:12 | +10 stop | BNB | DOWN | 0.70 | 0.55 | -1.83 |
| 10-16 14:12 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-16 14:12 | +15 | BNB | DOWN | 0.70 | open |  |
| 10-16 14:12 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-16 14:12 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-16 14:12 | +10 stop | DOGE | UP | 0.55 | 0.79 | 2.10 |
| 10-16 14:12 | +10 | DOGE | UP | 0.55 | 0.79 | 2.10 |
| 10-16 14:12 | +10 stop | BTC | DOWN | 0.59 | 0.38 | -2.44 |
| 10-16 14:12 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-16 14:12 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-16 14:12 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-16 14:12 | +5 | BTC | DOWN | 0.69 | open |  |
| 10-16 14:09 | +10 stop | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-16 14:09 | +10 | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-16 14:08 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 10-16 14:07 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-16 14:07 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-16 14:07 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 14:06 | +5 | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-16 14:06 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-16 14:05 | +10 stop | DOGE | UP | 0.57 | 0.35 | -2.54 |
| 10-16 14:05 | +10 stop | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-16 14:05 | +20 | XRP | DOWN | 0.71 | 0.94 | 2.09 |
| 10-16 14:05 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-16 14:05 | +10 | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-16 14:05 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-16 14:04 | +10 stop | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 10-16 14:04 | +10 | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 10-16 14:04 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-16 14:04 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-16 14:04 | +10 stop | ETH | DOWN | 0.57 | 0.40 | -2.05 |
| 10-16 14:04 | +10 stop | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 10-16 14:04 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 10-16 14:04 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-16 14:04 | +10 stop | DOGE | DOWN | 0.58 | 0.43 | -1.86 |
| 10-16 14:04 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-16 14:04 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.96 |
| 10-16 14:04 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
