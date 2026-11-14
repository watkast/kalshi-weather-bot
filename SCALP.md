# Range-Scalp Bot

*Updated Sat Nov 14 05:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59102 | 51570 | 7532 (106) | 4 | $-15953.45 | -4.3% |
| **+10¢** | 44152 | 35340 | 8812 (139) | 5 | $-14964.17 | -5.4% |
| **+15¢** | 36996 | 27497 | 9499 (174) | 7 | $-13583.05 | -5.9% |
| **+20¢** | 32957 | 22983 | 9974 (226) | 7 | $-11985.27 | -5.8% |
| **+10¢ (15¢ stop)** | 71943 | 71805 | 138 (82) | 4 | $-26452.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 05:24 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 05:24 | +5 | BNB | UP | 0.68 | open |  |
| 11-14 05:23 | +10 stop | DOGE | UP | 0.66 | open |  |
| 11-14 05:23 | +15 | DOGE | UP | 0.66 | open |  |
| 11-14 05:23 | +10 | DOGE | UP | 0.66 | open |  |
| 11-14 05:23 | +5 | DOGE | UP | 0.66 | open |  |
| 11-14 05:23 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 11-14 05:23 | +20 | SOL | UP | 0.70 | open |  |
| 11-14 05:23 | +15 | SOL | UP | 0.70 | open |  |
| 11-14 05:23 | +10 | SOL | UP | 0.70 | 0.81 | 0.84 |
| 11-14 05:23 | +5 | SOL | UP | 0.70 | 0.76 | 0.32 |
| 11-14 05:23 | +5 | BNB | UP | 0.62 | 0.71 | 0.58 |
| 11-14 05:23 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.74 |
| 11-14 05:22 | +10 stop | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-14 05:22 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-14 05:22 | +10 | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-14 05:22 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-14 05:22 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 05:22 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-14 05:22 | +10 | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 05:22 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.40 |
| 11-14 05:22 | +5 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 11-14 05:22 | +5 | NEAR | UP | 0.61 | 0.67 | 0.27 |
| 11-14 05:22 | +10 stop | BNB | UP | 0.66 | open |  |
| 11-14 05:22 | +20 | BNB | UP | 0.66 | open |  |
| 11-14 05:22 | +15 | BNB | UP | 0.66 | open |  |
| 11-14 05:22 | +10 | BNB | UP | 0.66 | open |  |
| 11-14 05:22 | +5 | BNB | UP | 0.66 | 0.72 | 0.29 |
| 11-14 05:21 | +10 stop | ZEC | UP | 0.55 | open |  |
| 11-14 05:20 | +10 stop | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +20 | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +15 | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +10 | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 11-14 05:20 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-14 05:20 | +10 stop | XRP | UP | 0.54 | 0.38 | -1.94 |
| 11-14 05:19 | +5 | HYPE | UP | 0.67 | open |  |
| 11-14 05:19 | +10 stop | ZEC | UP | 0.70 | 0.49 | -2.43 |
| 11-14 05:18 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-14 05:18 | +10 stop | HYPE | UP | 0.65 | 0.45 | -2.34 |
