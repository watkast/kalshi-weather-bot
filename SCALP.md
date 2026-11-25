# Range-Scalp Bot

*Updated Wed Nov 25 03:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71367 | 62294 | 9073 (156) | 2 | $-19003.85 | -4.2% |
| **+10¢** | 53230 | 42631 | 10599 (202) | 2 | $-17620.70 | -5.3% |
| **+15¢** | 44578 | 33168 | 11410 (259) | 3 | $-15661.93 | -5.6% |
| **+20¢** | 39688 | 27672 | 12016 (325) | 3 | $-14070.41 | -5.7% |
| **+10¢ (15¢ stop)** | 86883 | 86680 | 203 (123) | 1 | $-31933.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 03:40 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 11-25 03:40 | +10 | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 11-25 03:40 | +10 stop | BNB | DOWN | 0.54 | 0.36 | -2.10 |
| 11-25 03:40 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-25 03:40 | +20 | BTC | UP | 0.69 | open |  |
| 11-25 03:40 | +15 | BTC | UP | 0.69 | open |  |
| 11-25 03:40 | +10 | BTC | UP | 0.69 | open |  |
| 11-25 03:40 | +5 | BTC | UP | 0.71 | open |  |
| 11-25 03:40 | +5 | BNB | DOWN | 0.36 | 0.54 | 1.45 |
| 11-25 03:39 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 11-25 03:39 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.67 |
| 11-25 03:39 | +10 | DOGE | UP | 0.52 | 0.63 | 0.75 |
| 11-25 03:39 | +5 | BNB | UP | 0.58 | 0.67 | 0.56 |
| 11-25 03:37 | +10 stop | BNB | UP | 0.64 | 0.34 | -3.33 |
| 11-25 03:37 | +5 | BNB | UP | 0.65 | 0.72 | 0.35 |
| 11-25 03:37 | +10 stop | BNB | DOWN | 0.52 | 0.36 | -1.95 |
| 11-25 03:36 | +10 stop | DOGE | DOWN | 0.68 | 0.39 | -3.23 |
| 11-25 03:36 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-25 03:36 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 11-25 03:36 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-25 03:36 | +10 stop | ZEC | UP | 0.53 | 0.70 | 1.37 |
| 11-25 03:36 | +5 | NEAR | UP | 0.54 | 0.60 | 0.25 |
| 11-25 03:35 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-25 03:35 | +10 stop | DOGE | UP | 0.61 | 0.44 | -2.05 |
| 11-25 03:34 | +10 stop | DOGE | DOWN | 0.55 | 0.39 | -1.95 |
| 11-25 03:34 | +5 | BNB | UP | 0.53 | 0.61 | 0.45 |
| 11-25 03:34 | +10 stop | ZEC | UP | 0.53 | 0.38 | -1.85 |
| 11-25 03:34 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-25 03:34 | +15 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-25 03:34 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-25 03:34 | +5 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-25 03:33 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 11-25 03:33 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-25 03:33 | +10 stop | NEAR | UP | 0.57 | 0.78 | 1.79 |
| 11-25 03:33 | +20 | NEAR | UP | 0.57 | 0.78 | 1.79 |
| 11-25 03:33 | +15 | NEAR | UP | 0.57 | 0.78 | 1.79 |
| 11-25 03:33 | +10 | NEAR | UP | 0.57 | 0.78 | 1.79 |
| 11-25 03:33 | +5 | NEAR | UP | 0.57 | 0.65 | 0.46 |
| 11-25 03:33 | +10 stop | HYPE | UP | 0.67 | 0.84 | 1.44 |
| 11-25 03:33 | +15 | HYPE | UP | 0.67 | 0.84 | 1.44 |
