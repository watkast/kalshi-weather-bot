# Range-Scalp Bot

*Updated Mon Nov 23 21:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70119 | 61193 | 8926 (147) | 5 | $-18832.44 | -4.3% |
| **+10¢** | 52315 | 41890 | 10425 (190) | 5 | $-17474.78 | -5.3% |
| **+15¢** | 43837 | 32609 | 11228 (246) | 6 | $-15565.19 | -5.7% |
| **+20¢** | 39029 | 27213 | 11816 (311) | 6 | $-13928.54 | -5.7% |
| **+10¢ (15¢ stop)** | 85410 | 85214 | 196 (118) | 0 | $-31408.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 21:27 | +10 stop | ZEC | UP | 0.71 | 0.52 | -2.23 |
| 11-23 21:25 | +10 stop | ZEC | DOWN | 0.52 | 0.37 | -1.85 |
| 11-23 21:24 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-23 21:24 | +10 stop | ZEC | DOWN | 0.44 | 0.58 | 1.04 |
| 11-23 21:24 | +10 stop | BNB | DOWN | 0.67 | 0.36 | -3.43 |
| 11-23 21:24 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-23 21:24 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-23 21:24 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 11-23 21:22 | +10 stop | ZEC | DOWN | 0.69 | 0.48 | -2.43 |
| 11-23 21:22 | +10 stop | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-23 21:22 | +5 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-23 21:22 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-23 21:22 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.38 |
| 11-23 21:22 | +10 stop | DOGE | DOWN | 0.69 | 0.50 | -2.23 |
| 11-23 21:22 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-23 21:22 | +10 | DOGE | DOWN | 0.69 | open |  |
| 11-23 21:22 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.62 |
| 11-23 21:21 | +10 stop | HYPE | DOWN | 0.69 | 0.51 | -2.13 |
| 11-23 21:21 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-23 21:21 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-23 21:21 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-23 21:21 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-23 21:21 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-23 21:21 | +10 stop | BTC | DOWN | 0.71 | 0.54 | -2.03 |
| 11-23 21:21 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-23 21:21 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-23 21:21 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-23 21:20 | +5 | XRP | DOWN | 0.51 | open |  |
| 11-23 21:19 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-23 21:18 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-23 21:18 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-23 21:18 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-23 21:18 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 21:18 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 21:17 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-23 21:17 | +5 | HYPE | DOWN | 0.60 | 0.68 | 0.47 |
| 11-23 21:17 | +10 stop | XRP | DOWN | 0.52 | 0.33 | -2.24 |
| 11-23 21:17 | +20 | XRP | DOWN | 0.52 | open |  |
| 11-23 21:17 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-23 21:17 | +10 | XRP | DOWN | 0.52 | open |  |
