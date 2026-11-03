# Range-Scalp Bot

*Updated Tue Nov 03 23:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46454 | 40449 | 6005 (72) | 2 | $-13365.54 | -4.6% |
| **+10¢** | 34684 | 27725 | 6959 (96) | 4 | $-12217.66 | -5.6% |
| **+15¢** | 29038 | 21553 | 7485 (124) | 4 | $-11169.02 | -6.1% |
| **+20¢** | 25799 | 17955 | 7844 (164) | 5 | $-9873.79 | -6.1% |
| **+10¢ (15¢ stop)** | 56661 | 56568 | 93 (56) | 1 | $-21233.04 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 23:07 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-03 23:06 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-03 23:06 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 11-03 23:05 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-03 23:05 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 11-03 23:05 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-03 23:05 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-03 23:02 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-03 23:02 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-03 23:02 | +10 stop | BTC | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 23:02 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-03 23:02 | +10 stop | BNB | DOWN | 0.68 | 0.82 | 1.13 |
| 11-03 23:02 | +20 | BNB | DOWN | 0.68 | 0.90 | 1.97 |
| 11-03 23:02 | +15 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 11-03 23:02 | +10 | BNB | DOWN | 0.68 | 0.82 | 1.13 |
| 11-03 23:02 | +5 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-03 23:01 | +10 stop | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-03 23:01 | +20 | HYPE | DOWN | 0.60 | 0.81 | 1.82 |
| 11-03 23:01 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 23:01 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-03 23:01 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-03 23:01 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-03 23:01 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 11-03 23:01 | +20 | XRP | DOWN | 0.70 | 0.90 | 1.78 |
| 11-03 23:01 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-03 23:01 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 11-03 23:01 | +5 | XRP | DOWN | 0.70 | 0.78 | 0.52 |
| 11-03 23:01 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-03 23:01 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.85 |
| 11-03 23:01 | +15 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 11-03 23:01 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-03 23:01 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-03 23:01 | +10 stop | DOGE | UP | 0.53 | 0.31 | -2.53 |
| 11-03 23:01 | +20 | DOGE | UP | 0.53 | open |  |
| 11-03 23:01 | +15 | DOGE | UP | 0.53 | open |  |
| 11-03 23:01 | +10 | DOGE | UP | 0.53 | open |  |
| 11-03 23:01 | +5 | DOGE | UP | 0.53 | 0.61 | 0.45 |
| 11-03 23:01 | +10 stop | NEAR | UP | 0.36 | 0.54 | 1.45 |
| 11-03 23:01 | +20 | NEAR | UP | 0.36 | open |  |
| 11-03 23:01 | +15 | NEAR | UP | 0.36 | 0.54 | 1.45 |
